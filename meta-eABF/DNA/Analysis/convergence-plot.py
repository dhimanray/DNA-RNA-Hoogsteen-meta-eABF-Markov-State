import numpy as np
import matplotlib.pyplot as plt

l = np.loadtxt('convergence200.dat')

plt.plot(l[:,0], l[:,1],linewidth=5)
plt.xlabel('Simulation time (ns)')
plt.ylabel('RMS Deviation from the PMF at 200 ns (kcal/mol)')
plt.xlim(0,200)
plt.ylim(0,11)
plt.show()
