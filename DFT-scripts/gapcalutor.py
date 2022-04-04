#!/usr/bin/env python3
import numpy as np
import matplotlib as mpl
import readline
import sys

#variaveis
bands = str(sys.argv[1])
fermi_energy = sys.argv[2]

# Gap calculator
def gap_calculator(bands,fermi_energy):
    negative_arr = []
    positive_arr = []
    band = open(bands)
    for line in band:
            array = line.lstrip().strip().split()
            band_arr = np.array(array[1:2])
            band_shift = [] 
            for i in band_arr:
                    band_shift.append(float(i)+ float(fermi_energy)) 
                    for i in band_shift:
                            if float(i) < 0:
                                    negative_arr.append(float(i))
                            if float(i) > 0:
                                    positive_arr.append(float(i))

    gap = -max(negative_arr) + min(positive_arr)
    return(gap)

# ############### MAIN ######################
# print(nivel_de_fermi(var))
# fermi_energy = (nivel_de_fermi(var)) 


gap = gap_calculator(bands,fermi_energy)
gap = round(gap, 2)  # arredonda o gap
print(gap)





