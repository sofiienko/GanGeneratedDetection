import io
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
from PIL import Image

import flask
from flask import send_file,  abort
from flask import jsonify, make_response
from flask_cors import CORS


# initialise Flask application and Keras model 
app = flask.Flask(__name__)
CORS(app)
predicted_image_name = 'predicted.png'
IMG_SIZE = (224, 224)

trained_model = tf.keras.models.load_model(os.path.join('trained','Densenet_categorical_10_11_20'))

@app.route('/ping')
def hello_world():
    return 'pong'

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