import numpy as np
from matplotlib.pyplot import imread, imsave
from scipy.fftpack import rfft, irfft

im_inp = imread('image_out_freq.png')
aresh = (im_inp.shape[0]*im_inp.shape[1])
scale = 1.0/aresh

forig = lambda dt : irfft(irfft(dt, axis=1), axis=0)

im_orig = forig((im_inp*2.0-1.0)*aresh)
im_orig = np.where(im_orig>1.0, 1.0, im_orig)
im_orig = np.where(im_orig<0.0, 0.0, im_orig)
imsave('./image_out_orig.png', im_orig)
