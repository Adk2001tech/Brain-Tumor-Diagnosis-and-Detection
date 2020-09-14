import os
import sys
import random
import math
import numpy as np
import skimage.io
import matplotlib
import matplotlib.pyplot as plt


# Root directory of the project
ROOT_DIR = os.path.abspath("../")
ROOT_DIR

# Import Mask RCNN
sys.path.append(ROOT_DIR)  # To find local version of the library
from mrcnn import utils
from mrcnn.config import Config
import mrcnn.model as modellib
from mrcnn import visualize, visualize_custom

# Directory to save logs and trained model
MODEL_DIR = os.path.join(ROOT_DIR, "logs")


# Local path to trained weights file

TUMOR_MODEL_PATH = os.path.join(ROOT_DIR, "maskrcnn_tumor.h5")
#/content/drive/My Drive/data/data/mask-Rcnn/maskrcnn_tumor.h5
# Directory of images to run detection on
# %mkdir ../images
IMAGE_DIR = os.path.join(ROOT_DIR, "images")


allowed_ext= ['.jpg', '.png']
path= sys.argv[1]
if path[-4:] not in allowed_ext:
	print('file extension allowed:{}, given:[{}]'.format(allowed_ext, path[-4:]))
	exit()



class Model_Config(Config):
    """Configuration for training on the brain tumor dataset.
    """
    # Give the configuration a recognizable name
    NAME = 'Tumor_detector'
    # Train on 1 GPU and 3 images per GPU. We can put multiple images on each
    #GPU_COUNT = 1
    IMAGES_PER_GPU = 1
    # Number of classes (including background)
    NUM_CLASSES = 1 + 1  # background + tumor
    IMAGE_MIN_DIM = 256
    IMAGE_MAX_DIM= 256
    
    # Use smaller anchors because our image and objects are small
    RPN_ANCHOR_SCALES = (8, 16, 32, 64, 128)  # anchor side in pixels
    
    DETECTION_MIN_CONFIDENCE = 0.70
    LEARNING_RATE = 0.001
 
    
config = Model_Config()
#config.display()

# Create model object in inference mode.
model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config)
# Load weights trained on MS-COCO
model.load_weights(TUMOR_MODEL_PATH, by_name=True)


# Load a random image from the `images` folder
image = skimage.io.imread(path)

# Run detection
results = model.detect([image], verbose=1)
class_names= ['-', 'tumor']
# Visualize results
r = results[0]
visualize.display_instances(image, r['rois'], r['masks'], r['class_ids'], 
                           class_names , r['scores'])

