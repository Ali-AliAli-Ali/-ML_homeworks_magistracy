import cv2

pic = cv2.imread('meme.jpg')
pic_gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY )

cv2.imshow('Original (color) picture', pic)
cv2.imshow ('Grayscale picture', pic_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
