# Python script to plot some functions from Q5 (b) on Assignment 1

import cmath
import matplotlib.pyplot as plt

N = 100.
omega_0 = 0.5
sigma = 0.1

C_t = []
cn_t = []
t = range(1, 101, 1)

    
def c_n(n):
    omega_n = n/N
    return cmath.exp(-(omega_n - omega_0)*(omega_n - omega_0)/(sigma*sigma))

A = 0

for i in range(1,101,1):
    A += c_n(i)

# invert A since the true coeffecient is 1/A    
A = 1.0/A

def C(t):
    ans_1 = 0
    ans_2 = 0
    for n in range(1,101,1):
        omega_n = n/N
        ans_1 += cmath.exp(-(omega_n - omega_0)*(omega_n - omega_0)/(sigma*sigma))*cmath.exp(1j*omega_n*t)
        ans_2 += cmath.exp(-(omega_n - omega_0)*(omega_n - omega_0)/(sigma*sigma))*cmath.exp(-1j*omega_n*t)
    return  A*cmath.sqrt(ans_1*ans_2)

# fill the arrays
for m in t:
    C_t.append(C(m))


# Plot the darn thing
plt.plot(C_t)

# plot the c_i(t) terms iteratively
for k in range(1,101,1):
    c_i = []
    omega_k = k/N
    print omega_k
    for n in t:
        c_i.append((A*c_n(k)*cmath.exp(1j*omega_k*n)).real)
    plt.plot(c_i)
    
plt.savefig('Q5_plot.png', dpi= 300)

