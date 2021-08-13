#!/bin/bash
#SBATCH --nodes 1
#SBATCH --partition=serial
#SBATCH --ntasks-per-node 1
#SBATCH --cpus-per-task 1
#SBATCH --mem 16000
#SBATCH --time 02:00:00
#SBATCH --array=1-1000
#SBATCH --output=exelogs/out/_masif_precompute.%A_%a.out
#SBATCH --error=exelogs/err/_masif_precompute.%A_%a.err

i=0
while read p; do
    if [ $(( i % 1000 + 1 )) == ${SLURM_ARRAY_TASK_ID} ]; then
        echo $p
        ./data_prepare_one.sh $p
    fi
    i=$((i+1))
done < keys.txt
