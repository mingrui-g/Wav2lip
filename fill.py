import pickle
import cv2
import numpy as np
import math

with open("0.pkl", 'rb') as fo:
        data = pickle.load(fo, encoding='bytes')
# x_data = np.array([28.77253,35.825287 ,44.171265 ,48.336693, 52.422325 ,59.86342,  64.89451 ,58.802757, 53.48098 , 47.56613 , 41.656303 ,36.025314])
# y_data = np.array([79.06205,  74.1839 ,  70.95375 , 71.61867 , 71.077065 ,74.45037,  79.840065
#  ,83.7613  , 85.81506  ,86.16196,  85.5865 ,  83.29569 ])

# pts = np.vstack((x_data, y_data)).astype(np.int32).T


x_data = data[0][48:60]
y_data = data[1][48:60]
pts = np.vstack((x_data, y_data)).astype(np.int32).T

# mask = cv2.imread("1.jpg")
# print(data[0, 48:60])
# print(data[1, 48:60])

(51.267994, 73.176834)

mask = np.zeros((96,96))
cv2.fillPoly(mask, [pts], (255), 8, 0)

a = 0
b = 255

origin = (x_data[3], y_data[0])
center = (48.0,48.0)
dis = math.sqrt(96*96) 
# if origin[0] <= center[0] and origin[1] <= center[1]:
#     dis = math.sqrt((95-origin[0])* (95-origin[0]) + (95-origin[1])* (95-origin[1]))
# elif origin[0] <= center[0] and origin[1] > center[1]:
#     dis = math.sqrt((95-origin[0])* (95-origin[0]) + origin[1] * origin[1])
# elif origin[0] > center[0] and origin[1] <= center[1]:
#     dis = math.sqrt(origin[0]* origin[0] + (95-origin[1])* (95-origin[1]))
# elif origin[0] > center[0] and origin[1] > center[1]:
#     dis = math.sqrt(origin[0]* origin[0] + origin[1] * origin[1])



weightB = (b - a) / dis

dis2 = 0
for x in range(96):
    for y in range(96):
        dis2 = math.sqrt( math.pow(x-origin[0], 2) + math.pow(y-origin[1], 2))
        mask[x][y] += weightB * (dis - dis2)

cv2.imwrite("test.png", mask)


# x_data = data[0][48:60]
# y_data = data[1][48:60]
# pts = np.vstack((x_data, y_data)).astype(np.int32).T



# mask = cv2.imread("24.jpg")
# image_size = 96
# #mask = cv2.resize(mask, (image_size, image_size))
# mask = np.zeros((96,96))

# print(x_data.shape)
# print(y_data.shape)
# center = cv2.fillPoly(mask, [pts], (255), 0, 0)
# cv2.imwrite("test.png", mask)








with open("12.pkl", 'rb') as fo:
        data = pickle.load(fo, encoding='bytes')

upper = int(data[1][0]) ##jaw 

mask = np.zeros((96,96))
## lip area
x_data = data[0][48:60]
y_data = data[1][48:60]
pts = np.vstack((x_data, y_data)).astype(np.int32).T
cv2.fillPoly(mask, [pts], (5), 8, 0)

a = 0
b = 255

origin = (x_data[3], y_data[0])
center = (48.0,48.0)
dis_x = 0
dis_y=0

if origin[0] > center[0]:
    dis_x = origin[0]
else:
    dis_x = center[0]

if origin[1] - upper > 95 - origin[1]:
    dis_y = origin[1] - upper
else:
    dis_y = 95 - origin[1]
dis = math.sqrt(dis_x * dis_x + dis_y * dis_y)
dis = 72
weightB = (b - a) / dis

for x in range(upper, 96):
    for y in range(96):
        dis2 = math.sqrt( math.pow(y-origin[0], 2) + math.pow(x-origin[1], 2))
        mask[x][y] += int(weightB * (dis - dis2))


cv2.imwrite("test.png", mask)