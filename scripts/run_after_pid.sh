#!/bin/bash

pid=49693   # PID of the running process

while kill -0 "$pid" 2>/dev/null; do
    sleep 1
done

echo "Job Started..."
./phl-fe1.ecut.sh
echo "Job Ended."
