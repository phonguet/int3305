import numpy as np
import math
import matplotlib.pyplot as plt

f=2
fs=100
N=6
A = 4
n=20

t = np.arange(0,N/f,1.0/fs)

s1_t = lambda t : A*np.sin(2*math.pi*f*t)

s2_t = lambda t, i : (1.0*A/(2*i+1)**2)*np.sin(2*math.pi*(2*i+1)*f*t)
s2=np.zeros(len(t))
for i in range(2*n+2):
	s2 += s2_t(t, i)

plt.plot(t, s1_t(t))
plt.savefig('./s1_t.png')
plt.clf()

plt.plot(t, s2)
plt.savefig('./s2_t.png')
