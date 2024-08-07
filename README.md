# Ejecución del Proyecto Flask

Este proyecto utiliza Flask para calcular la secuencia Fibonacci y enviar correos electrónicos basados en la hora actual o en un tiempo específico proporcionado.

## Requisitos Previos

Asegúrate de tener instalado lo siguiente:

- Python (preferiblemente Python 3.x)
- pip (administrador de paquetes de Python)

## Configuración del Entorno

1. **Instalación de Dependencias**

   Abre una terminal y navega hasta la carpeta raíz del proyecto. Ejecuta el siguiente comando para instalar las dependencias necesarias:

   ```bash
   pip install -r requirements.txt
    ```
2. **Activar el Entorno Virtual**
    ```bash
     source venv/bin/activate   # Linux/macOS
     venv\Scripts\activate      # Windows
    ```
3. **Iniciar el Servidor**
   Ejecutar
     ```bash
      flask run
    ```
## Uso de la API
1. **Endpoint /fibonacci**
Este endpoint calcula la secuencia Fibonacci basada en la hora actual y devuelve un JSON con los resultados.
URL: http://localhost:5000/fibonacci
URL DESPLIEGUE: https://14f0-2800-e2-1e80-1497-f8ac-eb0e-b237-7d72.ngrok-free.app/fibonacci

2. **Endpoint /fibonacci/<time>**
Este endpoint calcula la secuencia Fibonacci basada en un tiempo específico proporcionado en formato HH:MM:SS y envía un correo electrónico con los resultados.
URL: http://localhost:5000/fibonacci_time
URL DESPLIEGUE: https://14f0-2800-e2-1e80-1497-f8ac-eb0e-b237-7d72.ngrok-free.app/fibonacci/10:20:30
Cuerpo de la Solicitud (JSON):
