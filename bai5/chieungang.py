import cv2
import matplotlib
import numpy as np
import colorsys


height = width = 330
chieungang = np.zeros((height,width,3), np.uint8)


for c in range (0,width):
	a = colorsys.hsv_to_rgb(c/360.0,1,1)
	b = (a[2]*255,a[1]*255,a[0]*255) 
	for r in range (0,height): 
		chieungang[r:r+1,c:c+1] = b	

cv2.imshow('Dai mau bien doi tuan tu theo chieu ngang', chieungang)
cv2.imwrite("chieungang.jpg",chieungang)

cv2.waitKey(0)
cv2.destroyAllWindows()