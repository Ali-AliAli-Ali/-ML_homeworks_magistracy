import cv2

pic = cv2.imread('meme.jpg')
pic_hsv = cv2.cvtColor(pic, cv2.COLOR_BGR2HSV)

cv2.imshow('Original (color) picture', pic)
cv2.imshow ('Picture in hsv format', pic_hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()
