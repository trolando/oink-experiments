Obtaining games
===============
* Use generate.py to generate the random games (needs "rngame" and "stgame" in tools/)
* Use download.sh to download and extract the benchmarks by Keiren

Compiling Oink
==============
* sources: https://www.github.com/trolando/oink
* build with CMake
* copy oink, rngame, stgame to tools/

Compiling SPGSolver
===================
* sources: https://www.github.com/umbertomarotta/SPGSolver/
* g++ CPPSolver.cpp -std=c++11 -lboost\_program\_options -lpthread -O3 -o spgsolver 
* copy spgsolver to tools/spgsolver

Compiling parallel-si
=====================
* sources: https://www.github.com/jfearnley/parallel-si
* build with CMake
* copy parsi to tools/

Compiling pbespgsolver
======================
* sources: https://svn.win.tue.nl/repos/MCRL2/ revision 15046
* build with CMake, disable all the extra tooling
* copy pbespgsolver to tools/

Compiling PGSolver
==================
* sources: https://github.com/tcsprojects/pgsolver
* build with OPAM
* copy pgsolver to tools/

To run the experiments
======================
* in terminal: ./exp.py run 1
* with slurm: sbatch slurm.sh

To obtain the results to csv
============================
* just the finished experiments:./exp.py csv > results.csv
* with PAR2 score (penalize timeouts x2): ./exp.py csvpar2 > par2.csv

Remarks
=======
* List of games odd cycles: oddcycles
* Log files used for the paper: logs.tar.bz2
* The csv files used for the paper: results.csv, par2.csv
* Random games used for the paper: random.tar.bz2 (split into 100M files)
* Use "Release" builds in CMake
