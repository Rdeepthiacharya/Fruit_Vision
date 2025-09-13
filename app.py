from flask import Flask, request, render_template
from markupsafe import escape
import os
import numpy as np
import tensorflow as tf
from keras.models import load_model
from keras.preprocessing import image
from werkzeug.utils import secure_filename

# Get the root directory of the app
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# Load the pre-trained fruit classification model
model = load_model("models/fruits.keras")

# Define the class names for the fruit classification
class_name = [
    'Fresh Apple',
    'Fresh Banana',
    'Fresh Orange',
    'Rotten Apple',
    'Rotten Banana',
    'Rotten Orange'
]

# Initialize Flask app
app = Flask(__name__)

# Set the upload folder for saving images
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    
# Render the pages

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    prediction = ''
    confidence = ''
    image_url = None

    if request.method == 'POST':
        # Check if an image file was uploaded
        if 'fruit' in request.files:
            file = request.files['fruit']
            if file.filename != '':
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                image_url = '/' + filepath.replace('\\', '/')

                # Preprocess the image for prediction
                test_image = image.load_img(filepath, target_size=(300, 300))
                test_image = image.img_to_array(test_image)
                test_image = np.expand_dims(test_image, axis=0)
                # Make prediction using the loaded model
                prediction = model.predict(test_image)

                # Get the predicted class and confidence value
                predicted_class = class_name[np.argmax(prediction[0])]
                confidence_val = round(np.max(prediction[0]) * 100)

                # Format the prediction and confidence for display
                prediction = "prediction -> " + str(predicted_class)
                confidence = "chances -> " + str(confidence_val) + "%"

    # Render the prediction page with results and image
    return render_template("prediction.html", prediction=prediction, confidence=confidence, image_url=image_url)

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.debug = True
    app.run()