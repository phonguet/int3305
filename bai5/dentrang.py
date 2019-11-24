# import numpy as np
# import matplotlib.pyplot as plt

# check = np.zeros((9, 9))
# check[::2, 1::2] = 1
# check[1::2, ::2] = 1

# plt.imshow(check, cmap='gray', interpolation='nearest')
# plt.show()

import cv2
import matplotlib
import numpy as np

height = width = 400
dentrang = np.zeros((height,width,3), np.uint8)

for r in range (0,width):
	for c in range (0,height):
		if((((r//50)%2)+((c//50)%2))%2)==1:
			dentrang[r:r+1,c:c+1] = (255,255,255)
			pass
		else:
			dentrang[r:r+1,c:c+1] = (0,0,0)
			pass
		pass
	pass

cv2.imshow('Ban co den trang', dentrang)
cv2.imwrite("dentrang.jpg",dentrang )

cv2.waitKey(0)
cv2.destroyAllWindows()