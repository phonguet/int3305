import numpy as np
from matplotlib.pyplot import imread, imsave
from scipy.fftpack import rfft, irfft

im_inp = imread('image_inp.png')
aresh = (im_inp.shape[0]*im_inp.shape[1])
scale = 1.0/aresh

ffreq = lambda dt : rfft(rfft(dt, axis=0), axis=1)

im_dr = ffreq(im_inp)
im_freq = (im_dr*scale+1.0)/2.0
imsave('./image_out_freq.png', im_freq)
