# Brain-Tumor-Diagnosis-and-Detection🕵

## Abstract:
Brain tumors vary in their position, mass, nature, and consistency of these lesions. Due to the similarities found between brain lesions and normal tissues, many challenges are faced by the researcher in developing algorithms for tumor segmentation. Brain tumor abstraction is thought-provoking job in medical image handing out because brain image and its structure is complicated.

<img align="right" src=https://med.umich.edu/branding/images/our-new-logo.png width="35">

Get **MOTIVATED** from **Michigan Medicine's** <a href="https://youtu.be/UZZ08_fC7UU">YouTube</a> Video. 

<img src="Images/bt2.jpg" width="700" title="Tumor detection">

Optical imaging and artificial intelligence are making brain tumor diagnosis quicker and more accurate.

[This Project aim for providing the **Baseline TUMOR detection and classification models using MASK-RCNN(detection) and DEEP LEARNING CLASSIFICATION TECHNIQUES**.](#)

<table>
  <tr>
    <td><strong>TUMOR CLASSIFICATION (Part I)</strong></td>
     <td><strong>TUMOR DETECTION (Part II)</strong></td>
  </tr>
  <tr>
    <td><img src="Images/brain.png" width="300" title="Input image"></td>
    <td><p align="center">
  <img src="Images/out1.png" width="180" title="Input image">
  <img src="Images/out2.png" width="200" title="Mask-Rcnn output image">
</p></td>
  </tr>
 </table>

<hr>

## Part I:
### **Image Data Analysis and Classification**

The main purpose of this project(part i) is to Analysis Image Data and ultimately to build a **CNN model** that would classify if subject has a tumor or not baised on MRI scan. I used the **VGG-16** model architecture and weights to train the model for this binary problem. I used `accuracy` as a metric to justify the model.

**Visit <a href="https://github.com/Adk2001tech/Brain-Tumor-Diagnosis-and-Detection/blob/master/Notebooks/brain-tumor-detection_vgg-16.ipynb">NOTEBOOK</a> for PROJECT PART(I)** 

**Table of Contents** :
* <p style="color: blue">Image Data Loading...</p>
* <p style="color: blue">Visualizing with Colormaps</p>

<p align="center">
  <img src="Images/part11.png" width="400" title="Image Data">
  <img src="Images/part12.png" width="400" title="Visualizing with Colormaps">
</p>
<br>

* <p style="color: blue">Equalized Hist Technique and K-Means clustring</p>
* <p style="color: blue">Edge detection</p>
* <p style="color: blue">Model traning (VGG-16)</p>

<p align="center">
  <img src="Images/part13.png" width="400" title="Equalized Hist Technique and K-Means clustring">
  <img src="Images/part15.png" width="400" title="Model traning (VGG-16)">
</p>
<br>

* <p style="color: blue">Tesing model performance</p>
* <p style="color: blue">Model Evaluation</p>

<p align="center">
  <img src="Images/part16.png" width="900" title="Tesing model performance">
</p>


<img align="right" width="400" src="Images/clf_model.jpg" width="400" title="Classification Model">


Tumor Detection on Test data:
<table border="0">
 <tr>
    <td><b style="font-size:30px"> Accuracy</b></td>
    <td><b style="font-size:30px">Precision</b></td>
   <td><b style="font-size:30px">F1-Score</b></td>
 </tr>
 <tr>
    <td>90%</td>
    <td>86%</td>
   <td>92%</td>
 </tr>
</table>
<br>



#### Classify on You own image📷:

* Download **<a href="https://github.com/Adk2001tech/Brain-Tumor-Diagnosis-and-Detection/blob/master/Py_scripts/tumor_classify_vgg16.py">Python Script</a>** and **<a href="https://drive.google.com/file/d/1RHpLvg3m6BWoJcD90d26dfT4lOjE-15v/view?usp=sharing">Model weights</a>**.
* Make sure they are loaded in same directory.
* Run .py Script as below:
     
     `python tumor_classify_vgg16.py  relative_path/img.jpg`
     
<hr>
     
     
## Part II:

<img align="right" src="Images/detect_model.png" width="480" title="Mask-RCNN Model">

### Brain Tumor Detection
Project(part ii) aims to build an actual DETECTOR(DL Model) which will point out on the location of the tumor on the scan along it's MASK using **Mask R-CNN**.

Special thanks to <a href="https://github.com/matterport/Mask_RCNN">Mask-Rnn-GitHub</a>.
* This is an implementation of Mask R-CNN on Python 3, Keras, and TensorFlow. The model generates bounding boxes and segmentation masks for each instance of an object in the image. It's based on **Feature Pyramid Network (FPN) and a ResNet101 backbone**. 
* Requirements   

        tensorflow=== 1.15.0
        keras== 2.0.8
        pycocotools
        
**Visit <a href="https://github.com/Adk2001tech/Brain-Tumor-Diagnosis-and-Detection/blob/master/Notebooks/brain-tumor-detection-final-mask-r-cnn.ipynb">NOTEBOOK</a> for PROJECT PART(II)** 
**Table of Contents**
* <p style="color: blue">Setting up development environment</p>

      1. Clone GitHub <a href="https://github.com/matterport/Mask_RCNN">Repository</a>
      2. Change your directory to `/MASK_RCNN`
      3. ROOT_DIR = os.path.abspath('')
         # Add to System path
         sys.path.append(ROOT_DIR)
      4. Add `logs` folder to keep track of logs and trained models
     Take a deep dive in **model traing** with  <a href="https://github.com/matterport/Mask_RCNN/blob/master/samples/shapes/train_shapes.ipynb">Notebook1_custom</a> and <a href="https://github.com/Adk2001tech/Brain-Tumor-Diagnosis-and-Detection/blob/master/Notebooks/brain-tumor-detection-final-mask-r-cnn.ipynb">Notebook2_tumor</a>
* <p style="color: blue">Setting up Model Configuration and Data Generators</p>


<img src="Images/out25.png" width="400" title="Image Data">
<img src="Images/out23.png" width="400" title="Visualizing with Colormaps">


* <p style="color: blue">Model traning</p>
* <p style="color: blue">Tesing model performance</p>

<table align="right">
  <tr>
    <td><strong>INPUT IMAGE</strong></td>
     <td><strong>OUTPUT IMAGE</strong></td>
  </tr>
  <tr>
    <td><img src="Images/inp3.png" width="180" title="Input image"></td>
    <td><p align="center">
  <img src="Images/inp33.png" width="180" title="Mask-Rcnn output image">
</p></td>
  </tr>
 </table>


<table>
  <tr>
    <td><strong>INPUT IMAGE</strong></td>
     <td><strong>OUTPUT IMAGE</strong></td>
  </tr>
  <tr>
    <td><img src="Images/inp1.png" width="180" title="Input image"></td>
    <td><p align="center">
  <img src="Images/inp11.png" width="180" title="Mask-Rcnn output image">
</p></td>
  </tr>
 </table>
 
 <table align="right">
  <tr>
    <td><img src="Images/inp2.png" width="180" title="Input image"></td>
    <td><p align="center">
  <img src="Images/inp22.png" width="180" title="Mask-Rcnn output image">
</p></td>
  </tr>
 </table>


<table>

  <tr>
    <td><img src="Images/inp4.png" width="180" title="Input image"></td>
    <td><p align="center">
  <img src="Images/inp44.png" width="180" title="Mask-Rcnn output image">
</p></td>
  </tr>
 </table
 <br>
 
* <p style="color: blue">Evaluation</p>



#### TUMOR Detection on You own image📷:

* Clone GitHub <a href="https://github.com/matterport/Mask_RCNN">Repository</a>
* Change your directory to `/MASK_RCNN`
* Download Tumor detection model weights from <a href="https://drive.google.com/file/d/1JsvMGdP4OGano3fn4939HLQHqhQkRPCz/view?usp=sharing">here</a>.
* Create `logs` folder, and load/paste `mask_rcnn_tumor.h5` file.
* Run .py <a href="https://github.com/Adk2001tech/Brain-Tumor-Diagnosis-and-Detection/blob/master/Py_scripts/tumor_detect_rcnn.py">Script</a> as below:
  
     `python tumor_detect_rcnn.py  relative_path/img.jpg`
     
     
