import MDAnalysis as md

u = md.Universe('ionized.psf','5UZF-MSM.dcd')

base = u.select_atoms("resid 8-10 or resid 15-17 and not name H*")

up_below_base = u.select_atoms("resid 8 or resid 10 or resid 15 or resid 17 and not name H*")

with md.Writer("3base.dcd",base.n_atoms) as W:
    for ts in u.trajectory:
        com = base.center_of_mass()
        ts.positions -= com
        W.write(base)
with md.Writer("3base.pdb",base.n_atoms) as W:
    if u.trajectory.frame == 0:
        W.write(base)
    


