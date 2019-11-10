import MDAnalysis as md


u = md.Universe('ionized.psf','5UZF-meta-eABF.dcd')
i = 0
f1 = open('h-bond-distance.dat','w')
for ts in u.trajectory:             #loop over frames of trajectory
#--N1 of ADE -----------------
    n1 = u.select_atoms('bynum 491')
    r1 = n1.positions
#--N7 of ADE ------------------
    n7 = u.select_atoms('bynum 488')
    r7 = n7.positions
#--N3 of THY -------------------
    n3 = u.select_atoms('bynum 271')
    r3 = n3.positions
#calculate distances
    wc = md.lib.distances.distance_array(r1,r3)
    hg = md.lib.distances.distance_array(r7,r3)
    i += 1
    print(i,wc[0,0],hg[0,0], file=f1)
f1.close()

