import cv2
import numpy as np

#Reading the image
image = cv2.imread("blob.jpg",cv2.IMREAD_COLOR)


#Create SimpleBlobDetector_Params.
parameters = cv2.SimpleBlobDetector_Params()

#Thresholds
parameters.minThreshold=10
parameters.thresholdStep=200
# parameters.maxThreshold=75

#Minimum Distance between Blobs
# parameters.minDistBetweenBlobs = 250

#Define different parameters
#Color Filters
parameters.filterByColor= True
parameters.blobColor= 0

#Area filters
parameters.filterByArea = True
parameters.minArea=900
parameters.maxArea=7800

#Circularity filter
parameters.filterByCircularity = True
parameters.minCircularity = 0.25
parameters.maxCircularity = 0.985

#Convexity filter
parameters.filterByConvexity= True
parameters.minConvexity = 0.185
parameters.maxConvexity = 0.995

#Inertia filter
parameters.filterByInertia = True
parameters.minInertiaRatio = 0.01
parameters.maxInertiaRatio = 1

#Set up the detector. SimpleBlobDetector_create() is the new version, 
#SimpleBlobDetector is for OpenCV < ver 3.x
detector = cv2.SimpleBlobDetector_create(parameters)

#initialize detector with the image
keypoints = detector.detect(image)

#Draw detected blobs as red circles
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
image_with_keypoints = cv2.drawKeypoints(image,keypoints,np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show keypoints
cv2.imshow("Keypoints", image_with_keypoints)
cv2.waitKey(0)