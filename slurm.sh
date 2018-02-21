#!/bin/bash

for g in `./exp.py list`
do
    srun -N1 -n1 -c16 --tasks-per-node=1 --exclusive -o job%J.out ./exp.py rungroup "$g" &
done

wait
