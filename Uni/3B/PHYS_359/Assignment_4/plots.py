import numpy as np
from numpy import append
from pylab import plot,show,setp,xlim,ylim,axis,ylabel,xlabel,title,legend

def f(x, g):
    den = (1 + g*np.exp(-1.0/x))*(1 + g*np.exp(-1.0/x))
    y = (g/(x*x))*(np.exp(-1.0/x)/den)
    return y

xmax = 3
x = np.linspace(0.001, xmax, num=1000)
y = np.zeros((5, 1000))

#First plot aka 4 c)

#fill the x and y range
for j in range(5):
    g = float(j) + 1.0
    y0 = []
    for i in x:
        y0.append(f(float(i), g))
    y[j:] = y0
    plot(x,y0,label="g = %d"%(g,))

#plot(x,y[0],'b')
#plot(x,y[1],'r')
#plot(x,y[2],'g')
#plot(x,y[3],'c')
#plot(x,y[4],'m')
xlabel('$T$ in units of $\epsilon / k_{B}$')
ylabel('$C(T)$')
legend(loc = 1, ncol = 1)
show()


