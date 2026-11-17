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
#ctypes: Librería para llamar funciones del sistema operativo (en este caso, la API de Windows).
import ctypes

#pyautogui.moveTo() en Windows usa SetCursorPos(): el cursor sí se mueve en pantalla, pero Windows no lo
#registra como actividad del usuario. Por eso el temporizador de inactividad sigue corriendo y, al rato de
#no estar presente, la sesión se bloquea igual. mouse_event() con MOUSEEVENTF_MOVE sí cuenta como entrada.
MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_ABSOLUTE = 0x8000
#SetThreadExecutionState(): pide que, mientras este programa siga en ejecución, no se apague la pantalla
#ni el equipo entre en suspensión. Al terminar hay que soltar ese pedido.
ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002

#pyautogui.size(): Método para obtener el tamaño de la pantalla de forma automática en forma de la siguiente 
#tupla: (ancho, alto).
screen_width, screen_height = pyautogui.size()
#Ahora calcularemos el centroide de la pantalla al dividir entre dos su ancho y altura.
center_x = screen_width // 2    #Centroide x = Ancho / 2
center_y = screen_height // 2   #Centroide y = Altura / 2
#Se declara el radio del movimiento circular del mo se en pixeles.
radius = 100
#La velocidad del movimiento circular del mouse se utilizará dentro del bucle while que realiza el movimiento.
speed = 0.005  #Control de velocidad: Mientras mayor sea, más rápido se moverá el mouse.

#calculate_next_position(): Función que calcula la próxima posición del mouse en forma de círculo a través de 
#la librería math.
def calculate_next_position(angle):
    #math.cos(): Método que calcula el coseno de un ángulo dado en radianes. 
    x = center_x + int(radius * math.cos(angle))
    #math.sin(): Método que calcula el seno de un ángulo dado en radianes.
    y = center_y + int(radius * math.sin(angle))
    return x, y

#move_mouse(): Avisa a Windows de un movimiento real. Las coordenadas absolutas de mouse_event() van de
#0 a 65535 y cubren el monitor principal, no van en pixeles directos.
def move_mouse(x, y):
    converted_x = 65536 * x // screen_width + 1
    converted_y = 65536 * y // screen_height + 1
    ctypes.windll.user32.mouse_event(
        MOUSEEVENTF_MOVE | MOUSEEVENTF_ABSOLUTE,
        ctypes.c_long(converted_x),
        ctypes.c_long(converted_y),
        0,
        0,
    )

#keep_display_awake(): Reinicia el temporizador de pantalla y de suspensión de Windows.
def keep_display_awake():
    ctypes.windll.kernel32.SetThreadExecutionState(
        ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED
    )

#release_display(): Devuelve a Windows su comportamiento normal de apagado y bloqueo de pantalla.
def release_display():
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)

#Bucle while: Este checa si se ha presionado la tecla s, para determinar si se debe detener o no el movimiento 
#automático circular del mouse. try/finally suelta el pedido de "pantalla activa" aunque el programa termine
#con la tecla S o con [CTRL] + C.
angle = 0
keep_display_awake()
try:
    while not keyboard.is_pressed('s'):
        #Calcular la próxima posición.
        next_x, next_y = calculate_next_position(angle)
        #Mover el mouse a la siguiente posición y renovar el pedido de mantener la pantalla encendida.
        move_mouse(next_x, next_y)
        keep_display_awake()
        #Incrementar el ángulo.
        angle += speed
        #Hacer que el ángulo se mantenga dentro del rango de 0 a 2pi.
        angle %= (2 * math.pi)
        #time.sleep(): Método que se utiliza para suspender la ejecución de un programa durante un intervalo de 
        #tiempo específico dado en segundos. El delay se cambia para controlar la velocidad del mouse.
        time.sleep(0.01)
finally:
    release_display()

#print(): Método para imprimir un mensaje en consola y después dar un salto de línea (Enter).
print("Program stopped.")