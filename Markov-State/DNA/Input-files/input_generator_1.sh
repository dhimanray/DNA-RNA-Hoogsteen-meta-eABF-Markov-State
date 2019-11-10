#!/bin/bash

cd /home/dhiman/DNA-Hoogsteen/Markov-State/5UZF/initial_States/starting-structure

i=1
for f in frame*; do
	outdir=MSM_trajectory_$i
	mkdir $outdir
	cp $f $outdir/5UZF-MSM.pdb
	cp /home/dhiman/DNA-Hoogsteen/Markov-State/5UZF/initial_States/ideal-input/* $outdir
	sed -i "s/MSM_trajectory/$outdir/g" $outdir/job-submission.sh
	((i++))
done	
