from flask import Flask, render_template, url_for, request, jsonify
from tensorflow import keras
from PIL import Image
import numpy as np

app = Flask(__name__)

model = keras.models.load_model('trainedmodel_10class.hdf5')

def preprocess_image(image):
    image = image.resize((299, 299))
    image = np.array(image)
    image = image/255
    image = np.expand_dims(image, axis=0)
    image = np.vstack([image]) 
    return image

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/classifier')
def classifier():
    return render_template('classifier.html')

@app.route('/upload', methods = ['POST'])
def upload_image():
    uploaded_image = request.files['image']

    if uploaded_image:
        try:
            image = Image.open(uploaded_image)
            processed_image = preprocess_image(image)
            prediction = model.predict(processed_image)

            food_classes = ['cheesecake', 'chicken_wings', 'chocolate_cake', 'club_sandwich',
                            'garlic_bread', 'lasagna', 'nachos', 'pizza',
                            'samosa', 'waffles']

            predicted_class = food_classes[np.argmax(prediction)]
            return {"prediction": predicted_class}
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        return jsonify({"Error" : "No image file provided"})


if __name__ == '__main__':
    app.run(debug=True)