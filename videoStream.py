'''A different program or module to capture the video stream through the WebCam'''
import os
import cv2
import face_recognition as fr
from threading import Thread

# The VideoStream class
class VideoStream:
    def __init__(self, stream):
        self.video = cv2.VideoCapture(stream)
        # Setting the FPS for the video stream
        self.video.set(cv2.CAP_PROP_FPS, 60)

        if self.video.isOpened() is False:
            print("Can't accessing the webcam stream.")
            exit(0)

        self.grabbed , self.frame = self.video.read()

        self.stopped = True
        
        self.thread = Thread(target=self.update)
        self.thread.daemon = True
    
    def start(self):
        self.stopped = False
        self.thread.start()

    def update(self):
        while True :
            if self.stopped is True :
                break
            self.grabbed , self.frame = self.video.read()

        self.video.release()

    def read(self):
        return self.frame

    def stop(self):
        self.stopped = True

def encode_faces():
    encoded_data = {}

    for dirpath, dnames, fnames in os.walk("./Images"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face = fr.load_image_file("Images/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded_data[f.split(".")[0]] = encoding

    # return encoded data of the images
    return encoded_data