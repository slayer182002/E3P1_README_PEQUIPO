import cv2
import numpy as np
import sqlite3
from datetime import datetime
import joblib
import os

# Cargar modelo SVM y clasificador de rostros
model = joblib.load("mask_detector_svm.pkl")
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Crear carpeta si no existe
if not os.path.exists("capturas"):
    os.makedirs("capturas")

# Crear base de datos y tabla
conn = sqlite3.connect("eventos.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS eventos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha_hora TEXT NOT NULL,
        ruta_imagen TEXT NOT NULL
    )
''')
conn.commit()

# Función para guardar evento
def guardar_evento(ruta):
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO eventos (fecha_hora, ruta_imagen) VALUES (?, ?)", (fecha_hora, ruta))
    conn.commit()

# Iniciar cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        rostro = frame[y:y+h, x:x+w]
        rostro_resized = cv2.resize(rostro, (100, 100))  # Asegúrate de que coincida con tu entrenamiento
        rostro_flattened = rostro_resized.flatten().reshape(1, -1) / 255.0  # Normalizar

        pred = model.predict(rostro_flattened)[0]
        label = "Con Cubrebocas" if pred == 0 else "Sin Cubrebocas"
        color = (0, 255, 0) if label == "Con Cubrebocas" else (0, 0, 255)

        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        # Guardar evento si no tiene cubrebocas
        if label == "Sin Cubrebocas":
            nombre_imagen = f"capturas/alerta_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            cv2.imwrite(nombre_imagen, frame)
            guardar_evento(nombre_imagen)

    cv2.imshow("Detección Cubrebocas", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
conn.close()
cv2.destroyAllWindows()
