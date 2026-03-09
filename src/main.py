import cv2
import os
import time # Librería necesaria para medir el tiempo


folder = '../images'
if not os.path.exists(folder):
    os.makedirs(folder)


cap = cv2.VideoCapture(0)

print("Calculando FPS en tiempo real... Presiona 'q' para salir.")



while True:
    
    start_time = time.time()

    ret, frame = cap.read()
    if not ret:
        break

    
    

    # Tiempo de refresco: Diferencia entre el tiempo actual y el anterior
    # FPS = 1 / Tiempo de refresco
    end_time = time.time()
    tiempo_refresco = end_time - start_time
    
    
    if tiempo_refresco > 0:
        fps = 1 / tiempo_refresco
    else:
        fps = 0

    texto = f"FPS: {int(fps)} | Refresco: {tiempo_refresco:.4f}s"
    cv2.putText(frame, texto, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    
    cv2.imshow('Analisis de Rendimiento', frame)

   
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        cv2.imwrite(os.path.join(folder, 'captura_fps.png'), frame)
        print(f"Foto guardada. FPS registrados: {fps:.2f}")
        break
    elif key == ord('q'):
        break

# Limpieza
cap.release()
cv2.destroyAllWindows()