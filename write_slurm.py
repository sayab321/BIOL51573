#!/bin/env python3
print("#!/bin/bash")

job_name = "watermelon_blastn"
hours = 1
partition = "cloud72"
qos = "cloud"
email = "mmiya@uark.edu"

print(f"#SBATCH --job-name={job_name}")
print(f"#SBATCH --partition = {partition}")
print(f"#SBATCH --nodes=1")
print(f"#SBATCH --qos = {qos}")
print(f"#SBATCH --cpus-per-task=32")
print(f"#SBATCH --time={hours}:00:00")
print(f"#SBATCH --output=%x.%j.out")
print(f"#SBATCH --error=%x.%j.err")
print(f"#SBATCH --mail-type=ALL")
print(f"#SBATCH --mail-user={email}")

print("module purge")
print("module load blast")
print("")

print("# Run the blast command")
print("blastn -query watermelon.fsa -subject watermelon.fsa > wat.vs.wat.blastn")

