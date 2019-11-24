import numpy as np
from matplotlib.pyplot import imread, imsave, imshow, show

n = 8
c = 6 # c*8 pixel
#ff0000, #800080

chess = np.zeros( (n,n), dtype='uint8' )
chess[1::2,::2] = 254
chess[::2,1::2] = 254

chrp = np.repeat(chess, c, axis=0)
chrp = np.repeat(chrp, c, axis=1)

chess_bw = np.zeros((chrp.shape[0],chrp.shape[0],3), dtype='uint8')
chess_bw[...,0]=chess_bw[...,1]=chess_bw[...,2]=np.copy(chrp)

imsave('chess_blackwhite.png',chess_bw)

#
next_x = 16711680  # We start the search at x=6
max_iters = 8388736  # Maximum number of iterations
gamma = np.abs(max_iters-next_x)//(c*n)  # Step size multiplier
precision = 0.00001  # Desired precision of result

genfx=[]
def df(x):
    return 4 * x**3 - 9 * x**2
for _i in range(next_x, max_iters+1, gamma):
    current_x = next_x
    next_x = current_x - gamma * df(current_x)
    step = next_x - current_x
    genfx.append(next_x)
print(next_x)