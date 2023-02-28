from utils.utils import *
import os
import tensorflow as tf
import numpy as np

DIR_LOC = os.getcwd()


def load_model():
    model_path = os.path.join(DIR_LOC, 'src', 'pred', 'models','model_twibbon.h5')
    model = tf.keras.models.load_model(model_path)
    return model

def tf_predict(img):
    class_label = ['Tanpa Twibbon', "Twibbon Find IT!"]
    model = load_model()
    result = model.predict(img)
    predicted_class = int(np.round(result.flatten()[0]))
    probability = result.flatten()[0]
    if predicted_class == 0:
        probability = 1-probability
    predicted_class_name = class_label[int(predicted_class)]

    return {"predicted_label": predicted_class_name,
            "probability": str(probability)}