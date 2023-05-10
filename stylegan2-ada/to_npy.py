import os
import numpy as np
import cv2

def to_npy(path='C://Users/user/Desktop/code/adagan/data/faces'):
    listImages = os.listdir(path)
    x = np.ndarray(shape=(len(listImages),96,96,3), dtype=np.float32)
    for i in range(len(listImages)):     
        img = cv2.imread(path+listImages[i])
        x[i] = img
        print(path+listImages[i])
    np.save('dataset.npy', x)
    print('file has saved')
    
if __name__ == '__main__':
    to_npy()