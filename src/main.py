import cv2
import os

# 1. Preparar carpeta
folder = '../images'
if not os.path.exists(folder):
    os.makedirs(folder)

# 2. Iniciar cámara
cap = cv2.VideoCapture(0)

print("Cámara detectada. Presiona 's' para guardar o 'q' para salir.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # --- ANÁLISIS DEL ARRAY 
    alto, ancho, _ = frame.shape
    centro_x = ancho // 2
    centro_y = alto // 2
    punto_centro = (centro_x, centro_y)


    cv2.circle(frame, punto_centro, 50, (0, 255, 0), 3)
    cv2.circle(frame, punto_centro, 2, (0, 0, 255), -1)

    
    cv2.imshow('Webcam con Circulo Central', frame)

    
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        ruta_guardado = os.path.join(folder, 'captura_circulo.png')
        cv2.imwrite(ruta_guardado, frame)
        print(f"¡Imagen guardada con éxito en {ruta_guardado}!")
        print(f"Resolución analizada: {ancho}x{alto} px")
        break 
        
    elif key == ord('q'):
        print("Cerrando sin guardar.")
        break 

# 3. Limpieza final
cap.release()
cv2.destroyAllWindows()