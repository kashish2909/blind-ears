from flask import Flask
from flask import request, jsonify, redirect, url_for
from flask import Flask, render_template, request,Response
from werkzeug.utils import secure_filename
import requests
import numpy as np
#import scipy
import cv2
import os
#from skimage.transform import resize, pyramid_reduce
from keras.models import load_model
import PIL
from PIL import Image
import tensorflow as tf
from requests.models import Response

model=load_model('mnist.h5')
graph=tf.get_default_graph()

UPLOAD_FOLDER = os.path.basename('uploads')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


result=0


@app.route('/')
def student():
   return render_template('index.html')

#blind-ears
@app.route('/result',methods = ['POST'])
def hello_world():
    print(request.files['file'])
    file = request.files['file']
    # file=files.media
    # file=cv2.imread('./uploads')
    # image_test=Image.open(file)
    # image_test=np.asarray(image_test)
    # image_test=cv2.resize(image_test,(28,28))
    # image_test = np.reshape(image_test,(1,28,28,3))
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    path=os.path.join('./uploads',file.filename)
    image_test=cv2.imread(path,0)
    image_test=255-image_test
    image_test=image_test/255.0
    image_test=cv2.resize(image_test,(28,28))
    # print(file.filename)
    # image_test=cv2.resize(image_test,(224,224))
    #image_test=image_test.get()
    #image_test = scipy.misc.imresize(image_test, [224,224])
    image_test = np.reshape(image_test,(1,28,28,1))
    with graph.as_default():
        result=model.predict(image_test)
    result=np.argmax(result,axis=1)
    result=str(int(result))
    f = open("./templates/result.html","w")
    f.write(result)
    print(result)
    # data = {'name': 'nabin khadka'}
    # return jsonify(data)
    return result

@app.route('/return')
def setres():
    return render_template('result.html')

if __name__ == '__main__':
#    print("predicting") 
   app.debug=True
   app.run()
   app.run(debug=True)
