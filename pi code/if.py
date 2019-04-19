import cv2
import requests
import os

def send_data_to_server(image_path):  
    form_data = open(image_path, 'rb')
    print(form_data)
    files = {'media': form_data}
    print(files['media'])
    response = requests.post('http://127.0.0.1:5000/result', files=files)
    print(response)

send_data_to_server('./upload/test_mnist.png')