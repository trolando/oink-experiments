#!/usr/bin/env python3
import os
from subprocess import call


def rngame(*args, _out):
    call(["tools/rngame"]+[str(x) for x in args], stdout=_out)


def stgame(*args, _out):
    call(["tools/stgame"]+[str(x) for x in args], stdout=_out)


def generate_rngames(count, size, maxPrio, minOutDeg, maxOutDeg):
    print("Generating {} random games with parameters {}, {}, {}, {}...".format(count, size, maxPrio, minOutDeg, maxOutDeg))
    for k in range(0, count):
        fn = "random/rn-{}-{}-{}-{}-{}.pg".format(size, maxPrio, minOutDeg, maxOutDeg, k)
        if not os.path.isfile(fn):
            with open(fn, "w+") as outfile:
                rngame(size, maxPrio, minOutDeg, maxOutDeg, "x", _out=outfile)


def generate_stgames(count, size, minOutDeg, maxOutDeg, minInDeg, maxInDeg):
    print("Generating {} steady games with parameters {}, {}-{}, {}-{}...".format(count, size, minOutDeg, maxOutDeg, minInDeg, maxInDeg))
    for k in range(0, count):
        fn = "random/st-{}-{}-{}-{}-{}-{}.pg".format(size, minOutDeg, maxOutDeg, minInDeg, maxInDeg, k)
        if not os.path.isfile(fn):
            with open(fn, "w+") as outfile:
                stgame(size, minOutDeg, maxOutDeg, minInDeg, maxInDeg, _out=outfile)


if __name__ == "__main__":
    generate_rngames(20, 100, 100, 1, 2)
    generate_rngames(20, 200, 200, 1, 2)
    generate_rngames(20, 500, 500, 1, 2)
    generate_rngames(20, 1000, 1000, 1, 2)
    generate_rngames(20, 2000, 2000, 1, 2)
    generate_rngames(20, 5000, 5000, 1, 2)
    generate_rngames(20, 10000, 10000, 1, 2)
    generate_rngames(20, 20000, 20000, 1, 2)
    generate_rngames(20, 40000, 40000, 1, 2)
    # generate_rngames(20, 70000, 70000, 1, 2)
    # generate_rngames(20, 100000, 100000, 1, 2)
    generate_rngames(20, 100, 100, 1, 100)
    generate_rngames(20, 500, 500, 1, 500)
    generate_rngames(20, 1000, 1000, 1, 1000)
    generate_rngames(20, 2000, 2000, 1, 2000)
    generate_rngames(20, 4000, 4000, 1, 4000)
    generate_rngames(20, 7000, 7000, 1, 7000)
    generate_stgames(20, 100, 1, 4, 1, 4)
    generate_stgames(20, 200, 1, 4, 1, 4)
    generate_stgames(20, 500, 1, 4, 1, 4)
    generate_stgames(20, 1000, 1, 4, 1, 4)
    generate_stgames(20, 2000, 1, 4, 1, 4)
    generate_stgames(20, 5000, 1, 4, 1, 4)
    generate_stgames(20, 10000, 1, 4, 1, 4)
    generate_stgames(20, 20000, 1, 4, 1, 4)
    generate_stgames(20, 40000, 1, 4, 1, 4)
