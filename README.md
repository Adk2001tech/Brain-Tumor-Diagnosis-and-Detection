# Brain-Tumor-Diagnosis-and-Detection🕵

## Abstract:
Brain tumors vary in their position, mass, nature, and consistency of these lesions. Due to the similarities found between brain lesions and normal tissues, many challenges are faced by the researcher in developing algorithms for tumor segmentation. Brain tumor abstraction is thought-provoking job in medical image handing out because brain image and its structure is complicated.

<img align="right" src=https://med.umich.edu/branding/images/our-new-logo.png width="35">

Get **MOTIVATED** from **Michigan Medicine's** <a href="https://youtu.be/UZZ08_fC7UU">YouTube</a> Video. 

<img src="Images/bt2.jpg" width="700" title="Tumor detection">

Optical imaging and artificial intelligence are making brain tumor diagnosis quicker and more accurate.

This Project aim for providing the **Baseline TUMOR detection and classification models using MASK-RCNN(detection) and DEEP LEAARNING CLASSIFICATION TECHNIQUES**.

<table>
  <tr>
    <td><strong>TUMOR CLASSIFICATION</strong></td>
     <td><strong>TUMOR DETECTION</strong></td>
  </tr>
  <tr>
    <td><img src="Images/brain.png" width="400" title="Input image"></td>
    <td><p align="center">
  <img src="Images/out1.png" width="200" title="Input image">
  <img src="Images/out2.png" width="200" title="Mask-Rcnn output image">
</p></td>
  </tr>
 </table>

<hr>

## Part I:
### **Image Data Analysis and Classification**

The main purpose of this project(part i) is to Analysis Image Data and ultimately to build a **CNN model** that would classify if subject has a tumor or not baised on MRI scan. I used the **VGG-16** model architecture and weights to train the model for this binary problem. I used `accuracy` as a metric to justify the model.

**Visit NOTEBOOK for PROJECT PART(I)** 

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

Tumor Detection
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

<img align="right" width="400" src="Images/clf_model.jpg" width="400" title="Classification Model">

#### Classify on You own image📷:

* Download **Python Script** and **Model weights**.
* Make sure they are loaded in same directory.
* Run .py Scripts as below:
     
     `python tumor_classify_vgg16.py  relative_path/img.jpg`
     
     
     
     
## Part II:
