#!/bin/bash

for g in `./exp.py list`
do
    srun -N1 -n1 -c8 -o job%J.out --exclusive ./exp.py rungroup "$g" &
done

wait
