# Control de camara con OpenCV

## Configuracion del Entorno

Recomendado el uso de miniConda para gestionar el entorno:
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

  1. Acceso a Hardware: Conexion con la webcam
  2. Analisis de Arrays(Numpy): Obtener la resolucion y canales de color analizando la forma de la imagen
  3. Procesamiento en Tiempo Real (versiones previas):
       - Dibujo de formas geométricas
       - Rescalado dinámico a 100x100px
  4. Metricas de Rendimiento: Calculo de FPS y tiempo de refresco
  5. Modo Rafaga: Captura de 5 fotos con cadencia programable

## Controles del Programa

Al ejecutar python src/main.py se abrira una ventana en vivo con los siguientes controles:

  - Tecla s: Inicia la rafaga de 5 capturas en tiempo real
  - Tecla q: Cierra la aplicacion y libera la camara



