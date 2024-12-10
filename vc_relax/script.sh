#!/bin/bash

# Ensure the script stops on any error
set -e

# Go to phl-fe0/Step01 directory
cd ./phl-fe0/Step01
echo "Current Directory: $(pwd)"

echo "Starting Quantum ESPRESSO phl-fe0/Step01 vc-relax calculation..."

# Run the mpirun command
mpirun -np 12 --oversubscribe pw.x -inp vc_relax.in > vc_relax.out

# Check the exit status of the command
if [ $? -eq 0 ]; then
    echo "phl-fe0/Step01 vc-relax calculation completed successfully!"
else
    echo "phl-fe0/Step01 vc-relax calculation failed!" >&2
    exit 1
fi

# Go to phl-fe0 directory
cd ./../../phl-fe1
echo "Current Directory: $(pwd)"

echo "Starting Quantum ESPRESSO phl-fe1 vc-relax calculation..."

# Run the mpirun command
mpirun -np 12 --oversubscribe pw.x -inp vc_relax.in > vc_relax.out

# Check the exit status of the command
if [ $? -eq 0 ]; then
    echo "phl-fe1 vc-relax calculation completed successfully!"
else
    echo "phl-fe1 vc-relax calculation failed!" >&2
    exit 1
fi

echo "Script execution finished."

