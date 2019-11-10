import numpy as np

ref = np.loadtxt('pmf_200_ns')


for i in range(20,200,2):
    l = np.loadtxt('pmf_%d_ns'%i)
    mse = 0.0
    for j in range(len(l)):
        mse += (1./len(l))*(l[j][2] - ref[j][2])**2
    rmse = np.sqrt(mse)
    print i, rmse
