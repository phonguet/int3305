import numpy as np
from scipy.signal import convolve, fftconvolve

def cyclic_convolution(x, h):
    L = len(x)
    N = len(h)
    if L > N:
        t = x
        x = h
        h = t
        t = N
        N = L
        L = t

    S0 = np.concatenate((x[::-1], np.zeros(N-L, dtype=h.dtype.name)))
    sy = np.array([np.roll(S0, -L+1+i) for i in range(N)])
    return sy.dot(h)


def linear_convolution(x, h):
    L = len(x)
    N = len(h)
    M = L + N - 1
    if L > N:
        t = x
        x = h
        h = t
        t = N
        N = L
        L = t

    S0 = np.concatenate((x[::-1], np.zeros(N - 1, dtype=h.dtype.name)))
    sy = np.array([np.roll(S0, i)[L - 1:] for i in range(M)])
    return sy.dot(h)

print('Nhap cac phan tu cua mang x:')
x = np.array([int(it) for it in input().split(' ')])
print('Nhap cac phan tu cua mang h:')
h = np.array([int(it) for it in input().split(' ')])
L = len(x)
N = len(h)

"""
TEST DATA
"""
# x = np.array([1, 0, 1])
# h = np.array([1, 0, 0, 1, 8, 2])

y1 = linear_convolution(x, h)
print('a. Linear convolution:', y1, sep='\n')
y1_c = convolve(x, h)
print('a. Linear convolution (ham san co) :', y1_c, sep='\n')

y2 = cyclic_convolution(x, h)
print('b. Cyclic convolution:', y1, sep='\n')

xp = np.append(x, np.zeros(N-1, dtype=x.dtype.name))
hp = np.append(h, np.zeros(L-1, dtype=h.dtype.name))
y3 = cyclic_convolution(xp, hp)
print('b. Linear convolution by Cyclic convolution:', y1, sep='\n')
