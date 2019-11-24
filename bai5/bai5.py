import numpy as np
from matplotlib.pyplot import imread, imsave, imshow, show

n = 8
c = 6 # c*8 pixel

chess = np.zeros( (n,n), dtype='uint8' )
chess[1::2,::2] = 1
chess[::2,1::2] = 1

chrp = np.repeat(chess, c, axis=0)
chrp = np.repeat(chrp, c, axis=1)

chess_bw = np.zeros((chrp.shape[0],chrp.shape[0],3), dtype='uint8')
chess_bw[...,0]=chess_bw[...,1]=chess_bw[...,2]=np.copy(chrp)*254

imsave('chess_blackwhite.png',chess_bw)
