#!/bin/bash
#SBATCH --job-name=watermelon_blastn
#SBATCH --partition = cloud72
#SBATCH --nodes=1
#SBATCH --qos = cloud
#SBATCH --cpus-per-task=32
#SBATCH --time=1:00:00
#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=mmiya@uark.edu
module purge
module load blast

cd $SLURM_SUMIT_DIR

# Run the blast command
blastn -query watermelon.fsa -subject watermelon.fsa > wat.vs.wat.blastn
