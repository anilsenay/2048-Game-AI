#!/bin/bash
for i in {1..20}
do
   python main.py > "results/heuristic_run_$i.txt"
done