import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # or any {'0', '1', '2'}
from numpy import asarray
from random import shuffle
from math import floor
import numpy as np
from numpy import savez_compressed
from keras.preprocessing import image
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
import glob
from PIL import Image
from numpy import asarray

# from PIL import Image
# import image

images = []
data = []
def formatData():
    folders = []

    imageFolder = 'C:/Users/calvi/Desktop/smART_data/dataset/training_set/*'
    for name in glob.glob(imageFolder):
        print("name", name)
        folders.append(f"{name}")

    print("folders", folders)

    for a in range(len(folders)):
        for b in (os.listdir(folders[a])):
            images.append(b)
    print(len(images))

    # get image path, assign to list
    numFiles0 = len(os.listdir(folders[0]))
    numFiles1 = len(os.listdir(folders[1]))
    numFiles2 = len(os.listdir(folders[2]))
    numFiles3 = len(os.listdir(folders[3]))
    for i in range(len(images)):
        if i >= (numFiles0 + numFiles1 + numFiles2 + numFiles3):
            data.append(
                f'C:/Users/calvi/Desktop/smART_data/dataset/training_set/sculpture/{images[i]}')
        elif i >= (numFiles0 + numFiles1 + numFiles2):
            data.append(
                f'C:/Users/calvi/Desktop/smART_data/dataset/training_set/painting/{images[i]}')
        elif i >= (numFiles0 + numFiles1):
            data.append(
                f'C:/Users/calvi/Desktop/smART_data/dataset/training_set/iconography/{images[i]}')
        elif i >= numFiles0:
            data.append(
                f'C:/Users/calvi/Desktop/smART_data/dataset/training_set/engraving/{images[i]}')
        else:
            data.append(
                f'C:/Users/calvi/Desktop/smART_data/dataset/training_set/drawings/{images[i]}')

formatData()
print(len(data))

npImgs = []
for i in range(len(data)):
    image = Image.open(data[i])
    # convert image to numpy array
    img = asarray(image)
    npImgs.append(img)

print("before len(npImgs)",len(npImgs))



print("after len(npImgs)",len(npImgs))
#
