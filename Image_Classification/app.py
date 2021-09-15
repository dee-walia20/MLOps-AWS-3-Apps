from flask import Flask, render_template, request
import cv2
import numpy as np
import os
import tensorflow as tf

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

#print(tf.config.list_physical_devices('GPU'))

from tensorflow.keras.models import load_model
from tensorflow.keras.applications.xception import decode_predictions
from tensorflow.keras.applications.xception import preprocess_input
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

model = load_model('model.h5')

labels = pd.read_csv("labels.txt", sep="\n").values

@app.route('/')
def index():
    return render_template("index.html", data="hey")

@app.route("/prediction", methods=["POST"])
def prediction():
    img = request.files['img']
    img.save("static/img.jpg")
    image = cv2.imread("static/img.jpg")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (299,299))
    image = np.reshape(image, (1,299,299,3))
    image = preprocess_input(image)
    pred = model.predict(image)
    #pred = np.argmax(pred)
    pred = decode_predictions(pred, top=1)[0][0][1]
    print(pred)
    #pred = labels[pred]
    return render_template("prediction.html", data=pred)

# To avoid cachinng problem. always the first was getting uploaded in prediction page previosuly.
@app.after_request
def add_header(response):
    response.cache_control.max_age = 0
    return response

if __name__ == "__main__":
    app.run(debug=True)