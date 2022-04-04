import PyGnuplot as pg 
import numpy as np
import matplotlib as mpl
import readline

#variaveis
#arquivo de entrada
bands = str("Br3Cr2I3.band.gnu") #arquivo de saido do bands.x
var = "Br3Cr2I3.scf.out" #arquivo de saida do scf

#entradas do gnuplot
titulo = "GGA-PBE-U"
intervalo_x = "[0:1.5773]"
intervalo_y = "[-2:2]"
 
#nivel de fermi
def nivel_de_fermi(var):
   arquivo = open(var)
   for line in arquivo:
           line = line.lstrip()
           if line.startswith("the Fermi energy "):
                   string = line.split()
                   fermi_energy= float(string[4])
                   fermi_energy= str(-1*fermi_energy)
                   return(float(fermi_energy))
   
##########################################################

##########################################################
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

############################################################################
print(nivel_de_fermi(var))
fermi_energy = (nivel_de_fermi(var)) 
gap = gap_calculator(bands,fermi_energy)
gap = round(gap ,2) #arredonda o gap

############################################################################

#gnuplot plot
pg.c('f(x) = 0') 
readline.read_init_file(bands)
pg.c('set title "'+ str(titulo)+ ' of Gap = ' + str(gap) + " eV font 'Arial,20'")
pg.c('plot '+intervalo_x+' '+ intervalo_y+' ' + repr(bands) + ' using 1:($2+' + str(nivel_de_fermi(var)) + ') with lines lt rgb "blue" lw 3.0 ')
pg.c('replot f(x) with lines lt rgb "black" lw 2.5')







