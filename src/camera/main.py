from fastapi import FastAPI, HTTPException, Response
from qreader import QReader
import cv2
import json
import os
from datetime import datetime

# Create a QReader instance
qreader = QReader()

app = FastAPI()

# File path to store JSON data
json_file_path = "qr_code_data.json"

# Dictionary to store QR code data
qr_code_data = {}

# Load existing data from JSON file
if os.path.exists(json_file_path):
    with open(json_file_path, 'r') as file:
        qr_code_data = json.load(file)

@app.get('/capturar')
async def capturar_qr_code():
    # Capture an image from the webcam
    camera = cv2.VideoCapture(1)
    _, image = camera.read()
    camera.release()

    # Save the image
    cv2.imwrite("qrcode.png", image)

    # Get the image that contains the QR code
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Use the detect_and_decode function to get the decoded QR data
    decoded_text = qreader.detect_and_decode(image=image)

    # Obter a data e hora atual
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Store the decoded data and timestamp in the dictionary
    qr_code_data['QR_Code_{}'.format(len(qr_code_data) + 1)] = {'data': decoded_text, 'data_hora': current_time}

    # Write data to JSON file
    with open(json_file_path, 'w') as file:
        json.dump(qr_code_data, file, indent=4)

    # Return the decoded text
    return {'Dados': decoded_text}

@app.get('/mostrar_dados_qr')
async def mostrar_dados_qr():
    # Return the dictionary containing QR code data
    return qr_code_data
