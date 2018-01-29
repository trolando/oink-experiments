These instructions are for the artifact evaluation of TACAS.

The virtual machine needs extra packages that must be installed first.

If you want to test more than just some of the example model checking, equivalence checking or random instances, see README.md.

Setup required packages
=======================
* `sudo dpkg -i debs/*deb`

Compile Oink
============
* `cd oink`
* `mkdir build`
* `cd build`
* `cmake .. -DBUILD_EXTRA_TOOLS=1 ..`
* `make`
* `cd ../..`
* `mkdir tools`
* `cp oink/build/oink tools/`

Extract random games
====================
* `cat random.tar.bz2.* | tar Jxv`

Extract log files
=================
* `tar xf logs.tar`

Running Oink
============
* `tools/oink --help`
* `tools/oink -v examples/<model> --<solver>`
