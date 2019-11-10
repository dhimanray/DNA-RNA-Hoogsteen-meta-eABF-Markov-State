import numpy as np 
import matplotlib.pyplot as plt
l = np.loadtxt('pmf_200_ns')

num_bins = int(np.sqrt(len(l)))
bin_width = abs(l[1,1] - l[2,1])

kT = 0.6
rho = np.zeros((num_bins))
F = np.zeros((num_bins,2))
for i in range(num_bins):
    for j in range(num_bins):
        A = l[num_bins*i+j,2]
        rho[i] += np.exp(-A/kT)*bin_width
    F[i,0] = l[num_bins*i,0]
    F[i,1] = -kT*np.log(rho[i])
#print rho
#print F

l = []
mmin = min(F[:,1])
F[:,1] -= mmin

#print F

f1 = open('DNA-1D-PMF-chi.dat','w')
for i in range(num_bins):
    print >>f1, F[i,0], F[i,1]
f1.close()



