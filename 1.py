import numpy as np
import cv2


input_pic = cv2.imread('meme_distorted.jpg')
train_pic = cv2.imread('meme.jpg')
 
input_pic_gray = cv2.cvtColor(input_pic, cv2.COLOR_BGR2GRAY)
train_pic_gray = cv2.cvtColor(train_pic, cv2.COLOR_BGR2GRAY)
 
orb = cv2.ORB_create()
input_keypts, input_descrs = orb.detectAndCompute(input_pic_gray, None)
train_keypts, train_descrs = orb.detectAndCompute(train_pic_gray, None)

matcher = cv2.BFMatcher()
matches = matcher.match(input_descrs,train_descrs)
 
final_pic = cv2.drawMatches(input_pic, input_keypts, train_pic, train_keypts, matches[:20], None)
final_pic = cv2.resize(final_pic, (0,0), fx=0.7, fy=0.7, interpolation=cv2.INTER_NEAREST)

cv2.imshow('Matches', final_pic)

cv2.waitKey(0)
cv2.destroyAllWindows()
