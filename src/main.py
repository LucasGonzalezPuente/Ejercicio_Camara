import cv2
import os

folder = '../images'

if not os.path.exists(folder):
    os.makedirs(folder)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR: No se pudo acceder a la camara")
else:
    print("Camara detectada. Presiona 's' para hacer una foto o 'q' para salir")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("ERROR: No se pudo recibir el frame")
            break

        cv2.imshow('Previsualizacion - Presiona S para guardar', frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):
            img_name = os.path.join(folder, "captura_ejercicio.png")
            cv2.imwrite(img_name, frame)
            print(f"Imagen guardada en {img_name}")

        elif key == ord('q'):
            print("Cerrando sin guardar")
            break

    cap.release()
    cv2.destroyAllWindows()


