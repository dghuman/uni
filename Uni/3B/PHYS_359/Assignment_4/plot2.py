import numpy as np
from numpy import append
from pylab import subplots,plot,show,setp,xlim,ylim,axis,ylabel,xlabel,title,legend,scatter

def f(x, g):
    den = (1.0 + g*np.exp(-1.0/x))*(1.0 + g*np.exp(-1.0/x))
    y = (g/(x*x))*(np.exp(-1.0/x)/den)
    return y

xmax = 3
x = np.linspace(0.001, xmax, num=1000)
#y = np.zeros((5, 1000))
s = 20
T = []
C = []
#Plot of 4 d)

#fill the x and y range
for j in range(5):
    g = float(j) + 1.0
    y0 = []
    for i in x:
        y0.append(f(float(i), g))
    #y[j:] = y0
    C.append(max(y0))
    T.append(y0.index(max(y0)))
    #plot(x,y0,label="g = %d"%(g,))

fig, ax1 = subplots()
ax2 = ax1.twinx()
lns1 = ax1.scatter([1,2,3,4,5],T, c='b', label = '$T$')
ax1.set_xlabel('$g = g_{e}/g_{0}$')
ax1.set_ylabel('$T_{max}$')
#x.sort()
lns2 = ax2.scatter([1,2,3,4,5],C, c='r', label = '$C$')
ax2.set_ylabel('Max $C(T)$')
ax1.legend(loc = 1, ncol = 1)
ax2.legend(loc = 2, ncol=1)
show()

