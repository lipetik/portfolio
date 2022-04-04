reset

set xtics font 'Arial ,15'
set ytics font 'Arial ,15'
set xlabel "Energy (eV)" font 'Arial ,14'
set xrange [-4:4] 
set ylabel "Density of states" font 'Arial ,17'
#set key top left
set yzeroaxis linetype 8 lw 2.0 
set yzeroaxis ls 8 lw 2.0
#set key top right box
#set key width 0.02
#set key height 0.02
#set key font "Arial,11"
set key noautotitle

plot 'Br3Cr2I3.pdos_atm#1(Cr1)_wfc#1(s)' using ($1+2.4973):2 with lines lt rgb "black"       lw 2.5 title "Cr-(s)" ,\
     'Br3Cr2I3.pdos_atm#1(Cr1)_wfc#3(p)' using ($1+2.4973):2 with lines lt rgb "red"         lw 2.5 title "Cr-(p)" ,\
     'Br3Cr2I3.pdos_atm#1(Cr1)_wfc#4(d)' using ($1+2.4973):2 with lines lt rgb "blue"        lw 2.5 title "Cr-(d)" ,\
     'Br3Cr2I3.pdos_atm#3(I)_wfc#1(s)'   using ($1+2.4973):2 with lines lt rgb "yellow"      lw 2.5 title "I-(s)"  ,\
     'Br3Cr2I3.pdos_atm#3(I)_wfc#2(p)'   using ($1+2.4973):2 with lines lt rgb "magenta"     lw 2.5 title "I-(p)"  ,\
     'Br3Cr2I3.pdos_atm#3(I)_wfc#3(d)'   using ($1+2.4973):2 with lines lt rgb "green"       lw 2.5 title "I-(d)"  ,\
     'Br3Cr2I3.pdos_atm#6(Br)_wfc#1(s)'  using ($1+2.4973):2 with lines lt rgb "light-blue"  lw 2.5 title "Br-(s)" ,\
     'Br3Cr2I3.pdos_atm#6(Br)_wfc#2(p)'  using ($1+2.4973):2 with lines lt rgb "turquoise"   lw 2.5 title "Br-(p)" ,\
     'Br3Cr2I3.pdos_atm#6(Br)_wfc#3(d)'  using ($1+2.4973):2 with lines lt rgb "orange"      lw 2.5 title "Br-(d)" ,\
     'Br3Cr2I3.pdos_atm#1(Cr1)_wfc#1(s)' using ($1+2.4973):(-$3) with lines lt rgb "black"       lw 2.5 ,\
     'Br3Cr2I3.pdos_atm#1(Cr1)_wfc#3(p)' using ($1+2.4973):(-$3) with lines lt rgb "red"         lw 2.5 ,\
     'Br3Cr2I3.pdos_atm#1(Cr1)_wfc#4(d)' using ($1+2.4973):(-$3) with lines lt rgb "blue"        lw 2.5 , \
     'Br3Cr2I3.pdos_atm#3(I)_wfc#1(s)'   using ($1+2.4973):(-$3) with lines lt rgb "yellow"      lw 2.5 ,\
     'Br3Cr2I3.pdos_atm#3(I)_wfc#2(p)'   using ($1+2.4973):(-$3) with lines lt rgb "magenta"     lw 2.5 ,\
     'Br3Cr2I3.pdos_atm#3(I)_wfc#3(d)'   using ($1+2.4973):(-$3) with lines lt rgb "green"       lw 2.5 ,\
     'Br3Cr2I3.pdos_atm#6(Br)_wfc#1(s)'  using ($1+2.4973):(-$3) with lines lt rgb "light-blue"  lw 2.5 , \
     'Br3Cr2I3.pdos_atm#6(Br)_wfc#2(p)'  using ($1+2.4973):(-$3) with lines lt rgb "turquoise"   lw 2.5 , \
     'Br3Cr2I3.pdos_atm#6(Br)_wfc#3(d)'  using ($1+2.4973):(-$3) with lines lt rgb "orange"      lw 2.5  






