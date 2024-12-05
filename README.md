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

-Real-Time Detection:
It captures frames from the webcam feed using OpenCV and detects faces in real-time.

-Face Matching:
The detected faces are matched against the encoded faces to identify individuals.

-Attendance Logging:
Once a face is recognized, the name is logged into a attendance.csv file with the current date and time.
