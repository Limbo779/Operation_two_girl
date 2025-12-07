#!/bin/bash

# Run each script in the background (&)
# Redirect all output (success and errors) to the "void" (/dev/null)

echo "Started the process"

python3 m1.py > /dev/null 2>&1 &
python3 m2.py > /dev/null 2>&1 &
python3 m3.py > /dev/null 2>&1 &
python3 m4.py > /dev/null 2>&1 &
python3 m5.py > /dev/null 2>&1 &
python3 m6.py > /dev/null 2>&1 &
python3 m7.py > /dev/null 2>&1 &
python3 m8.py > /dev/null 2>&1 &
python3 m9.py > /dev/null 2>&1 &
python3 m10.py > /dev/null 2>&1 &

# Wait for all of them to finish before closing
wait

echo "All 10 scripts finished."
