import cv2
from tensorflow.keras.models import load_model
import numpy as np
import tensorflow as tf

graph = tf.compat.v1.get_default_graph()

print("Loading model")
classifier = load_model("../static/media/graph-1.classifier")
print("Model loaded")
def predict(img):

    ls = ['sin','tan', 'X=Y', 'X=y^2']
    yo = cv2.imread(img)
    cv2.imshow('d', yo)
    b = cv2.resize(yo, (64, 64))
    per = classifier.predict_proba([[b]])
    he = classifier.predict_classes([[b]])
    hehe = np.round(per * 100, 2)
    print(hehe)
    result = {}

    result['Sin'] = str(hehe[0][0])
    result['Tan'] = str(hehe[0][1])
    result['X=Y'] = str(hehe[0][2])
    result['X=Y^2'] = str(hehe[0][3])
    print(result)
    return result
