 How to Use This Repository

**Step 1:** Clone the Repository

git clone https://github.com/HarshithaSrikakolapu/face-detection.git

cd face-detection


**Step 2:** Install Required Libraries

It’s recommended to use a virtual environment (optional):

pip install -r requirements.txt

If requirements.txt is not available, just install manually:

pip install opencv-python


Make sure the file haarcascade_frontalface_default.xml is present in your project folder.

You can get it from:

**OpenCV GitHub:**

https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

Place this file in the same directory as your facedetection.py file.

**Step 3:** Run the Face Detection Script
Make sure the .xml file is in the same directory as your Python script.

Run the script:

python facedetection.py


**Step 4:** Using the Application
It will open your webcam.
Detected faces will be highlighted with rectangles.

Press q to quit the webcam window.


**Requirements**
 
Python 3.x

OpenCV (opencv-python)

Webcam (for real-time detection)

**About the XML Model**

The file haarcascade_frontalface_default.xml is a pre-trained classifier for frontal face detection. It is provided by OpenCV.


**Made with ❤️ by Harshitha**
