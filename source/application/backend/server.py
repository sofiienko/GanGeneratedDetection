import io
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
from PIL import Image

import flask
from flask import send_file,  abort
from flask import jsonify, make_response
from flask import request
from flask_cors import CORS

	
from pymemcache.client import base

cache = base.Client(('localhost', 11211))

# initialise Flask application and Keras model 
app = flask.Flask(__name__)
CORS(app)
predicted_image_name = 'predicted.png'
IMG_SIZE = (224, 224)

#trained_model = tf.keras.models.load_model(os.path.join('trained','Densenet_categorical_10_11_20'))

@app.route('/backend/test/ping')
def ping():
    return 'pong'
	
@app.route('/backend/test/cache', methods=['POST', 'GET'])
def hello_world():
    if flask.request.method == 'POST':
        sessionId = request.args.get('id')
        data = request.json
        cache.set(sessionId, data)
        return make_response('pong ' + sessionId, 200)
    else:
        sessionId = request.args.get('id')
        data = cache.get(sessionId)
        return make_response(data,200)

	
@app.route('/backend/image1', methods=['POST'])
def img1():
    if not flask.request.files['photos']: return abort(401)
    sessionId = request.args.get('id')
    
    imageFormRequest = flask.request.files['photos'].read()
    img = Image.open(io.BytesIO(imageFormRequest))
    cache.set(sessionId + "img1", img)
    return make_response("", 200)


app.route('/backend/image1', methods=['POST'])
def img2():
    if not flask.request.files['photos']: return abort(401)
    sessionId = request.args.get('id')
    

    imageFormRequest = flask.request.files['photos'].read()
    img = Image.open(io.BytesIO(imageFormRequest))
    cache.set(sessionId + "img2", img)
    return make_response("", 200)

app.route('/backend/result', methods=['POST'])
def getResult():
    return send_file(
    io.BytesIO(image_binary),
    mimetype='image/jpeg',
    as_attachment=True,
    attachment_filename='result.jpg')

@app.route('/predict', methods=['POST'])
def predict():
    print('New request')
    print(flask.request)
    if flask.request.files['photos']:
        imageFormRequest = flask.request.files['photos'].read()
        row_img = Image.open(io.BytesIO(imageFormRequest))
        resized_img = row_img.resize(IMG_SIZE, Image.ANTIALIAS)

        batch = []
        batch.append(np.array(resized_img)/255.)
        prediction = trained_model.predict(np.array(batch))
        return make_response(jsonify(({'probability': str(prediction[(0,0)])})), 200)

    return abort(401)



if __name__=='__main__':
    print(('* loading Keras model and Flask starting server'))
    #global model
    #model = load_model()
    #global graph
    #graph = tf.get_default_graph()

    app.run(host='0.0.0.0',port=5000, debug = True)