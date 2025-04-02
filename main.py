import cv2
import pyttsx3
import threading
from deepface import DeepFace

# Inicialización del sintetizador de voz
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# Configuración de detección de movimiento
fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=50, detectShadows=True)

# Configuración del rastreador de objetos
tracker = cv2.legacy.TrackerCSRT_create()

# Captura de video
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: No se pudo acceder a la cámara.")
    exit()

# Leer el primer frame para inicializar el rastreador
ret, frame = cap.read()
if not ret:
    print("Error al capturar el video")
    cap.release()
    cv2.destroyAllWindows()
    exit()

# Inicializar la detección de rostros
bbox = None
mensaje_anterior = ""

def reconocimiento(frame):
    try:
        frame_resized = cv2.resize(frame, (224, 224))  # Reducir tamaño para mejorar rendimiento
        recognition = DeepFace.find(frame_resized, db_path='db', model_name='VGG-Face', silent=True)
        if recognition and isinstance(recognition, list) and len(recognition[0]) > 0:
            return recognition[0]['identity'][0].split('/')[-2]
    except (ValueError, KeyError, IndexError):
        return 'Rostro No Detectado'
    return 'Rostro No Detectado'

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detección de movimiento
    fgmask = fgbg.apply(frame)
    fgmask = cv2.GaussianBlur(fgmask, (5, 5), 0)
    _, movement = cv2.threshold(fgmask, 254, 255, cv2.THRESH_BINARY)

    # Seguimiento de personas
    if bbox is not None:
        success, bbox = tracker.update(frame)
        if success:
            x, y, w, h = map(int, bbox)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, "Seguimiento", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        else:
            bbox = None
            cv2.putText(frame, "Perdido", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Reconocimiento facial solo si hay movimiento significativo
    if cv2.countNonZero(movement) > 500:
        mensaje = reconocimiento(frame)
        if mensaje != mensaje_anterior and mensaje != 'Rostro No Detectado':
            threading.Thread(target=speak, args=(f"Hola {mensaje}",)).start()
        mensaje_anterior = mensaje
    else:
        mensaje = "Sin movimiento"

    cv2.putText(frame, mensaje, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Mostrar los resultados
    cv2.imshow("Cuadro Original", frame)
    cv2.imshow("Detección de Movimiento", movement)

    # Salir con la tecla 'q'
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

