# Python file for making simple plots in project

import numpy as np
from matplotlib import pyplot as plt

# Let x = E_S,0 - E_D,0
x = np.linspace(-1, 1, 100)

def no_osc(x, T = 1, gamma = 1):
    exp = np.exp(-gamma*T)
    sin = (np.sin(x*0.5*T))
    return exp*(sin**2)/x**2


plt.title(r"M$\ddot{o}$ssbaur Neutrinos")  
plt.plot(x, no_osc(x), color='k', label=r'$T=\gamma=1$')
plt.plot(x, no_osc(x, T=3), color='r', label=r'$T=3$')
plt.plot(x, no_osc(x, T=5), color='b', label=r'$T=5$')
#plt.yscale("log")
plt.legend()
plt.xlabel(r'$E_{S,0} - E_{D,0}$')
plt.ylabel(r'$\mathcal{P}$')
plt.savefig('/home/dilraj/Documents/uni/uni/Uni/Queens/PHYS_921/Project/plots/plot.png', dpi=300)
