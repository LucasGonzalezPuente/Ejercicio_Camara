import cv2
import os

# Ruta para guardar
folder = '../images'
if not os.path.exists(folder):
    os.makedirs(folder)

# Iniciar cámara
cap = cv2.VideoCapture(0)

print("Camara detectada. Presiona 's' para hacer una foto o 'q' para salir")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('Captura de imagen', frame)
    
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('s'):
        # --- ANÁLISIS DEL ARRAY ---
        dimensiones = frame.shape
        alto = dimensiones[0]
        ancho = dimensiones[1]
        canales = dimensiones[2]

        print("\n" + "="*30)
        print("DATOS DEL ARRAY DE LA IMAGEN")
        print("="*30)
        print(f"Resolución: {ancho} px (ancho) x {alto} px (alto)")
        print(f"Canales de color: {canales}")
        print(f"Total de píxeles: {frame.size}")
        print("="*30 + "\n")

        # Guardar imagen
        cv2.imwrite(os.path.join(folder, 'foto_resolucion.png'), frame)
        print("Imagen guardada en la carpeta images/")
        break
        
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()