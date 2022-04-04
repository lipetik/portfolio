set encoding utf8

set xtics("G" 0.000, "M" 0.5774 , "K" 0.9107 , "G" 1.5773) font 'Arial,18'
set key font "Arial,15"

set grid xtics lt -1 lw 2.5 
f(x) = 0
set title "Bands-GGA-U" font 'Arial,20'
set ylabel "Energy(eV)" font 'Arial,15'
set ytics font 'Arial,18'
unset key

plot [0:1.5773] [-2:2] "Br3Cr2I3.band.gnu" using 1:($2+2.4973) with lines  lt rgb "red" lw 3.0, \
     f(x) with lines lt rgb "black" lw 2.0
