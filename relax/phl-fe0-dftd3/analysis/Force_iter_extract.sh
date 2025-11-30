#!/bin/bash

input="./../relax.out"         
output="Force_iter.dat"   
: > "$output"   # empty the file

iter=0
grep -E "Total[[:space:]]+force" "$input" | while read -r line; do
    iter=$((iter + 1))	# get the iteration number
    force=$(echo "$line" | awk '{print $4}')	# extract total force
    
    entry="${iter}\t\t${force}"	# format output line
    printf "%b\n" "$entry"
    printf "%b\n" "$entry" >> "$output"
done

echo "Saved to $output"

