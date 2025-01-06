from flask import Flask, render_template, request
import os
from model import predict_image
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Set up the folder for uploaded images
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Function to check if the file is an allowed image format
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle file upload and prediction
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Get prediction from the model
        label, confidence = predict_image(filepath)
        return render_template('result.html', label=label, confidence=confidence, filepath=filepath)

if __name__ == '__main__':
    app.run(debug=True)
