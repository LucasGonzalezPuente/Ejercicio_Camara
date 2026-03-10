import cv2
import numpy as np
import os
import time

folder = '../images'
if not os.path.exists(folder):
    os.makedirs(folder)

cap = cv2.VideoCapture(0)


piel_bajo = np.array([0, 30, 60])
piel_alto = np.array([20, 150, 255])


ret, frame_anterior = cap.read()

gris_anterior = cv2.cvtColor(frame_anterior, cv2.COLOR_BGR2GRAY)

print("Iniciando Deteccion Integral (Movimiento + Color Carne)...")
print("Presiona 'q' para salir.")

while True:
    ret, frame_actual = cap.read()
    if not ret: break

    
    gris_actual = cv2.cvtColor(frame_actual, cv2.COLOR_BGR2GRAY)
    
    
    diferencia = cv2.absdiff(gris_anterior, gris_actual)
    
    
    _, mascara_movimiento = cv2.threshold(diferencia, 30, 255, cv2.THRESH_BINARY)

    
    hsv = cv2.cvtColor(frame_actual, cv2.COLOR_BGR2HSV)
    mascara_color_binaria = cv2.inRange(hsv, piel_bajo, piel_alto)
    
  
    gris_actual_3ch = cv2.cvtColor(gris_actual, cv2.COLOR_GRAY2BGR) 
    color_carne_segmentado = cv2.bitwise_and(gris_actual_3ch, gris_actual_3ch, mask=mascara_color_binaria)

    final_combinado = cv2.bitwise_and(mascara_movimiento, mascara_color_binaria)

    
    pixeles_movimiento_piel = np.sum(final_combinado == 255)
    if pixeles_movimiento_piel > 3000: 
        cv2.putText(frame_actual, "MOVIMIENTO DE PIEL DETECTADO", (50, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    
    cv2.imshow('1. Webcam Principal (con Alerta)', frame_actual)
    cv2.imshow('2. Deteccion de Movimiento Puro (Mascara)', mascara_movimiento)
    cv2.imshow('3. Segmentacion de Color Carne (Textura)', color_carne_segmentado)
    cv2.imshow('4. Resultado Final Combinado', final_combinado)

    
    gris_anterior = gris_actual.copy()

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()