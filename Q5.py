'''
Q5.
Gaurav Kanu
1811067
'''

from scipy import constants
import numpy as np
import matplotlib.pyplot as plt

def plankfn(v):
    return (2*constants.h*v**3/(constants.c**2*(np.exp(constants.h*v/(constants.k*T))-1)))

def jeansfn(v):
    return (2*v**2*constants.k*T/constants.c**2)

def weinfn(v):
    return (2*constants.h*v**3/(constants.c**2*np.exp(constants.h*v/(constants.k*T))))

t = np.logspace(0,8,9)
v = np.logspace(0,22,500)

color = ['olive', 'purple', 'red', 'gray', 'gold', 'pink', 'orange', 'cyan', 'brown']
for i in range(len(t)):
    T = t[i]
    plt.plot(v, plankfn(v),color=color[i],label='T = %d'%T)
    plt.plot(v, jeansfn(v),':',color=color[i])
    plt.plot(v, weinfn(v),'--',color=color[i])
    plt.yscale('log')
    plt.xscale('log')
plt.title(r'$log_{10}(I_\nu)\;vs\; log_{10}(\nu)$ plot')
plt.legend()
plt.xlim([1e2,1e22])
plt.ylim([1e-25,1e8])
plt.ylabel('Specific Intensity(Unit=$Jm^{-2}s^{-1}Hz^{-1}sr^{-1}$)')
plt.xlabel('Frequency (Unit=Hz)')
plt.savefig('q5 plot.png')
plt.show()