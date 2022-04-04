#!/usr/bin/env python
import sys
var = str(sys.argv[1])
arquivo = open(var)
for line in arquivo:
        line = line.lstrip()
        if line.startswith("the Fermi energy is") :
                print(line)
