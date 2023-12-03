from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
import webbrowser
import numpy as np
import io
import base64
from PIL import Image
import cv2

app = Flask(__name__)

# Load the pickled model file
model = load_model("happysadmodel.h5")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/prediction", methods=['POST'])
def prediction():

    image = request.files["image"]
    image.save("image.jpg")
    image = cv2.imread("image.jpg")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image = cv2.resize(image, (256, 256))
    image = np.reshape(image, (1,256,256,3))

    predictions = model.predict(image)

    return render_template("prediction.html", data=predictions)

if __name__ == "__main__":
    webbrowser.open_new('http://localhost:5000/')
    app.run(debug=True)
