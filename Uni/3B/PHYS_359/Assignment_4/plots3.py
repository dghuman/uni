import numpy as np
from numpy import append
from pylab import plot,show,setp,xlim,ylim,axis,ylabel,xlabel,title,legend

def f(t, delta):
    e1 = np.exp(-delta/t)
    e2 = 2.0*np.exp(-1.0/t)
    z = 1.0 + e1 + 2.0*e2
    y = (1/(t*t))*((z*(delta*delta*e1 + 2.0*e2) - (delta*e1 + 2.0*e2)*(delta*e1 + 2.0*e2))/(z*z))
    return y

xmax = 1
x = np.linspace(0.001, xmax, num=1000)
y = np.zeros((5, 1000))
delta = [0.0,0.05,0.075,0.1,0.2,0.3]
#First plot aka 4 c)

#fill the x and y range
for j in range(len(delta)):
    y0 = []
    for i in x:
        y0.append(f(float(i), delta[j]))
    #y[j:] = y0
    plot(x,y0,label="$\delta$ = %f"%(delta[j],))

#plot(x,y[0],'b')
#plot(x,y[1],'r')
#plot(x,y[2],'g')
#plot(x,y[3],'c')
#plot(x,y[4],'m')
xlabel('$t$')
ylabel('$C(t)/k_{B}$')
legend(loc = 1, ncol = 1)
show()


