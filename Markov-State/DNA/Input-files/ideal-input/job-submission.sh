#!/bin/csh
#PBS -A ucichem-gibbs
#PBS -q home-gibbs
#PBS -N ext_eq Run1
#PBS -l nodes=1:ppn=2
###PBS -l procs=4
#PBS -l walltime=48:00:00
#PBS -o pbs.out
#PBS -e pbs.err
#PBS -V
#PBS -M dray1@uci.edu
#PBS -m ae

module load cuda
#export NAMD="/home/anupamc/NAMD_2.13b1_Linux-x86_64-multicore-CUDA"
#export LD_LIBRARY_PATH="${NAMD}/libcudart.so.9.1"
        
cd /oasis/tscc/scratch/dray1/dhiman/DNA-Hoogsteen/Markov-State/5UZF/MSM/MSM_trajectory
#module load 
/home/dray1/NAMD_2.12_Linux-x86_64-multicore-CUDA/namd2 +idlepoll +isomalloc_sync +p 2 production.conf > production.log
