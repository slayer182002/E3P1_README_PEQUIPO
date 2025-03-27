# Configuración del sintetizador de voz
engine = pyttsx3.init()
engine.setProperty('rate', 125)

# Configuración de detección de movimiento
fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=50, detectShadows=True)

# Configuración del rastreador de objetos
tracker = cv2.legacy.TrackerCSRT_create()

# Captura de video
cap = cv2.VideoCapture(0)

# Leer el primer frame para inicializar el rastreador
ret, frame = cap.read()
if not ret:
    print("Error al capturar el video")
    cap.release()
    cv2.destroyAllWindows()
    exit()

# Función de reconocimiento facial
def reconocimiento(frame):
    try:
        recognition = DeepFace.find(frame, db_path='db', model_name='VGG-Face', silent=True)
        nombre = recognition[0]['identity'][0].split('/')[-2]  # Extrae el nombre del archivo en la BD
        return nombre
    except (ValueError, KeyError):
        return 'Rostro No Detectado'

# Variable para evitar repetición de nombres
mensajeAnterior = ""

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detección de movimiento
    fgmask = fgbg.apply(frame)
    _, movement = cv2.threshold(fgmask, 254, 255, cv2.THRESH_BINARY)

    # Seguimiento de personas
    success, bbox = tracker.update(frame)
    if success:
        x, y, w, h = map(int, bbox)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, "Seguimiento", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    else:
        cv2.putText(frame, "Perdido", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Reconocimiento facial
    mensaje = reconocimiento(frame)
    if mensaje != mensajeAnterior:
        if mensaje != 'Rostro No Detectado':
            engine.say(f"Hola {mensaje}")
            engine.runAndWait()
        mensajeAnterior = mensaje

    cv2.putText(frame, mensaje, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Mostrar los resultados
    cv2.imshow("Cuadro Original", frame)
    cv2.imshow("Detección de Movimiento", movement)

    # Salir con la tecla 'q'
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
