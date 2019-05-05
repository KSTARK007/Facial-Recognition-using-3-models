# Facial Recognition
### Here we have 3 models 
## 1. First method is using haarCascade Method 
The Haar Cascades for face detection are NOT mine and can be found in [OpenCV's GitHub repository](https://github.com/opencv/opencv/tree/master/data/haarcascades)

This is already trained model 
It is trained on the dataset of top 10000 actors acording to IMDB 
### Requirements
	* mss 				- Screen capture
	* Numpy 			- Matrix calculations
	* CSV				- Data storing and loading
	* CV2				- Image rendering
	* Dlib				- Face recognition
	* requests			- HTTP requests
	* BeautifulSoup 		- Image download
Download mss from [BoboTig's GitHub repository](https://github.com/BoboTiG/python-mss)

### How to use
#### Download the pictures of the first X actors / actresses in IMDB
```python
#Set IMAGES_TO_DONWLOAD in IMDBActors.py:11 to the number of images to be downloaded.
IMAGES_TO_DONWLOAD = 100 #Number of images to download. MUST BE A MULTIPLE OF 50. 
```

```bash
#Run the script to download the images. The images will be donwloaded to a folder with
#the name 'actors' created by the script in the same directory.
$ python IMDBActors.py
```
#### Run FaceDetection.py to detect all the faces on the screen. Only the top corner (0, 0) to (800, 600) is detected.
```bash
#Run the script to identify the actors / actresses. The movies / series where
#they have been together are listed in the terminal.
$ python FaceDetection.py
```

## 2. Face_Recognition
The source code for this face detection core math model is NOT mine and can be found in [Python package ](https://github.com/ageitgey/face_recognition) by [Adam Geitgey](https://github.com/ageitgey)

I am using another repo by [Hardik Vasa](https://github.com/hardikvasa) to collect data from [google images](https://github.com/hardikvasa/google-images-download)

### Requirements
    Python 3.3+ or Python 2.7+

### Installation
##### google_images_download
```python
pip install google_images_download
```
##### face_recognition
```python
pip install face_recognition
```
### How to use
#### run .sh 
```bash
# First time to give it executable permissions run
sudo chmod 777 ./run.sh
# Every use run
./run.sh
```
#### Note: It downloads 50 images of Keanu Reeves from google images and then runs it with the images which are extracted from the trailer of [John wick 3](https://www.youtube.com/watch?v=pU8-7BX9uxs&t=2s) from youtube and shows the results on the terminal 


## 3.CNN using Keras model
