import cv2
import numpy as np

pic = cv2.imread('meme.jpg')

cv2.imshow('Original picture', pic)
threshold, pic_bin = cv2.threshold(pic, 128, 255, cv2.THRESH_BINARY)

cv2.imshow(f'Binarized picture with threshold %'.format(threshold), pic_bin)

cv2.waitKey(0)
cv2.destroyAllWindows()