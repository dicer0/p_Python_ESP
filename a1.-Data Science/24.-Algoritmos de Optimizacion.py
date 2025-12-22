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

#Este script ejemplifica distintos tipos de algoritmos y sus complejidades (Big O) en Python,
#mostrando ejemplos de:
# - Algoritmos constantes, lineales, logarítmicos, lineal-logarítmicos, cuadráticos y exponenciales.
# - Uso de estructuras hash (dict y set) para optimización.
# - Medición de tiempo de ejecución usando time y timeit.
# - Comparación de eficiencia y técnicas de optimización.
import time     #time: Librería del manejo de tiempos, como retardos, contadores, etc.
import random   #random: Librería que permite crear números aleatorios.
#bisect: Librería para buscar posiciones o insertar elementos en listas ORDENADAS usando búsqueda binaria.
import bisect

#FUNCIÓN DE TIPO DECORADOR: Es una función que recibe como parámetro otra función, modificándola o extendiéndola, 
#y devolviendo una nueva función. Para ello utiliza una función interna usualmente llamada wrapper (aunque se le 
#puede asignar el nombre que sea) que extrae los valores de los parámetros de la función que el decorador quiere 
#extender, pudiendo así realizar operaciones con ellos si es necesario. Los decoradores pueden recibir CUALQUIER 
#cantidad de argumentos, sin importar si son arrays o diccionarios indicado por (*args, **kwargs).

#medir_tiempo(): Función de tipo decorador que sirve para medir el tiempo de ejecución de cualquier función. 
#Recibe como parámetro el nombre de la función que vaya a procesar y devuelve sus segundos de ejecución.
def medir_tiempo(funcion):
    #wrapper(): Normalmente 
    def wrapper(*args, **kwargs):
        #time.time(): Método que devuelve un timestamp del momento cuando se ejecute esta línea de código.
        tiempo_inicio = time.time()     #Marca de tiempo_inicio
        #Con el resultado de la función no se hace nada en este decorador.
        resultado_funcion = funcion(*args, **kwargs)
        tiempo_final = time.time()      #Marca de tiempo_final
        #Esta es la única extensión que está realizando el decorador, imprime en consola el tiempo de ejecución.
        print(f"{funcion.__name__} ejecutó en: {tiempo_final - tiempo_inicio:.6f} segundos")
        return resultado_funcion
    return wrapper

#O(1) Constante: Acceso directo a diccionarios a través de hash.
#Hash: Este sirve para optimizar búsquedas, ya que toma un dato (por ejemplo un número o una cadena) y lo 
#transforma en un valor numérico fijo que se usa como índice dentro de un diccionario, permitiendo acceder a la 
#información de forma directa y eficiente; gracias a esto, estructuras como dict y set pueden insertar, buscar y 
#eliminar elementos en tiempo constante promedio O(1), evitando recorridos secuenciales como en las listas.
@medir_tiempo
def ejemplo_constante():
    #Creación de un diccionario grande, donde la siguiente línea de código es exactamente lo mismo que:
    #dic = {}
    #for i in range(1000000):
    #   dic[i] = i ** 2
    #Que da como resultado el diccionario: 
    #{i: i^2,
    #0: 0,
    #1: 1,
    #2: 4,
    #...
    #999999: 999998000001}
    dic = {i: i**2 for i in range(1000000)}  #Creación de diccionario grande.
    _ = dic[999999]
    return _

# ------------------------------------------------------
# O(n) Lineal: Recorrer una lista
# ------------------------------------------------------
@medir_tiempo
def ejemplo_lineal(n):
    """
    Recorre una lista de tamaño n para demostrar complejidad lineal O(n)
    """
    arr = list(range(n))
    total = 0
    for num in arr:
        total += num
    return total

# ------------------------------------------------------
# O(log n) Logarítmico: Búsqueda binaria
# ------------------------------------------------------
@medir_tiempo
def ejemplo_logaritmico(n):
    """
    Realiza búsqueda binaria en lista ordenada de tamaño n.
    Demuestra complejidad logarítmica O(log n)
    """
    arr = list(range(n))
    target = n - 1
    index = bisect.bisect_left(arr, target)  # Binary search
    return index

# ------------------------------------------------------
# O(n log n) Lineal-logarítmico: Merge Sort
# ------------------------------------------------------
def merge(left, right):
    """
    Merge de dos listas ordenadas
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

@medir_tiempo
def ejemplo_lineal_logaritmico(n):
    """
    Ordena una lista aleatoria usando Merge Sort (O(n log n))
    """
    arr = [random.randint(0, 1000000) for _ in range(n)]
    return merge_sort(arr)

def merge_sort(arr):
    """
    Implementación recursiva de Merge Sort
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# ------------------------------------------------------
# O(n²) Cuadrático: Doble bucle
# ------------------------------------------------------
@medir_tiempo
def ejemplo_cuadratico(n):
    """
    Doble bucle para demostrar complejidad cuadrática O(n²)
    """
    arr = list(range(n))
    count = 0
    for i in arr:
        for j in arr:
            count += 1
    return count

# ------------------------------------------------------
# O(2^n) Exponencial: Fibonacci recursivo sin memoización
# ------------------------------------------------------
@medir_tiempo
def ejemplo_exponencial(n):
    """
    Calcula Fibonacci de manera recursiva, complejidad exponencial O(2^n)
    """
    def fib(x):
        if x <= 1:
            return x
        return fib(x-1) + fib(x-2)
    return fib(n)

# ------------------------------------------------------
# Optimización usando hash (reducción O(n²) -> O(n))
# ------------------------------------------------------
@medir_tiempo
def ejemplo_hash(nums):
    """
    Detecta duplicados usando set (hash) para optimización de O(n²) -> O(n)
    """
    vistos = set()
    duplicados = []
    for n in nums:
        if n in vistos:
            duplicados.append(n)
        else:
            vistos.add(n)
    return duplicados

# ------------------------------------------------------
# Bloque principal
# ------------------------------------------------------
if __name__ == "__main__":
    print("Ejemplo O(1) Constante:")
    ejemplo_constante()
    
    print("\nEjemplo O(n) Lineal:")
    ejemplo_lineal(1000000)
    
    print("\nEjemplo O(log n) Logarítmico:")
    ejemplo_logaritmico(1000000)
    
    print("\nEjemplo O(n log n) Lineal-Logarítmico (Merge Sort):")
    ejemplo_lineal_logaritmico(100000)
    
    print("\nEjemplo O(n²) Cuadrático:")
    ejemplo_cuadratico(1000)
    
    print("\nEjemplo O(2^n) Exponencial (Fibonacci recursivo):")
    ejemplo_exponencial(30)
    
    print("\nEjemplo de optimización usando Hash (eliminar duplicados):")
    nums = [random.randint(0, 1000) for _ in range(10000)] + [5, 7, 5, 9]
    ejemplo_hash(nums)
