# -*- coding: utf-8 -*-

#En Python se introducen comentarios de una sola linea con el simbolo #.
#La primera línea de código incluida en este programa se conoce como declaración de codificación o codificación 
#de caracteres. Al especificar utf-8 (caracteres Unicode) como la codificación, nos aseguramos de que el archivo 
#pueda contener caracteres especiales, letras acentuadas y otros caracteres no ASCII sin problemas, garantizando 
#que Python interprete correctamente esos caracteres y evite posibles errores de codificación.
#Se puede detener una ejecución con el comando [CTRL] + C puesto en consola, con el comando "cls" se borra su 
#historial y en Visual Studio Code con el botón superior derecho de Play se corre el programa.
#Para comentar en Visual Studio Code varias líneas de código se debe pulsar:
#[CTRL] + K (VSCode queda a la espera). Después pulsa [CTRL] + C para comentar y [CTRL] + U para descomentar.

#AUTOMATIZACIÓN PARA MOVER EL MOUSE INDEFINIDAMENTE DE FORMA CIRCULAR:
#PyAutoGUI: Biblioteca que permite controlar el mouse y el teclado para realizar tareas repetitivas, automatizar 
#procesos de software, o incluso realizar tareas de accesibilidad para personas con discapacidades.
import pyautogui
#keyboard: Librería que permite detectar pulsaciones de teclas en el teclado.
import keyboard
#math: Librería que proporciona funciones y constantes matemáticas como seno, π, logaritmo, etc.
import math
#time: Librería para el manejo de tiempos, como retardos, contadores, etc.
import time

#pyautogui.size(): Método para obtener el tamaño de la pantalla de forma automática en forma de la siguiente 
#tupla: (ancho, alto).
screen_width, screen_height = pyautogui.size()
#Ahora calcularemos el centroide de la pantalla al dividir entre dos su ancho y altura.
center_x = screen_width // 2    #Centroide x = Ancho / 2
center_y = screen_height // 2   #Centroide y = Altura / 2
#Se declara el radio del movimiento circular del mouse en pixeles.
radius = 100
#La velocidad del movimiento circular del mouse se utilizará dentro del bucle while que realiza el movimiento.
speed = 0.05  #Control de velocidad: Mientras mayor sea, más rápido se moverá el mouse.

#calculate_next_position(): Función que calcula la próxima posición del mouse en forma de círculo a través de 
#la librería math.
def calculate_next_position(angle):
    #math.cos(): Método que calcula el coseno de un ángulo dado en radianes. 
    x = center_x + int(radius * math.cos(angle))
    #math.sin(): Método que calcula el seno de un ángulo dado en radianes.
    y = center_y + int(radius * math.sin(angle))
    return x, y

#Bucle while: Este checa si se ha presionado la tecla s, para determinar si se debe detener o no el movimiento 
#circular del mouse.
angle = 0
while not keyboard.is_pressed('s'):
    #Calcular la próxima posición.
    next_x, next_y = calculate_next_position(angle)
    #Mover el mouse a la siguiente posición.
    pyautogui.moveTo(next_x, next_y, duration=0)
    #Incrementar el ángulo.
    angle += speed
    #Hacer que el ángulo se mantenga dentro del rango de 0 a 2pi.
    angle %= (2 * math.pi)
    #time.sleep(): Método que se utiliza para suspender la ejecución de un programa durante un intervalo de 
    #tiempo específico dado en segundos. El delay se cambia para controlar la velocidad del mouse.
    time.sleep(0.01)

#print(): Método para imprimir un mensaje en consola y después dar un salto de línea (Enter).
print("Program stopped.")