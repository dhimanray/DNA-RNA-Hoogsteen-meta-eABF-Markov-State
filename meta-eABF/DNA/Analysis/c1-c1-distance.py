import MDAnalysis as md


u = md.Universe('ionized.psf','5UZF-meta-eABF.dcd')
i = 0
f1 = open('c1-c1-distance.dat','w')
for ts in u.trajectory:             #loop over frames of trajectory
#--C1 of ADE -----------------
    n1 = u.select_atoms('bynum 484')
    r1 = n1.positions
#--C1 of THY -------------------
    n3 = u.select_atoms('bynum 264')
    r3 = n3.positions
#calculate distances
    cc = md.lib.distances.distance_array(r1,r3)
    i += 1
    print(i,cc[0,0], file=f1)
f1.close()

