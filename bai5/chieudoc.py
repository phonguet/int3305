import cv2
import matplotlib
import numpy as np
import colorsys

height = width = 400
chieudoc = np.zeros((height,width,3), np.uint8)

for r in range (0,height):
	a = colorsys.hsv_to_rgb(r/360.0,1,1)
	b = (a[2]*255,a[1]*255,a[0]*255) 
	for c in range (0,width): 
		chieudoc[r:r+1,c:c+1] = b	

cv2.imshow('Dai mau bien doi tuan tu theo chieu doc', chieudoc)
cv2.imwrite("chieudoc.jpg",chieudoc )

cv2.waitKey(0)
cv2.destroyAllWindows()