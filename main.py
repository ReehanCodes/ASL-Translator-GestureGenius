#Declaring dependencies 
import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import time
import mediapipe as mp


mp_holistic = mp.solutions.holistic     #holistics model (make detection)
mp_drawing = mp.solutions.drawing_utils #drawing utilities (draw detection)


def mediapipe_detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #converting color channel bgr 2 rgb (mediapipe only uses rgb but opencv captures bgr)
    image.flags.writeable = False                  #image is not writable
    results = model.process(image)                 #use mediapipe to detect frame from opencv
    image.flags.writeable = True                    #make image writable again
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) #converting color channel rgb 2 bgr (so opencv can use)
    return image, results

def draw_landmarks (image, results):
    mp_drawing.draw_landmarks(image, results.face_landmarks, mp.solutions.holistic.FACEMESH_CONTOURS)       #Draw face connections
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS)       #Draw pose connections
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)  #Draw hand connections
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS) #Draw hand connections










cap = cv2.VideoCapture(0)

#Access mediapipe model
with mp_holistic.Holistic(min_detection_confidence= 0.5, min_tracking_confidence= 0.5) as holistic:    #initial detection tracking
    while cap.isOpened():   
        ret, frame = cap.read()     #Read feed frames


        #Make detections
        image, results = mediapipe_detection(frame, holistic)

        pose = np.array([[res.x,res.y,res.z,res.visbility,] for res in results.pose_landmarks.landmark]).flatten()
        print(len(pose))
        face = np.array([[res.x,res.y,res.z] for res in results.pose_landmarks.landmark]).flatten()
        print(len(face))
        lh = np.array([[res.x,res.y,res.z] for res in results.pose_landmarks.landmark]).flatten()
        print(len(lh))
        rh = np.array([[res.x,res.y,res.z,] for res in results.pose_landmarks.landmark]).flatten()
        print(len(rh))





        draw_landmarks(image, results)


        cv2.imshow('Hey', image)    #Display to screen
        #Break
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()           #Release webcam
    


    cv2.destroyAllWindows() #Break window
    


