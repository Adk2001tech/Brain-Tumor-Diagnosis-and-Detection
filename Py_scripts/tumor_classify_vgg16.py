import numpy as np
import pandas as pd
import sys

import matplotlib.pyplot as plt
import cv2

import tensorflow
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras import layers, Input
from tensorflow.keras.models import Model


def build_model():
    vgg= VGG16(input_shape=(224, 224, 3), include_top=False, weights='imagenet')
    vgg.layers
    for layer in vgg.layers:
        layer.trainable= False
    x= layers.Flatten()(vgg.output)
    x= layers.Dropout(0.25)(x)
    x= layers.Dense(1024, activation='relu')(x)
    x= layers.Dropout(0.15)(x)
    out= layers.Dense(1, activation='sigmoid')(x)
    
    return Model(inputs= vgg.input, outputs=out)

#READ IMAGE
allowed_ext= ['.jpg', '.png']
path= sys.argv[1]
if path[-4:] not in allowed_ext:
	print('file extension allowed:{}, given:[{}]'.format(allowed_ext, path[-4:]))
	exit()

gray=False

def load_img(path, resize=None):
    img= cv2.imread(path, 0)
    if resize:
        img= cv2.resize(img, resize)    
    return img

try:
	img= cv2.imread(path)
	img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	img= cv2.resize(img, (224, 224))/255.0
except:
	gray= True
	img= load_img(path, resize=(224, 224))
	img= cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)/255.0





model= build_model()
model.load_weights('tumor_diagnosis.h5')

if gray:
	plt.imshow(img, 'gray')
else:
	plt.imshow(img)

plt.show()


grd_truth= {0:'Healthy Brain', 1:'Brain having Tumor'}
pred= int(model.predict(np.expand_dims(img, 0))>0.5)

print(grd_truth[pred])


