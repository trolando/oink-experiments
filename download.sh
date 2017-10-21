#!/bin/sh
if [ ! -f modelchecking.zip ]; then
    wget http://www.open.ou.nl/jke/games/modelchecking.zip
fi
mkdir -p modelchecking && unzip -nj modelchecking.zip "modelchecking/games/*" -d modelchecking
if [ ! -f equivchecking.zip ]; then
    wget http://www.open.ou.nl/jke/games/equivchecking.zip
fi
mkdir -p equivchecking && unzip -nj equivchecking.zip "equivchecking/games/*" -d equivchecking
if [ ! -f pgsolver.zip ]; then
    wget http://www.open.ou.nl/jke/games/pgsolver.zip
fi
mkdir -p pgsolver && unzip -nj pgsolver.zip "pgsolver/games/*" -d pgsolver
if [ ! -f mlsolver.zip ]; then
    wget http://www.open.ou.nl/jke/games/mlsolver.zip
fi
mkdir -p mlsolver && unzip -nj mlsolver.zip "mlsolver/games/*" -d mlsolver
if [ ! -f bench-li.zip ]; then 
    wget https://www7.in.tum.de/tools/gpupg/bench-li.zip
fi
mkdir -p langincl && unzip -nj bench-li.zip -d langincl
