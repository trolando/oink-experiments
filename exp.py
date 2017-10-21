#!/usr/bin/env python3
from __future__ import print_function
from contextlib import contextmanager
import os
import sys
import re
from itertools import chain

# import framework
from expfw import Experiment, ExperimentEngine, online_variance


class ExpOink(Experiment):
    def parse_log(self, contents):
        res = {}
        s = re.compile(r'solving took ([\d\.,]+)').findall(contents)
        if len(s) != 1:
            return None
        res['time'] = float(s[0])
        return res

    def get_text(self, res):
        return "{:0.6f} sec".format(res['time'])

    def get_value(self, res):
        return res['time']

    def compress(self):
        self.name = "{}-c".format(self.name)
        self.solver = "{}-c".format(self.solver)
        self.call += ["--compress"]
        return self

    def inflate(self):
        self.name = "{}-i".format(self.name)
        self.solver = "{}-i".format(self.solver)
        self.call += ["--inflate"]
        return self

    def scc(self):
        self.name = "{}-s".format(self.name)
        self.solver = "{}-s".format(self.solver)
        self.call += ["--scc"]
        return self

    def nosp(self):
        self.name = "{}-n".format(self.name)
        self.solver = "{}-n".format(self.solver)
        self.call += ["--no-loops", "--no-single", "--no-wcwc"]
        return self


class ExpOinkRSL(ExpOink):
    def __init__(self, name, model):
        self.group = name
        self.solver = "rsl"
        self.name = "{}-rsl".format(name)
        self.call = ["tools/oink", "-v", model]
        self.model = model


class ExpOinkPP(ExpOink):
    def __init__(self, name, model):
        self.group = name
        self.solver = "pp"
        self.name = "{}-pp".format(name)
        self.call = ["tools/oink", "--pp", "-v", model]
        self.model = model


class ExpOinkPPP(ExpOink):
    def __init__(self, name, model):
        self.group = name
        self.solver = "ppp"
        self.name = "{}-ppp".format(name)
        self.call = ["tools/oink", "--ppp", "-v", model]
        self.model = model


class ExpOinkRR(ExpOink):
    def __init__(self, name, model):
        self.group = name
        self.solver = "rr"
        self.name = "{}-rr".format(name)
        self.call = ["tools/oink", "--rr", "-v", model]
        self.model = model


class ExpOinkDP(ExpOink):
    def __init__(self, name, model):
        self.group = name
        self.solver = "dp"
        self.name = "{}-dp".format(name)
        self.call = ["tools/oink", "--dp", "-v", model]
        self.model = model


class ExpOinkRRDP(ExpOink):
    def __init__(self, name, model):
        self.group = name
        self.solver = "rrdp"
        self.name = "{}-rrdp".format(name)
        self.call = ["tools/oink", "--rrdp", "-v", model]
        self.model = model


class ExpOinkZLK(ExpOink):
    def __init__(self, name, model):
        self.group = name
        self.solver = "zlk"
        self.name = "{}-zlk".format(name)
        self.call = ["tools/oink", "--zlk", "-w", "-1", "-v", model]
        self.model = model


class ExpOinkZLK1(ExpOink):
    def __init__(self, name, model):
        self.group = name
        self.solver = "zlk-1"
        self.name = "{}-zlk-1".format(name)
        self.call = ["tools/oink", "--zlk", "-w", "1", "-v", model]
        self.model = model


class ExpOinkZLK2(ExpOink):
    def __init__(self, name, model):
        self.group = name
        self.solver = "zlk-2"
        self.name = "{}-zlk-2".format(name)
        self.call = ["tools/oink", "--zlk", "-w", "2", "-v", model]
        self.model = model


class ExpOinkZLK8(ExpOink):
    def __init__(self, name, model):
        self.group = name
        self.solver = "zlk-8"
        self.name = "{}-zlk-8".format(name)
        self.call = ["tools/oink", "--zlk", "-w", "8", "-v", model]
        self.model = model


class ExpOinkPSI(ExpOink):
    def __init__(self, name, model):
        self.group = name
        self.solver = "psi"
        self.name = "{}-psi".format(name)
        self.call = ["tools/oink", "--psi", "-w", "-1", "-v", model]
        self.model = model


class ExpOinkPSI1(ExpOink):
    def __init__(self, name, model):
        self.group = name
        self.solver = "psi-1"
        self.name = "{}-psi-1".format(name)
        self.call = ["tools/oink", "--psi", "-w", "1", "-v", model]
        self.model = model


class ExpOinkPSI8(ExpOink):
    def __init__(self, name, model):
        self.group = name
        self.solver = "psi-8"
        self.name = "{}-psi-8".format(name)
        self.call = ["tools/oink", "--psi", "-w", "8", "-v", model]
        self.model = model


class ExpOinkSPM(ExpOink):
    def __init__(self, name, model):
        self.group = name
        self.solver = "spm"
        self.name = "{}-spm".format(name)
        self.call = ["tools/oink", "--spm", "-v", model]
        self.model = model


class ExpOinkTSPM(ExpOink):
    def __init__(self, name, model):
        self.group = name
        self.solver = "tspm"
        self.name = "{}-tspm".format(name)
        self.call = ["tools/oink", "--tspm", "-v", model]
        self.model = model


class ExpOinkQPT(ExpOink):
    def __init__(self, name, model):
        self.group = name
        self.solver = "qpt"
        self.name = "{}-qpt".format(name)
        self.call = ["tools/oink", "--qpt", "-v", model]
        self.model = model


class ExpPgsolver(Experiment):
    def parse_log(self, contents):
        res = {}
        s = re.compile("Chosen solver `[^']+' \.* ([\d\.,]+) sec").findall(contents)
        if len(s) != 1:
            return None
        res['time'] = float(s[0])
        return res

    def get_text(self, res):
        return "{:0.6f} sec".format(res['time'])

    def compress(self):
        self.name = "{}-c".format(self.name)
        self.call += ["--compress"]

    def dlo(self):
        self.name = "{}-dlo".format(self.name)
        self.call += ["-dlo"]

    def dgo(self):
        self.name = "{}-dgo".format(self.name)
        self.call += ["-dgo"]

    def dsg(self):
        self.name = "{}-dsg".format(self.name)
        self.call += ["-dsg"]

    def noscc(self):
        self.name = "{}-dsd".format(self.name)
        self.call += ["-dsd"]


class ExpPgsolverZlk(ExpPgsolver):
    def __init__(self, name, model):
        self.group = name
        self.solver = "pgzlk"
        self.name = "{}-pgzlk".format(name)
        self.call = ["tools/pgsolver", "-dsd", "-global", "recursive", "-jh", model]
        self.model = model


class ExpPgsolverSpm(ExpPgsolver):
    def __init__(self, name, model):
        self.group = name
        self.solver = "pgspm"
        self.name = "{}-pgspm".format(name)
        self.call = ["tools/pgsolver", "-dsd", "-global", "smallprog", "-jh", model]
        self.model = model


class ExpPgsolverSI(ExpPgsolver):
    def __init__(self, name, model):
        self.group = name
        self.solver = "pgsi"
        self.name = "{}-pgsi".format(name)
        self.call = ["tools/pgsolver", "-dsd", "-global", "optstratimprov", "-jh", model]
        self.model = model


class ExpParsi(Experiment):
    def parse_log(self, contents):
        res = {}
        s = re.compile("^([\d\.,]+)").findall(contents)
        if len(s) != 1:
            return None
        res['time'] = float(s[0])
        return res

    def get_text(self, res):
        return "{:0.6f} sec".format(res['time'])


class ExpParsiSeq(ExpParsi):
    def __init__(self, name, model):
        self.group = name
        self.solver = "parsi-seq"
        self.name = "{}-parsi-seq".format(name)
        self.call = ["tools/parsi", "cpubv", model]
        self.model = model


class ExpParsiMC(ExpParsi):
    def __init__(self, name, model, workers):
        self.group = name
        self.solver = "parsi-mc{}".format(str(workers))
        self.name = "{}-parsi-mc{}".format(name, str(workers))
        self.call = ["tools/parsi", "cpulist", model, str(workers)]
        self.model = model


class ExpSPGSolver(Experiment):
    def parse_log(self, contents):
        res = {}
        s = re.compile("Solved in \.* ([\d\.,]+)s").findall(contents)
        if len(s) != 1:
            return None
        res['time'] = float(s[0])
        return res

    def get_text(self, res):
        return "{:0.6f} sec".format(res['time'])


class ExpSPGSeq(ExpSPGSolver):
    def __init__(self, name, model):
        self.group = name
        self.solver = "spg-seq"
        self.name = "{}-spg-seq".format(name)
        self.call = ["tools/spgsolver", "--justHeat", "on", model]
        self.model = model


class ExpSPGMC(ExpSPGSolver):
    def __init__(self, name, model):
        self.group = name
        self.solver = "spg-mc"
        self.name = "{}-spg-mc".format(name)
        self.call = ["tools/spgsolver", "--justHeat", "on", model, "--concurrent", "on"]
        self.model = model


class ExpPBESPGSolver(Experiment):
    def parse_log(self, contents):
        res = {}
        s = re.compile("solving: ([\d\.,]+)").findall(contents)
        if len(s) != 1:
            return None
        res['time'] = float(s[0])
        return res

    def get_text(self, res):
        return "{:0.6f} sec".format(res['time'])


class ExpPBESPGZLK(ExpPBESPGSolver):
    def __init__(self, name, model):
        self.group = name
        self.solver = "pbeszlk"
        self.name = "{}-pbeszlk".format(name)
        self.call = ["tools/pbespgsolve", "-v", "--timings", "-srecursive", model]
        self.model = model


class ExpPBESPGPP(ExpPBESPGSolver):
    def __init__(self, name, model):
        self.group = name
        self.solver = "pbespp"
        self.name = "{}-pbespp".format(name)
        self.call = ["tools/pbespgsolve", "-v", "--timings", "-sprioprom", model]
        self.model = model


class ExpPBESPGSPM(ExpPBESPGSolver):
    def __init__(self, name, model):
        self.group = name
        self.solver = "pbespg"
        self.name = "{}-pbespg".format(name)
        self.call = ["tools/pbespgsolve", "-v", "--timings", model]
        self.model = model


class Experiments(object):
    def get_solvers(self):
        return {}

    def add_experiment(self, name, filename):
        for s, f in self.get_solvers().items():
            if not hasattr(self, s):
                setattr(self, s, {})
            inst = f(name, filename)
            if inst.solver != s: print("logic error, 'solver' set wrong?")
            getattr(self, s)[name] = inst

    def grouped_experiments(self):
        dicts = tuple(getattr(self, x) for x in self.get_solvers().keys())
        for k in set(chain(*(x.keys() for x in dicts))):
            yield [x[k] for x in filter(lambda x: k in x, dicts)]

    def __iter__(self):
        return self.grouped_experiments()


class DirectoryExperiments(Experiments):
    def __init__(self, directory, forbidden=[]):
        super(DirectoryExperiments, self).__init__()

        # initialize self.models
        files = list(filter(lambda f: os.path.isfile(directory+"/"+f), os.listdir(directory)))
        files = [f[:-len(".pg")] for f in filter(lambda f: f.endswith(".pg"), files)]
        self.models = [(x, "{}/{}.pg".format(directory, x)) for x in files]
        files = list(filter(lambda f: os.path.isfile(directory+"/"+f), os.listdir(directory)))
        files = [f[:-len(".gm")] for f in filter(lambda f: f.endswith(".gm"), files)]
        self.models = self.models + [(x, "{}/{}.gm".format(directory, x)) for x in files]
        files = list(filter(lambda f: os.path.isfile(directory+"/"+f), os.listdir(directory)))
        files = [f[:-len(".gm.bz2")] for f in filter(lambda f: f.endswith(".gm.bz2"), files)]
        self.models = tuple(self.models + [(x, "{}/{}.gm.bz2".format(directory, x)) for x in files])
        for name, filename in self.models:
            if filename not in forbidden:
                self.add_experiment(name, filename)


class OinkExperiments(DirectoryExperiments):
    def get_solvers(self):
        return {
            #'rsl': lambda name, filename: ExpOinkRSL(name, filename),
            'pp': lambda name, filename: ExpOinkPP(name, filename),
            'ppp': lambda name, filename: ExpOinkPPP(name, filename),
            'rr': lambda name, filename: ExpOinkRR(name, filename),
            'dp': lambda name, filename: ExpOinkDP(name, filename),
            'rrdp': lambda name, filename: ExpOinkRRDP(name, filename),
            'zlk': lambda name, filename: ExpOinkZLK(name, filename),
            'psi': lambda name, filename: ExpOinkPSI(name, filename),
            'spm': lambda name, filename: ExpOinkSPM(name, filename),
            'tspm': lambda name, filename: ExpOinkTSPM(name, filename),
            'qpt': lambda name, filename: ExpOinkQPT(name, filename),
            }


class ParsiExperiments(DirectoryExperiments):
    """Experiments to compare strategy improvement implementations."""
    def get_solvers(self):
        return {
            'psi-n': lambda name, filename: ExpOinkPSI(name, filename).nosp(),
            'psi-1-n': lambda name, filename: ExpOinkPSI1(name, filename).nosp(),
            'psi-8-n': lambda name, filename: ExpOinkPSI8(name, filename).nosp(),
            'pgsi': lambda name, filename: ExpPgsolverSI(name, filename),
            'parsi-seq': lambda name, filename: ExpParsiSeq(name, filename),
            'parsi-mc1': lambda name, filename: ExpParsiMC(name, filename, 1),
            'parsi-mc8': lambda name, filename: ExpParsiMC(name, filename, 8),
        }


class SPMExperiments(DirectoryExperiments):
    """Experiments to compare progress measures implementations."""
    def get_solvers(self):
        return {
            'spm-n': lambda name, filename: ExpOinkSPM(name, filename).nosp(),
            'tspm-n': lambda name, filename: ExpOinkTSPM(name, filename).nosp(),
            'qpt-n': lambda name, filename: ExpOinkQPT(name, filename).nosp(),
            'pbespg': lambda name, filename: ExpPBESPGSPM(name, filename),
            'pgspm': lambda name, filename: ExpPgsolverSpm(name, filename),
        }


class ZLKExperiments(DirectoryExperiments):
    """Experiments to compare Zielonka implementations."""
    def get_solvers(self):
        return {
            'zlk-n': lambda name, filename: ExpOinkZLK(name, filename).nosp(),
            'zlk-1-n': lambda name, filename: ExpOinkZLK1(name, filename).nosp(),
            'zlk-8-n': lambda name, filename: ExpOinkZLK8(name, filename).nosp(),
            'pgzlk': lambda name, filename: ExpPgsolverZlk(name, filename),
            'spg-seq': lambda name, filename: ExpSPGSeq(name, filename),
            'spg-mc': lambda name, filename: ExpSPGMC(name, filename),
            'pbeszlk': lambda name, filename: ExpPBESPGZLK(name, filename),
        }


# the experiments

# optional mechanism
forbidden = []
if (os.path.isfile("forbidden")):
    forbidden = [line.strip() for line in open("forbidden")]

# make engine
default_timeout = 600
sr = ExperimentEngine(outdir='logs', timeout=default_timeout)

dirs = []
dirs += ["random"]
dirs += ["modelchecking"]
dirs += ["equivchecking"]
# dirs += ["pgsolver"]
# dirs += ["mlsolver"]
# dirs += ["langincl"]

for directory in dirs:
    sr += OinkExperiments(directory, forbidden)
    sr += ParsiExperiments(directory, forbidden)
    sr += SPMExperiments(directory, forbidden)
    sr += ZLKExperiments(directory, forbidden)

# USAGE
# exp.py rungroup <GROUP> (ITERATIONS=1)
#   run all experiments in group <GROUP>
# exp.py reportgroup <GROUP> (ITERATIONS=1)
#   report all experiments in group <GROUP>
# exp.py list
#   list all groups
# exp.py run (ITERATIONS=1)
#   run all experiments
# exp.py todo (ITERATIONS=1)
#   give list of experiments that are not done
# exp.py csv
# exp.py csvpar2

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == 'rungroup':
            print("Going to run group {}".format(sys.argv[2]))
            if len(sys.argv) > 3:
                sr.run_group(sys.argv[2], int(sys.argv[3]))
            else:
                sr.run_group(sys.argv[2], 1)  # by default just 1 iteration
        elif sys.argv[1] == 'reportgroup':
            print("Going to report group {}".format(sys.argv[2]))
            if len(sys.argv) > 3:
                sr.report_group(sys.argv[2], int(sys.argv[3]))
            else:
                sr.report_group(sys.argv[2], 1)  # by default just 1 iteration
        elif sys.argv[1] == 'list':
            for g in sr.get_groups():
                print(g)
        elif sys.argv[1] == 'run':
            if len(sys.argv) > 2:
                sr.run_experiments(int(sys.argv[2]))
            else:
                sr.run_experiments(1)  # by default just 1 iteration
        elif sys.argv[1] == 'todo':
            if len(sys.argv) > 2:
                sr.todo(int(sys.argv[2]))
            else:
                sr.todo(1)  # by default just 1 iteration
        elif sys.argv[1] == 'cull1':
            # find models for which no solver can do it (broken specs)
            # this is just some of the old pgsolver files
            for group in set([exp.group for exp in sr.experiments]):
                notdone = True
                for e in [exp for exp in sr.experiments if exp.group == group]:
                    fn = e.model
                    status, value = sr.get_status(e, 0)
                    if status != Experiment.NOTDONE:
                        notdone = False
                        break
                if notdone: print(fn)
        elif sys.argv[1] == 'cull2':
            # find models for which every solver solves within 1 second (too easy)
            for group in set([exp.group for exp in sr.experiments]):
                below = true
                for e in [exp for exp in sr.experiments if exp.group == group]:
                    fn = e.model
                    status, value = sr.get_status(e, 0)
                    if status != experiment.DONE or float(value['time']) >= 1.0:
                        below = false
                if below: print(fn)
        elif sys.argv[1] == 'csv':
            # report 1st iteration
            for group in set([exp.group for exp in sr.experiments]):
                for e in [exp for exp in sr.experiments if exp.group == group]:
                    status, value = sr.get_status(e, 0)
                    if status == Experiment.DONE:
                        whichset = e.model[:e.model.find("/")]
                        print("{};{};{};{:.6f}".format(whichset, group, e.solver, value["time"]))
        elif sys.argv[1] == 'csvpar2':
            # report 1st iteration
            for group in set([exp.group for exp in sr.experiments]):
                for e in [exp for exp in sr.experiments if exp.group == group]:
                    status, value = sr.get_status(e, 0)
                    whichset = e.model[:e.model.find("/")]
                    if status == Experiment.DONE:
                        print("{};{};{};{:.6f}".format(whichset, group, e.solver, value["time"]))
                    elif status == Experiment.TIMEOUT:
                        print("{};{};{};{:.6f}".format(whichset, group, e.solver, 2*value))
                    else:
                        print("{};{};{};{:.6f}".format(whichset, group, e.solver, 2*default_timeout))
        else:
            print("Nothing to do?")
    else:
        print("Nothing to do?")
