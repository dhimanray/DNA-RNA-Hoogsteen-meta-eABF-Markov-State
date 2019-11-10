import numpy as np
import matplotlib.pyplot as plt

F = np.loadtxt('convergence.dat')

F1 = np.loadtxt('RNA-convergence.dat')

plt.plot(F[:,0], F[:,1],'b-', label='A6-DNA')
plt.plot(F1[:,0], F1[:,1], 'r-',label='A6-RNA')
plt.xlabel("Simulation time (ns)",fontsize=16)
plt.ylabel("RMSD of PMF (kcal/mol)",fontsize=16)
plt.legend(fontsize=16)
plt.ylim(0,11)
#plt.show()
plt.savefig('convergence-DNA-RNA.pdf')
