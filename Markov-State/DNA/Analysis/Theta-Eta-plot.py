import numpy as np
import matplotlib.pyplot as plt

for i in range(5):
    if i==0:
        title = 'HG'
    elif i==4:
        title = 'WC'
    else :
        title = 'I%d'%i

    l = np.loadtxt('pcca%d_5states_chi_theta_eta.dat'%(i+1))
    plt.figure(i)
    plt.scatter(l[:,1],l[:,2],marker='.',c='g')
    plt.xlim(-180,180)
    plt.ylim(-180,180)
    plt.xlabel('$\Theta$ ($^{\circ}$)',fontsize=20)
    plt.ylabel('$\eta$ ($^{\circ}$)',fontsize=20)
    plt.title(title,fontsize=20)
    plt.xticks([-180,-90,0,90,180])
    plt.yticks([-180,-90,0,90,180])
    plt.tick_params(labelsize=20)
#histogm, theta_edges, eta_edges = np.histogram2d(l[:,1], l[:,2], bins=180, density=False)

#cp=plt.pcolormesh(theta_edges,eta_edges,histogm,cmap='rainbow')
#cbar=plt.colorbar(cp)
#cbar.set_label('Density',fontsize=14)

#plt.show()
    plt.tight_layout()
    plt.savefig('pcca-5states-%d.pdf'%(i+1))
