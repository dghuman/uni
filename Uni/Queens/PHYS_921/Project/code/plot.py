# Python file for making simple plots in project

import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mplt

mplt.rc('xtick', labelsize=12)
mplt.rc('ytick', labelsize=12)

plt.rcParams.update({'font.size' : 20})
plt.rc('legend', fontsize = 18)

# Let x = E_S,0 - E_D,0
x = np.linspace(-1, 1, 100)
t = np.linspace(0, 10, 100)

# Simple SM case
def no_osc(x, T = 2, gamma = 1):
    exp = np.exp(-gamma*T)
    sin = (np.sin(x*0.5*T))
    return exp*(sin**2)/x**2


# My approx.
s13 = 2.24E-2
s12 = 3.10E-1

m2_nu = np.array([[0, -7.39E-5, -7.39E-5 - 2.45E-3], [7.39E-5, 0, -2.45E-3], [7.39E-5 + 2.45E-3, 2.45E-3, 0]])
U2 = np.array([(1 - s13)*(1 - s12), (1 - s13)*s12, s13])

def approx(x, T = 2, E = 1, sigma_p = 1, L = 1):
    v1 = 1
    v2 = (1 - m2_nu[1][0]/E)
    v3 = (1 - m2_nu[2][1]/E)*v2

    v = np.array([v1, v2, v3])
    T_j = np.array([T - L/v[0], T - L/v[1], T - L/v[2]])

    def T_min(j,k):
        return np.minimum(T_j[j],T_j[k])

    L_coh = (E**2)/np.abs(m2_nu)
    exp = np.exp(-np.abs(m2_nu)/(2*sigma_p))

    p_sum = 0

    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            T_jk = T_min(j,k)
            first_half = np.heaviside(T_jk, 1)*U2[j]*U2[k]*exp[j][k]*np.exp(-T_jk)*np.exp(-L/(L_coh[j][k]))
            second_half = np.sin(0.5*x*T_j[j])*np.sin(0.5*x*T_j[k])/(x**2)
            final = first_half*second_half
            p_sum = p_sum + final
    
    return p_sum


plt.title(r"Probability vs. Time")
#plt.title(r"Probability vs. Energy")
#plt.plot(x, no_osc(x), color='k', label=r'SM')
#plt.plot(x, approx(x), color='g', label=r'My Approx')
plt.plot(t, no_osc(x=1,T=t), color='k', label=r'SM')
plt.plot(t, approx(x=1,T=t), color='g', label=r'My Approx')
plt.legend(loc='upper right')
#plt.xlabel(r'$E_{S,0} - E_{D,0}$')
plt.xlabel(r'$T$')
plt.ylabel(r'$\mathcal{P}$')
plt.savefig('/home/dilraj/Documents/uni/uni/Uni/Queens/PHYS_921/Project/plots/T_plot.eps', format='eps')


