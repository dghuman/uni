import math,numpy
import matplotlib.pyplot as plt
#import operator as op
#from functools import reduce

# some definitions to make the computation easier
#def ncr(n, r):
#    r = min(r, n-r)
#    numer = reduce(op.mul, range(n, n-r, -1), 1)
#    denom = reduce(op.mul, range(1, r+1), 1)
#    return numer//denom

def alpha(thetai):
    return numpy.sqrt(1-((1.0/2.42)*numpy.sin(thetai))**2)/numpy.cos(thetai)

beta = 2.42
beta2 = 1.5
theta = numpy.linspace(0,math.pi/2., 100)

ER = (alpha(theta) - beta)/(alpha(theta) + beta)
ET = 2./(alpha(theta) + beta)
T = ((alpha(theta) - beta)/(alpha(theta)+beta))**2
R = alpha(theta)*beta*(2/(alpha(theta) + beta))**2
ER2 = (1-alpha(theta)*beta2)/(1+alpha(theta)*beta)
ET2 = 2./(alpha(theta)*beta + 1)

plt.plot([0.0,0.0],[-0.4,1.0], 'black')
plt.plot([0.0,1.6],[0.0,0.0], 'black')
plt.plot(theta,ET, 'b', label=r'$E_{T}/E_{I}$')
plt.plot(theta,ER, 'r', label=r'$E_{R}/E_{I}$')
plt.xlabel(r'$\theta_{I}$ in Radian')
plt.ylabel('Ratio')
plt.legend()
plt.annotate(r'$\theta_{C}$',xy=(1.36,0.29),xytext=(-10,30),textcoords='offset points',ha='right',va='bottom',bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))
plt.annotate(r'$\theta_{B}$',xy=(1.178,0.0),xytext=(0,20),textcoords='offset points',ha='right',va='bottom',bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))
plt.show()
    
plt.plot([0.0,0.0],[-0.4,1.0], 'black')
plt.plot([0.0,1.6],[0.0,0.0], 'black')
plt.plot([1.36,1.36],[0.0,1.0], 'gray')
plt.plot(theta,T, 'b', label='T')
plt.plot(theta,R, 'r', label='R')
plt.xlabel(r'$\theta_{I}$ in Radian')
plt.ylabel('Ratio')
plt.legend()
plt.annotate(r'$\theta_{C}$',xy=(1.36,0.3),xytext=(-10,30),textcoords='offset points',ha='right',va='bottom',bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))
plt.annotate(r'$\theta_{B}$',xy=(1.178,0.0),xytext=(0,20),textcoords='offset points',ha='right',va='bottom',bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))
plt.show()

plt.plot([0.0,0.0],[-0.4,1.0], 'black')
plt.plot([0.0,1.6],[0.0,0.0], 'black')
plt.plot(theta,ET2, 'b', label=r'$E_{T}/E_{I}$')
plt.plot(theta,ER2, 'r', label=r'$E_{R}/E_{I}$')
plt.xlabel(r'$\theta_{I}$ in Radian')
plt.ylabel('Ratio')
plt.legend()
plt.plot()
#savefig('thisistheone.png')

