import tensorflow as tf
import os

# Download and save MobileNetV2 model
model = tf.keras.applications.MobileNetV2(weights='imagenet')
model.save('MobileNetV2.keras')

print("Model downloaded and saved successfully.")
