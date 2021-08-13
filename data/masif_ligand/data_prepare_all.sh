#!/bin/bash
#SBATCH --account def-liyue
#SBATCH --cpus-per-task 1
#SBATCH --mem 64G
#SBATCH --time 08:00:00
#SBATCH --array=0-49
#SBATCH --output=../../logs/masif_precompute.%A_%a.out

masif_root=$(git rev-parse --show-toplevel)
masif_source=$masif_root/source/
cd $masif_source

i=0
for p in ../../data/PDBbind-refine-set/*
do
    name=$(basename $p)
    if [ ${#name} == 4 ]
    then
        if [ $(( i % 50 )) == ${SLURM_ARRAY_TASK_ID} ]
            then
            echo $name
            ../data/masif_ligand/data_prepare_one.sh $name
        fi
        i=$((i+1))
    fi
done
