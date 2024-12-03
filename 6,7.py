import cv2

pic = cv2.imread('meme.jpg')
pic_flip_h = cv2.flip(pic, 1)  # 6
pic_flip_v = cv2.flip(pic, 0)  # 7

cv2.imshow('Original picture', pic)
cv2.imshow('Picture flipped horizontally', pic_flip_h)
cv2.imshow('Picture flipped vertically', pic_flip_v)

cv2.waitKey(0)
cv2.destroyAllWindows()