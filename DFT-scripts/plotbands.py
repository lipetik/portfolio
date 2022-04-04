import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
import readline
from io import StringIO

# Como usar ?

# Passo 1:
# Primeiro coloque o nome do arquivos de bandas com apenas um espaçamento
# entre entre linhas e colunas , retire também qualquer linha no final do
# do arquivo.

# Passo 2:
# Ajustar os comandos de plot da funcao plot bands 

# Arquivos para leitura
bands = "Br3Cr2I3.band.gnu-2" # coloque o arquivo da banda do material
scf = str("Br3Cr2I3.scf.out") # coloque o arquivo de saida do calculo scf


def nivel_de_fermi(scf):
    scf = open(scf)
    for line in scf:
        line = line.lstrip()
        if line.startswith('the Fermi energy '):
            string = line.split()
            fermi_energy = -1 * float(string[4])
            fermi_energy = str(fermi_energy)
            return(float(fermi_energy))


def gap_calculator(bands, energia_de_fermi):
    fermi_level = energia_de_fermi
    band = open(bands)
    positive_arr = []
    negative_arr = []
    for line in band:
        array = line.lstrip().strip().split()
        energy_array = np.array(array[1:2])
        band_shift = []
        for i in energy_array:
            band_shift.append(float(i) + float(fermi_level))
            for i in band_shift:
                if float(i) < 0:
                    negative_arr.append(float(i))
                if float(i) > 0:
                    positive_arr.append(float(i))

    gap = -max(negative_arr) + min(positive_arr)

    return(gap)


# Parametros para ajustar o plot
def plot_bands(bands, energia_de_fermi, Gap):
    lw = 2.5
    k_path = [r'${\Gamma}$', 'K', 'M', r'${\Gamma}$']
    x_path = [0, 0.5774, 0.9107, 1.5773]
    ymin = -2
    ymax = 1
    xmin = 0
    xmax = 1.5773
    name_material = 'Br3Cr2I3 - Supercell'
    figure_name = 'Br3Cr2I3 - Supercell'

########################################################################  
    # Plot de bandas
    with open(bands) as f:
        data = f.read()
    data = data.split('\n\n')
    for d in data:
        ds = np.loadtxt(StringIO(str(d)))
        plt.plot(ds[:, 0], ds[:, 1]+energia_de_fermi, color='blue', lw=2.4)
        plt.ylim(ymin, ymax)
        plt.xlim(xmin, xmax)
    plt.title(f'Bandas de energia {name_material}: Gap calculado = {round(Gap,3)} eV')
    plt.xticks(x_path, k_path, fontsize=16)
    plt.xlabel('K-path', fontsize=16)
    for i in range(len(x_path)):
        plt.axvline(x=x_path[i], linewidth=2, color='black')
    plt.axhline(y=0, lw=lw, color='black')
    plt.axhline(y=1, lw=lw, color='black')
    plt.axhline(y=-2, lw=lw, color='black')
    plt.ylabel('E - Ef (eV)', fontsize=16)
    plt.savefig(f'{figure_name}',dpi=1000)
    plt.show()

#########################################################################


energia_de_fermi = nivel_de_fermi(scf)
Gap = gap_calculator(bands, energia_de_fermi)
print('Fermi energy = ', energia_de_fermi)
plot_bands(bands, energia_de_fermi,Gap)
print('Gap = ', Gap)






