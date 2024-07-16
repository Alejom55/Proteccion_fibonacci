from flask import Flask, request, make_response, redirect, render_template
from datetime import datetime
from sendEmail import emailSender
from decouple import config
# from flask_ngrok import run_with_ngrok
app = Flask(__name__)
PASSWORD = config('EMAIL_PASSWORD')
EMAIL_SENDER = config('EMAIL_SENDER')
# run_with_ngrok(app)

# Función para calcular la secuencia Fibonacci
def fibonacci(n, first, second):
    if n < 0:
        raise ValueError("The number n must be greater than or equal to 0.")
    elif n == 0:
        return [first]
    elif n == 1:
        return [first, second]
    else:
        listNumbers = [first, second]
        for k in range(2, n+2):
            n = first + second
            listNumbers.append(n)
            second = first
            first = n
        listNumbers.sort(reverse=True)
        return listNumbers

# Función para enviar el correo con la secuencia Fibonacci
def sendEmailWithFibonacci(response_data):
    sequenceFibonacci = response_data["sequence"]
    currentSeconds = response_data["seconds"]
    minutes = response_data["minutes"]
    hours = response_data["hours"]

    sender = EMAIL_SENDER
    # recipients = ["didier.correa@proteccion.com.co", "correalondon@gmail.com"]
    recipients = ["misteriosoA55@gmail.com", "gracruxouhacre-8415@yopmail.com"]
    subject = "Prueba Técnica - Alejandro Marín Henao"
    message = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                background-color: #f0f0f0;
                padding: 20px;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                background-color: #ffffff;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 20px rgba(0,0,0,0.1);
            }}
            h2 {{
                color: #333333;
                border-bottom: 1px solid #eeeeee;
                padding-bottom: 10px;
            }}
            p {{
                margin: 10px 0;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Secuencia Fibonacci</h2>
            <p>La secuencia Fibonacci generada es: {', '.join(map(str, sequenceFibonacci))}</p>
            <p>Hora de extracción: {hours}:{str(minutes).zfill(2)}:{str(currentSeconds).zfill(2)}</p>
            <p>Gracias por tu atención.</p>
        </div>
    </body>
    </html>
    """
    password = PASSWORD

    try:
        emailSender(sender, recipients, subject, message, password)
        return "Email sent successfully with Fibonacci sequence."
    except smtplib.SMTPAuthenticationError:
        return "Failed to send email: Authentication error. Please check sender's email credentials.", 500
    
    except smtplib.SMTPException as e:
        return f"Failed to send email: {str(e)}", 500
    
    except Exception as e:
        return f"Failed to send email: {str(e)}", 500

# Endpoint para calcular y retornar la secuencia Fibonacci
@app.route('/fibonacci')
def fibonacci_endpoint():
    response_data = generateData()
    return response_data

# Endpoint para calcular la secuencia Fibonacci basado en el tiempo especificado
@app.route('/fibonacci/<time>')
def fibonacciTime(time):
    try:
        hours, minutes, seconds = map(int, time.split(':'))
        ordered_minutes_str = ''.join(sorted(str(minutes).zfill(2)))
        sequence = fibonacci(seconds, int(
            ordered_minutes_str[0]), int(ordered_minutes_str[1]))
        response_data = {
            "sequence": sequence,
            "seconds": seconds,
            "minutes": minutes,
            "hours": hours
        }
        sendEmailWithFibonacci(response_data)
        return response_data
    except ValueError:
        return {"error": "Invalid time format. Please use HH:MM:SS"}, 400

# Función para obtener la hora actual y calcular la secuencia Fibonacci
def generateData():
    now = datetime.now()
    current_hour = now.hour
    current_minutes = now.minute
    minutes_str = str(current_minutes).zfill(2)
    ordered_minutes_str = ''.join(sorted(minutes_str))
    current_seconds = now.second
    sequence = fibonacci(
        current_seconds, int(ordered_minutes_str[0]), int(ordered_minutes_str[1]))
    response_data = {
        "sequence": sequence,
        "seconds": current_seconds,
        "minutes": current_minutes,
        "hours": current_hour
    }
    sendEmailWithFibonacci(response_data)
    return response_data


if __name__ == '__main__':
    app.run(debug=True)
