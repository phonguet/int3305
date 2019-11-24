import numpy as np
from matplotlib.pyplot import imread, imsave, imshow, show

c = 3
n = 8

chess = np.zeros( (n,n), dtype='int8' )
chess[1::2,::2] = 1
chess[::2,1::2] = 1

chrp = np.repeat(chess, c, axis=0)
chrp = np.repeat(chrp, c, axis=1)

imshow(chrp)
