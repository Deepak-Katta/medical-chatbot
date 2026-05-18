from flask import Flask, render_template, request
from chatbot import get_response
import os
import cv2

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():

    user_message = request.form['message']

    response = get_response(user_message)

    return response

@app.route('/upload', methods=['POST'])
def upload_image():

    file = request.files['image']

    if file:

        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

        file.save(filepath)

        image = cv2.imread(filepath)

        height, width, channels = image.shape

        result = f"Image Uploaded Successfully. Width: {width}, Height: {height}"

        return result

    return "No Image Uploaded"

if __name__ == '__main__':
    app.run(debug=True)
