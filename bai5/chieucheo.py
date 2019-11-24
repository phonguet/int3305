import cv2
import matplotlib
import numpy as np
import colorsys

height = width = 330
chieucheo = np.zeros((height,width,3), np.uint8)

for r in range (0,height):
	for c in range (0,width):
		a = colorsys.hsv_to_rgb((r+c)/(2*360.0),1,1)
		b = (a[2]*255,a[1]*255,a[0]*255) 
		chieucheo[r:r+1,c:c+1] = b	

cv2.imshow('Dai mau bien doi tuan tu theo chieu cheo', chieucheo)
cv2.imwrite("chieucheo.jpg",chieucheo )

cv2.waitKey(0)
cv2.destroyAllWindows()