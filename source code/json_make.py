import json
import base64
import os
import glob

data = {}

dir = 'C:/Users/USER/Desktop/calib_test_data/9월'
FileList = glob.glob(dir + '/*.jpg')
img_namess = FileList

for idx, d in enumerate(img_namess):
    with open(d, mode='rb') as file:
        img = file.read()

    data['img'] = base64.encodebytes(img).decode("utf-8")
    print(json.dumps(data))