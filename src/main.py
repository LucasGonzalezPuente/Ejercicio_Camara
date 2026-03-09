import cv2
import os


folder = '../images'
if not os.path.exists(folder):
    os.makedirs(folder)


cap = cv2.VideoCapture(0)


if not cap.isOpened():
    print("Error: No se pudo acceder a la webcam.")
    exit()

print("--- Webcam en VIVO a 100x100 px ---")
print("Presiona 's' para guardar la foto rescalada.")
print("Presiona 'q' para salir sin guardar.")

while True:
    
    ret, frame = cap.read()
    if not ret:
        break

  
    # Interpolation=cv2.INTER_AREA, el mejor para reducir imágenes(promedia pixeles vecinos)
    frame_rescalado = cv2.resize(frame, (100, 100), interpolation=cv2.INTER_AREA)


    alto_n, ancho_n, _ = frame_rescalado.shape
    

    centro_x = ancho_n // 2
    centro_y = alto_n // 2
    punto_centro = (centro_x, centro_y)


    
    cv2.circle(frame_rescalado, punto_centro, 20, (0, 255, 0), 2)
    cv2.circle(frame_rescalado, punto_centro, 2, (0, 0, 255), -1)

    
    cv2.imshow('Live a 100x100', frame_rescalado)

    
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('s'):
        
        img_name = os.path.join(folder, 'captura_100x100.png')
        cv2.imwrite(img_name, frame_rescalado)
        
        print(f"\n" + "="*30)
        print("DATOS DE LA FOTO GUARDADA")
        print("="*30)
        print(f"Resolución guardada: {ancho_n}x{alto_n} px")
        print(f"Análisis del Array: {frame_rescalado.shape}")
        print(f"Total de píxeles: {frame_rescalado.size}")
        print("="*30 + "\n")
        
        break 
        
    elif key == ord('q'):
        print("Cerrando sin guardar.")
        break 

#
cap.release()
cv2.destroyAllWindows()
print("Programa finalizado.")