import MDAnalysis as md

for i in range(1,6):

    u = md.Universe('3base_traj_1.pdb','pcca%d_5states_500samples_tica-2ns.pdb'%i)
    f1 = open('pcca%d_5states_chi_theta_eta.dat'%i,'w')
    for ts in u.trajectory:             #loop over frames of trajectory
#---------- CALCULATE CHI ------------------#
        #select the atom objects
        x1 = u.select_atoms('bynum 88')
        x2 = u.select_atoms('bynum 89')
        x3 = u.select_atoms('bynum 90')
        x4 = u.select_atoms('bynum 97')

        #calculate position of the atoms
        r1 = x1.positions
        r2 = x2.positions
        r3 = x3.positions
        r4 = x4.positions

        #calculate the dihedral angle
        chi = md.lib.distances.calc_dihedrals(r1,r2,r3,r4)

#----------- Calculate Theta ----------------#
        #select the atom group objects
        p1 = u.select_atoms('bynum 9:17 49:59 71:78 111:120')
        p2 = u.select_atoms('bynum 102:106')
        p3 = u.select_atoms('bynum 81:85')
        p4 = u.select_atoms('bynum 97 91 92 93 90')

        #calculate center of mass of groups
        pr1 = p1.center_of_mass()
        pr2 = p2.center_of_mass()
        pr3 = p3.center_of_mass()
        pr4 = p4.center_of_mass()

        #calculate the dihedral angle
        theta = md.lib.distances.calc_dihedrals(pr1,pr2,pr3,pr4)


        
#----------- Calculate Eta ------------------#
        t1 = u.select_atoms('bynum 9:17 49:59 71:78 111:120')
        t2 = u.select_atoms('bynum 40:44')
        t3 = u.select_atoms('bynum 20:24')
        t4 = u.select_atoms('bynum 29:37')

        #calculate center of mass of groups
        tr1 = t1.center_of_mass()
        tr2 = t2.center_of_mass()
        tr3 = t3.center_of_mass()
        tr4 = t4.center_of_mass()

        #calculate the dihedral angle
        eta = md.lib.distances.calc_dihedrals(tr1,tr2,tr3,tr4)

        print(chi[0]*180.0/3.14, theta*180.0/3.14, eta*180.0/3.14, file=f1)
    f1.close()

