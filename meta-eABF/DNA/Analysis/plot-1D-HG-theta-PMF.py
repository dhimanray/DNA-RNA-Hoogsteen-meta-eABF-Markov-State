import numpy as np
import matplotlib.pyplot as plt

F = np.loadtxt('DNA-HG-1D-PMF-theta.dat')

F1 = np.loadtxt('RNA-HG-1D-PMF-theta.dat')

plt.plot(F[:,0], F[:,1],'b-', lw=4, label='A6-DNA')
plt.plot(F1[:,0], F1[:,1], 'r-', lw=4, label='A6-RNA')
plt.title('PMF along $\Theta$ (HG)',fontsize=18)
plt.xlabel("$\Theta (\circ)$",fontsize=18)
plt.ylabel("PMF (kcal/mol)",fontsize=18)
plt.xticks([-180,-90,0,90,180])
plt.xlim(-180,180)
plt.ylim(0,13)
#plt.legend(fontsize=16)
plt.tick_params(labelsize=18)
#plt.show()
plt.tight_layout()
plt.savefig('1d-compare-HG-theta.pdf')
