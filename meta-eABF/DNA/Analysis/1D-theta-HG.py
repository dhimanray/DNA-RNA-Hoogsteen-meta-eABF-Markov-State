import numpy as np 
import matplotlib.pyplot as plt
l = np.loadtxt('pmf_200_ns01')

num_bins = int(np.sqrt(2*len(l)))
bin_width = abs(l[0,0] - l[num_bins,0])

kT = 0.6
rho = np.zeros((num_bins))
F = np.zeros((num_bins,2))

#------------ Watson Crick part -------------------#
for i in range(num_bins):
    for j in range(num_bins/2):
        A = l[num_bins*j+i,2]
        rho[i] += np.exp(-A/kT)*bin_width
    F[i,0] = l[i,1]
    F[i,1] = -kT*np.log(rho[i])
#print rho
#print F


mmin = min(F[:,1])
F[:,1] -= mmin

#print F

f1 = open('DNA-HG-1D-PMF-theta.dat','w')
for i in range(num_bins):
    print >>f1, F[i,0], F[i,1]
f1.close()







