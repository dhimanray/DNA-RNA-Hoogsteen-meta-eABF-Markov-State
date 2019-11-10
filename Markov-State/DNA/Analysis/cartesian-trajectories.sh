#:/bin/bash

for i in {1..45}
do
	cp cartesian-traj.py ../MSM_trajectory_$i
	cd ../MSM_trajectory_$i
	python cartesian-traj.py 
	mv 3base.pdb ../Cartesian-trajectories/3base_traj_$i.pdb
	mv 3base.dcd ../Cartesian-trajectories/3base_traj_$i.dcd
	cd ../Cartesian-trajectories
done
