import cv2
import numpy as np

#Reading the image
image = cv2.imread("blob.jpg",cv2.IMREAD_COLOR)

#Set up the detector. SimpleBlobDetector_create() is the new version, 
#SimpleBlobDetector is deprecated.
detector = cv2.SimpleBlobDetector_create()

#initialize detector with the image
keypoints = detector.detect(image)

#Draw detected blobs as green circles
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
image_with_keypoints = cv2.drawKeypoints(image,keypoints,np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

# Show keypoints
cv2.imshow("Keypoints", image_with_keypoints)
cv2.imwrite("image_with_keypoints.jpg", image_with_keypoints)
cv2.waitKey(0)