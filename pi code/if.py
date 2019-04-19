import cv2
import requests
import os
import urllib.request

def send_data_to_server(image_path):  
    form_data = open(image_path, 'rb')
    print(form_data)
    files = {'file': form_data}
    print(files['file'])
    url='http://a1c199ec.ngrok.io'
    response = requests.post(url+'/result', files=files)
    print(response)
    r=requests.get(url+'/return')
    rr=r.text
    # rr=urllib.request.urlopen('http://6819d7ff.ngrok.io/return').read()
    print(rr)

send_data_to_server('./upload/test_mnist.png')