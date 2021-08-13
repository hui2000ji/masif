#!/bin/bash
#SBATCH --account def-liyue
#SBATCH --cpus-per-task 1
#SBATCH --mem 64G
#SBATCH --time 08:00:00
#SBATCH --array=0-49
#SBATCH --output=../../logs/masif_precompute.%A_%a.out

i=0
for p in ../../data/PDBbind-refine-set
do
    if [ ${#p} == 4 ]
    then
        if [ $(( i % 50 )) == ${SLURM_ARRAY_TASK_ID} ]
            then
            echo $p
            ../data/masif_ligand/data_prepare_one.sh $p
        fi
        i=$((i+1))
    fi
done
