import numpy as np
import math
import matplotlib.pyplot as plt

arrs = np.arange(0,10,0.01)
A = 5

fff_sin = lambda k:A*np.sin(arrs)
fsq_sin = lambda k:A*(1.0/(2*k+1))*np.sin(2*math.pi*(2*k+1)*arrs)
fsm_sin = lambda k:A*(1.0/(k))*np.sin(2*math.pi*(k)*arrs)

s=np.zeros(len(arrs))
for i in range(1,100):
	s+=fsm_sin(i)

plt.plot(arrs, s)
# plt.plot(arrs, fsm_sin(1))
# plt.show()
plt.savefig('home.png')

# print(fsin(5,6))