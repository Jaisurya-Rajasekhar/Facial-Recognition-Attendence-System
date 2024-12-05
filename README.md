#Facial Recognition-Based Attendance System
This project is a Python-based application that uses dlib and OpenCV to automate the attendance marking process. It recognizes faces in real-time from a webcam feed, matches them with a pre-existing database, and logs attendance with a timestamp into a CSV file.

-Features
Real-time facial recognition using dlib.
Image processing and video frame handling with OpenCV.
Logging of recognized faces with timestamps in a CSV file.
Draws bounding boxes and names of recognized faces on the webcam feed.
Efficient handling of multiple faces in a single frame.

-Technologies Used
Programming Language: Python
Libraries:
dlib: For facial recognition and landmark detection.
OpenCV: For image processing and video handling.
CSV Module: For logging attendance.

-Setup Instructions
1. Clone the Repository
bash
Copy code
git clone https://github.com/your-username/Facial-Recognition-Attendance-System.git
cd Facial-Recognition-Attendance-System
2. Install Dependencies
Ensure Python is installed, then install the required libraries:

bash
Copy code
pip install opencv-python dlib
3. Prepare the Face Dataset
Save images of known individuals in a folder (e.g., known_faces/).
Name the images as Name.jpg or Name.png.
4. Run the Application
bash
Copy code
python main.py
How It Works
Encoding Known Faces:
The application preprocesses and encodes the faces from the known_faces/ folder using dlib's facial recognition model.

Real-Time Detection:
It captures frames from the webcam feed using OpenCV and detects faces in real-time.

Face Matching:
The detected faces are matched against the encoded faces to identify individuals.

Attendance Logging:
Once a face is recognized, the name is logged into a attendance.csv file with the current date and time.
