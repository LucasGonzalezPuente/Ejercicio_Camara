import cv2
import os
import time

folder = '../images'
if not os.path.exists(folder):
    os.makedirs(folder)

cadencia = 1.0  
cap = cv2.VideoCapture(0)

print(f"Presiona 's' para ráfaga REAL de 5 fotos cada {cadencia}s.")

while True:
    ret, frame = cap.read()
    if not ret: break

    
    
    cv2.imshow('Webcam', frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        for i in range(1, 6):
            print(f"Capturando foto {i}...")

            # --- Vaciar el búfer ---
            # Leemos 5 veces seguidas rápidamente para descartar 
            # las imágenes viejas que quedaron en el cable/memoria.
            for _ in range(5):
                cap.read() 
            
            
            ret, frame_actual = cap.read()
            
            if ret:
                nombre = os.path.join(folder, f"foto_real_{i}.png")
                cv2.imwrite(nombre, frame_actual)
                print(f"Guardada: {nombre}")
                
                if i < 5:
                    print(f"Esperando {cadencia} segundos...")
                    time.sleep(cadencia)
            
        print("Ráfaga terminada con éxito.")
        break
        
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()