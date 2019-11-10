import numpy as np
import matplotlib.pyplot as plt

for i in range(5):

    l = np.loadtxt('pcca%d_5states_chi_theta_eta.dat'%(i+1))
#    plt.figure(i)
    if i==0:
        ll = 'HG'
    elif i==4:
        ll = 'WC'
    else :
        ll = 'I%d'%i
    plt.scatter(l[:,0],l[:,1],marker='.',label=ll)
    plt.xlim(-180,180)
    plt.ylim(-180,180)
    plt.xlabel('$\chi$ ($^{\circ}$)',fontsize=18)
    plt.ylabel('$\Theta$ ($^{\circ}$)',fontsize=18)
    plt.xticks([-180,-90,0,90,180])
    plt.yticks([-180,-90,0,90,180])
    plt.title('DNA', fontsize=18, fontweight='bold')
    plt.tick_params(labelsize=18)
    plt.legend(fontsize=16,ncol=1)
plt.tight_layout()
#plt.show()
plt.savefig('Chi-theta-plot.pdf')
