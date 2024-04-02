#import library
import pandas as pd
import numpy as np
import streamlit as st
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import matplotlib.pyplot as plt
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model

#import pickle
import pickle

#load model
def run():
    file = st.file_uploader("Upload an image", type=["jpg", "png"])

    model = tf.keras.models.load_model('model_ann_sequential_improve.h5')
    target_size=(50, 50)

    def import_and_predict(image_data, model):
        image = tf.keras.utils.load_img(image_data, target_size=(50, 50))
        x = tf.keras.utils.img_to_array(image)
        x = np.expand_dims(x, axis=0)

        plt.imshow(image)
        plt.axis('off')
        plt.show()

        # Make prediction
        classes = model.predict(x)
        result_pred = np.argmax(classes, axis=1)
        labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
                  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
                  'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
                  'U', 'V', 'W', 'X', 'Y', 'Z', '_']

        predicted_class = labels[result_pred[0]]  # Get the predicted class
        return f"Prediction: {predicted_class}"

    if file is None:
        st.text("Please upload an image file")
    else:
        prediction = import_and_predict(file, model)
        st.image(file)
        st.write(prediction, font="Arial",  size=50)  # Increase text size
        
if __name__ == "__main__":
    run()
