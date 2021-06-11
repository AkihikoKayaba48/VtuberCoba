import socket
import mediapipe as mp
import cv2
import json
import numpy

from head_pose_estimation.mark_detector import MarkDetector
from head_pose_estimation.pose_estimator import PoseEstimator
from head_pose_estimation.stabilizer import Stabilizer
from head_pose_estimation.visualization import *
from head_pose_estimation.misc import *

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic


#koneksi
HEADERSIZE = 10
#address = ('127.0.0.1', 5066)
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect(address)
#clientsocket = s.accept()
#print(f"Connection from {address} has ben estabilished!")


cap = cv2.VideoCapture(0)
with mp_holistic.Holistic(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as holistic:

    while cap.isOpened():
        ret, frame = cap.read()

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = holistic.process(image)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACE_CONNECTIONS)
        mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        #mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

        cv2.imshow('Test Webcam', image)

        pose=''
        
        try:
            pose = results.pose_landmarks.landmark
        except:
            pose = ''

        pose_serialize=[]
        
        print(msg)
        #pose = (results.right_hand_landmarks.landmark)
        
        #pose_serialize=[]
        #if isinstance(pose, str):
        #    msg = json.dumps('nada')
        #else:
        #    for i in range(len(pose)):
        #        x=pose[i].x
        #        y=pose[i].y
        #        z=pose[i].z
        #        pose_serialize.append([i,x,y,z])
        #print(pose_serialize)
        #msg = json.dumps(pose_serialize)
        #print('len: ',len(msg))
        #print('len encode: ',len(msg.encode('utf-8')))

        #msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg.encode('utf-8')
        
        #s.send(bytes(msg))
        
        #print(msg)
        #pose=results.pose_landmarks.landmark

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()