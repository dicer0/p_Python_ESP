#Programa que genera una señal senoidal de 400Hz desde el DAC de la pyboard, terminal X5

#PROGRAMA PARA GENERAR UNA SEÑAL SENOIDAL ARMÓNICA EN LA PYBOARD:
from pyb import DAC
from math import pi, sin

dac = DAC(0)

buf = bytearray(100)

for i in range(len(buf)):
    buf[i] = 128 + int(127 * sin(2*pi*i/len(buf)))
dac.write_timed(buf, 400*len(buf), mode = DAC.CIRCULAR)