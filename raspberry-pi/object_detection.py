import cv2
import numpy as np
import bluetooth
import time
from tflite_runtime.interpreter import Interpreter

# Charger le modèle YOLOv4-tiny (à placer dans le dossier model/)
model = Interpreter(model_path="model/yolov4-tiny.tflite")
model.allocate_tensors()

# Configurer la connexion Bluetooth
ev3_mac_address = "00:16:53:1A:B1:2E"  # Remplace par l'adresse MAC de ton EV3
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((ev3_mac_address, 1))

# Capture vidéo
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Prétraitement (redimensionner, normaliser, etc.)
    input_data = cv2.resize(frame, (320, 320))
    input_data = np.expand_dims(input_data, axis=0)

    # Inférence
    model.set_tensor(input_details[0]['index'], input_data)
    model.invoke()
    output_data = model.get_tensor(output_details[0]['index'])

    # Traitement des résultats (exemple simplifié)
    # Supposons que la détection retourne une liste d'objets avec leur position
    # obj = [x_min, y_min, x_max, y_max, confidence, class_id]
    obj = detect_objects(output_data)  # Fonction à définir pour traiter les résultats

    if obj:
        x_center = (obj[0] + obj[2]) / 2
        width = obj[2] - obj[0]

        # Exemple de logique de décision
        if width > 100:  # Si l'objet est proche
            if x_center < 100:
                sock.send("TURN:LEFT:45")
            elif x_center > 220:
                sock.send("TURN:RIGHT:45")
            else:
                sock.send("MOVE:BACKWARD:30")
        else:
            sock.send("MOVE:FORWARD:30")

    # Afficher la vidéo
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
sock.close()