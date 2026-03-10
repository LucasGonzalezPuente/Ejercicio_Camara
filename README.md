# Control de camara con OpenCV

## Configuracion del Entorno

Recomendado el uso de miniConda para gestionar el entorno
  ## Crear el entorno
  - conda create -n vision python=3.10 -y
  - conda activate vision

  ## Instalar librerías necesarias
  pip install -r requirements.txt

## Estructura del Proyecto

  - src/main.py: Script principal con la lógica de procesamiento
  - images/: Directorio donde se guardan las imágenes
  - requirements.txt: Lista de librerías Python necesarias

## Flow de la Aplicación

  1. Acceso a Hardware: Conexión con la webcam mediante cv2.VideoCapture.

  2. Análisis de Arrays (NumPy): Obtención de resolución y canales de color analizando la forma (shape) de la imagen.

  3. Detección de Movimiento: Uso de la diferencia absoluta entre fotogramas consecutivos (cv2.absdiff) y umbralización binaria.

  4. Segmentación por Color: Filtrado en espacio de color HSV para aislar tonos de piel (color carne).

  5. Lógica Combinada: Intersección mediante operaciones bitwise para detectar movimiento exclusivamente en áreas con presencia de piel.

  6. Métricas de Rendimiento: Cálculo de FPS y tiempo de refresco en tiempo real.
  

## Controles del Programa

Al ejecutar python src/main.py se abrira una ventana en vivo con los siguientes controles:

  - Tecla s: Inicia la rafaga de 5 capturas en tiempo real
  - Tecla q: Cierra la aplicacion y libera la camara



