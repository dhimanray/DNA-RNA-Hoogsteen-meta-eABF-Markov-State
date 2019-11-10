#:/bin/bash

for i in {41..45}
do
	cd /oasis/tscc/scratch/dray1/dhiman/DNA-Hoogsteen/Markov-State/5UZF/MSM/MSM_trajectory_$i
	qsub job-submission.sh
done
