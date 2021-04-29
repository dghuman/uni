# Python file for making simple plots in project

import numpy as np
from matplotlib import pyplot as plt

# Let x = E_S,0 - E_D,0
x = np.linspace(-1, 1, 100)

# Simple SM case
def no_osc(x, T = 1, gamma = 1):
    exp = np.exp(-gamma*T)
    sin = (np.sin(x*0.5*T))
    return exp*(sin**2)/x**2


# My approx.
s13 = 2.24E-2
s12 = 3.10E-1

m2_nu = np.array([[0, -7.39E-5, -7.39E-5 - 2.45E-3], [7.39E-5, 0, -2.45E-3], [7.39E-5 + 2.45E-3, 2.45E-3]])
U2 = np.array([(1 - s13)*(1 - s12), (1 - s13)*s12, s13])

def approx(x, T = 2, E = 1, sigma_p = 1, L = 1):
    v1 = 1
    v2 = (1 - m2_nu[1][0]/E)
    v3 = (1 - m2_nu[2][1]/E)*v2

    v = np.array([v1, v2, v3])
    T_j = T - L/v

    def T_min(j,k):
        return min([T_j[j],T_j[k]])

    L_coh = (E**2)/abs(m2_nu)
    exp = np.exp(-abs(m2_nu)/(2*sigma_p))

    sum = 0

    for j in range(3):
        for k in range(3):
            
    
    






plt.title(r"M$\ddot{o}$ssbaur Neutrinos")  
plt.plot(x, no_osc(x), color='k', label=r'$T=\gamma=1$')
plt.plot(x, no_osc(x, T=3), color='r', label=r'$T=3$')
plt.plot(x, no_osc(x, T=5), color='b', label=r'$T=5$')
#plt.yscale("log")
plt.legend()
plt.xlabel(r'$E_{S,0} - E_{D,0}$')
plt.ylabel(r'$\mathcal{P}$')
plt.savefig('/home/dilraj/Documents/uni/uni/Uni/Queens/PHYS_921/Project/plots/plot.png', dpi=300)
