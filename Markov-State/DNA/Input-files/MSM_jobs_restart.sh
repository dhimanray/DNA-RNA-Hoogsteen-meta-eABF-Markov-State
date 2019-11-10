#:/bin/bash

for i in {26..45}
do
	cd /oasis/tscc/scratch/dray1/dhiman/DNA-Hoogsteen/Markov-State/5UZF/MSM/MSM_trajectory_$i
	cp production.conf production.conf.old
	cp ../production.conf .
	qsub job-submission.sh
done
