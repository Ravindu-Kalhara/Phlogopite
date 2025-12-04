#!/bin/bash

scf_prefix="phl"
output="Etot_ecut.dat"
: > "$output"	# empty the file

for file in "$scf_prefix".ecut_*.out; do
    ecutwfc=$(echo "$file" | sed 's/.*ecut_//; s/\.out$//')	 # extract ecutwfc
    total_energy=$(grep -e '^!.*total energy' "$file" | awk '{print $5}')	# extract total energy

    line="${ecutwfc}\t\t${total_energy}"
    printf "%b\n" "$line"	# print to terminal
    printf "%b\n" "$line" >> "$output"	# append to file
done

echo "Saved results to $output"
