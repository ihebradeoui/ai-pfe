import asyncio
import base64
from cgi import test
from datetime import datetime, timedelta
import io
import os
import PIL.Image as Image
from cv2 import IMREAD_ANYCOLOR, IMREAD_UNCHANGED
import requests
import cv2
import numpy as np 
import itertools
import keras
from FaceDetector import FaceDetector

from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img 
from keras.models import Sequential 
from keras import optimizers
from keras.preprocessing import image
from keras.layers import Dropout, Flatten, Dense 
from keras import applications 
from keras.utils.np_utils import to_categorical 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import math 
from datetime import datetime
from time import time , ctime
from FacesManager import FirebaseConector

from Models.Suspect import Suspect
suspects=[]
def images():
    r =requests.get('https://localhost:5001/api/Police/photos/00221221',verify=False)
    res=r.json()
    a=1
    for i in res:
        b=base64.b64decode(i)
        image = Image.open(io.BytesIO(b))
        image.save('dataset/user'+str(a)+'.jpg')
        a+=1
def sus():
    suspectsReq =requests.get('https://localhost:5001/api/Police/suspects',verify=False)
    suspectsJson=suspectsReq.json()
    for jsonSus in suspectsJson:
        suspects.append(
            Suspect(
                jsonSus['id'],
                jsonSus['name'],
                jsonSus['location'],
                jsonSus['image']    
            )
        )
def moveNegativeFaces():
    i=1
    dec=FaceDetector()
    for directory in os.listdir('lfw'):
        for file in os.listdir(os.path.join('lfw',directory)):
           
            
            rawImg=cv2.imread(os.path.join(os.path.join('lfw',directory,file)))
            img, bboxs = dec.findFaces(rawImg,False)
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            
            

                        
            (x,y,w,h) = bboxs[0][1]
            cv2.imwrite("dataset/User." + "unknown" + '.' + str(i) + ".jpg", gray[y:y+h,x:x+w])
            i+=1  
            if i == 160:
                break      

a = FirebaseConector()
a.connect()
asyncio.run(a.set_in_firebase('iheb'))
