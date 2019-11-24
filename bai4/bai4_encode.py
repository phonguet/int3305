import numpy as np
from matplotlib.pyplot import imread, imsave
from scipy.fftpack import rfft, irfft

im_inp = imread('image_inp.png')
aresh = (im_inp.shape[0]*im_inp.shape[1])
scale = 1.0/aresh

im_dr = ffreq(im_inp)
im_freq = (im_dr*scale+1.0)/2.0
imsave('./image_out_freq.png', im_freq)

# ffreq = lambda dt : rfft(rfft(dt, axis=0), axis=1)
#
# from scipy.fftpack import fft2, ifft2
# im_gray1d = np.average(im_inp[..., :3], axis=2)
# im_gray4c = np.copy(im_inp)
# im_gray4c[..., 0]=im_gray4c[..., 1]=im_gray4c[..., 2]=im_gray1d
# imsave('./image_out_freqg.png', im_gray4c)
#
# im_out1d = fft2(im_gray1d).view(np.float64)
# im_out1d = (im_out1d*scale)
# im_out4c = np.copy(im_inp)
# im_out4c[..., 0]=im_out4c[..., 1]=im_out4c[..., 2]=im_out1d
# imsave('./image_out_freqz.png', im_out4c)
#
# im_inp = imread('image_out_freqz.png')
# im_inp1d = np.average(im_inp[..., :3], axis=2)
# im_orig = ifft2((im_inp1d)*aresh).view(np.float64)
# im_orig = np.where(im_orig>1.0, 1.0, im_orig)
# im_orig = np.where(im_orig<0.0, 0.0, im_orig)
# imsave('./image_out_orig.png', im_orig)

