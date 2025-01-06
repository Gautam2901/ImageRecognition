import tensorflow as tf
import numpy as np

# Load the pre-trained model
model = tf.keras.models.load_model('MobileNetV2.keras')

# Function to predict the image
def predict_image(image_path):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)

    predictions = model.predict(img_array)
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)
    return decoded_predictions[0][0][1], decoded_predictions[0][0][2]  # Return class name and confidence
