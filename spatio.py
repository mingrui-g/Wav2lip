import pickle
import cv2
import numpy as np
import math

with open("0.pkl", 'rb') as fo:
        data = pickle.load(fo, encoding='bytes')

upper = int(data[1][0]) ##jaw 

mask = np.zeros((96,96))
## lip area
x_data = data[0][48:60]
y_data = data[1][48:60]
pts = np.vstack((x_data, y_data)).astype(np.int32).T
cv2.fillPoly(mask, [pts], (255), 8, 0)

a = 0
b = 255

origin = (x_data[3], y_data[0])
center = (48.0,48.0)
dis_x, dis_y=0

if origin[0] > center[0]:
    dis_x = origin[0]
else:
    dis_x = center[0]

if origin[1] - upper > 95 - origin[1]:
    dis_y = origin[1] - upper
else:
    dis_y = 95 - origin[1]
dis = math.sqrt(dis_x * dis_x + dis_y * dis_y)

weightB = (b - a) / dis

for x in range(upper, 96):
    for y in range(96):
        dis2 = math.sqrt( math.pow(y-origin[0], 2) + math.pow(x-origin[1], 2))
        mask[x][y] += weightB * (dis - dis2)

cv2.imwrite("test.png", mask)