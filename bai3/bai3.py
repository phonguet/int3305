import numpy as np
from matplotlib.pyplot import imread, imsave, get_cmap

im_inp = imread('./image_inp.png')

# Convert To Gray Scale
im_gray = np.dot(im_inp[..., :3], [0.2989, 0.5870, 0.1140])
imsave('./image_out_gray.png', im_gray, cmap=get_cmap('gray'))

# Convert to R, G, B, A
image_r = np.copy(im_inp)
image_r[...,1]=image_r[...,2]=image_r[...,0]
imsave('./image_out_r.png', image_r)

image_g = np.copy(im_inp)
image_g[...,2]=image_g[...,0]=image_g[...,1]
imsave('./image_out_g.png', image_g)

image_b = np.copy(im_inp)
image_b[...,0]=image_b[...,1]=image_b[...,2]
imsave('./image_out_b.png', image_b)

image_a = im_inp[:, :, 3]
image_a[...,0]=image_a[...,1]=image_a[...,2]=image_a[...,3]
imsave('./image_out_a.png', image_a)

# Merge Image
imr_r = imread('./image_out_r.png')[:,:,0]
imr_g = imread('./image_out_g.png')[:,:,1]
imr_b = imread('./image_out_b.png')[:,:,2]
imr_a = imread('./image_out_a.png')[:,:,3]

im_out = np.zeros((imr_a.shape[0], imr_a.shape[1], 4), 'float32')
im_out[..., 0] = imr_r
im_out[..., 1] = imr_g
im_out[..., 2] = imr_b
im_out[..., 3] = imr_a
imsave('./image_out_rgba.png', im_out)
