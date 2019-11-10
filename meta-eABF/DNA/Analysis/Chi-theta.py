import MDAnalysis as md

u = md.Universe('ionized.psf','5UZF-meta-eABF.dcd')
f1 = open('chi_theta.dat','w')
i = 0
for ts in u.trajectory:             #loop over frames of trajectory
#---------- CALCULATE CHI ------------------#
    #select the atom objects
    x1 = u.select_atoms('bynum 483')
    x2 = u.select_atoms('bynum 484')
    x3 = u.select_atoms('bynum 486')
    x4 = u.select_atoms('bynum 495')

    #calculate position of the atoms
    r1 = x1.positions
    r2 = x2.positions
    r3 = x3.positions
    r4 = x4.positions

    #calculate the dihedral angle
    chi = md.lib.distances.calc_dihedrals(r1,r2,r3,r4)

#----------- Calculate Theta ----------------#
    #select the atom group objects
    p1 = u.select_atoms('bynum 234:247 298:312 456:467 518:531')
    p2 = u.select_atoms('bynum 505:509')
    p3 = u.select_atoms('bynum 473:477')
    p4 = u.select_atoms('bynum 495 487 488 486 489 490')

    #calculate center of mass of groups
    pr1 = p1.center_of_mass()    
    pr2 = p2.center_of_mass()
    pr3 = p3.center_of_mass()
    pr4 = p4.center_of_mass()

    #calculate the dihedral angle
    theta = md.lib.distances.calc_dihedrals(pr1,pr2,pr3,pr4)

    i += 1
    print(i,chi[0], theta, file=f1)
f1.close()

