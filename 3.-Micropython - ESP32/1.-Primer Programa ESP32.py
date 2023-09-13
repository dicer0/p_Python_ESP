# -*- coding: utf-8 -*-

#Comentario de una sola linea con el simbolo #, en Python para nada se deben poner acentos sino el programa
#puede fallar o imprimir raro en consola, la siguiente línea de código es para que no tenga error, pero aún
#así al poner un ángulo saldrá raro en consola, la línea debe ponerse tal cual como aparece y justo al inicio.

#PROGRAMA PARA PARPADEAR UN LED DEL MICROCONTROLADOR ESP32
#Librerías para poder usar el convertidor ADC (Analógico-Digital), el UART que es la comunicación serial con el ESP32, y los pines del ESP32
from machine import ADC, UART, Pin
import time #time: Librería del manejo de tiempos, como retardos, contadores, etc.
#El uart 0 es el de comunicación, por lo que no es recomendable usarlo, 
uart = UART(2, 9600) #Tasa de muestreo en el puerto serie UART número 2 del ESP32, que es el pin 25 (GPIO16) y 27 (GPIO17) llamado U2_TXD y U2_RXD

time.sleep(0.1) #Duerme 0,1 segundos

adc = ADC(Pin(32)) 

adc.atten(ADC.ATTN_11DB)

led = Pin(2, Pin.OUT) #Pin de salida el pin 2 del ESP32

count = 0

while(True):
    ai0 = adc.read()
    str_ai0 = str(ai0) + "\r\n"
    uart.write(str_ai0)
    
    print(str(ai0))
    
    if(count%2 == 0):
        led.value(1) #Prende led digital
    else:
        led.value(0) #Apaga led digital
    if(count == 100):
        count = 0
    count = count + 1
    time.sleep(1)