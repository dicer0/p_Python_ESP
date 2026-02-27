# -*- coding: utf-8 -*-
#TIPOS DE ESTRUCTURAS DE DATOS EN PYTHON: La gran diferencia entre ellos, es que algunos tienen cierto orden (índice y valor) y otros no, 
#además de que algunos son editables o mutables, donde se les puede agregar, eliminar, o modificar elementos y otros son inmutables, donde sus 
#datos no se pueden cambiar.
# - Listas (list): Una lista es una colección ordenada y mutable (editable) de elementos. Se definen utilizando corchetes [].
#       Ejemplo: mi_lista = [1, 2, "hola", True].
# - Tuplas (tuple): Una tupla es una colección ordenada e inmutable de elementos. Se definen utilizando paréntesis ().
#       Ejemplo: mi_tupla = (1, 2, "hola", True).
# - Diccionarios (dict): Un diccionario es una colección desordenada y mutable de pares clave-valor. Se definen utilizando llaves {} y separando 
#   cada par clave-valor por dos puntos (:).
#       Ejemplo: mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}.
# - Conjuntos (set): Un conjunto es una colección desordenada y mutable de elementos únicos. No permite elementos duplicados y no tiene un orden 
#   definido. Se definen utilizando el método set() y utilizan las mismas llaves de los diccionarios {}.
#       Ejemplo: mi_conjunto = {1, 2, 3, 4, 5}.


#Ejercicio 1: Dada una lista de números enteros, crea una nueva lista que contenga únicamente los números pares, conservando el orden original.
datos = [3, 10, 7, 4, 2, 9, 8]
def nums_pares(datos):
    resultado = []
    #Operador de módulo (%): Calcula el cociente de una división entre 2 números, siendo una herramienta fundamental para determinar 
    #divisibilidad, alternar acciones (pares/impares) o limitar rangos de valores, su sintaxis es: 
    #       divisor/dividendo = cociente
    #       divisor%dividendo = resultado_operador_modulo;  7/2 = 3, con cociente = 1, por lo tanto 7%2 = 1, esto indica que 7 es impar.
    for i in datos:
        if(i%2 == 1):
            #- continue: Comando que interrumpe la iteración actual del condicional o bucle actual y salta inmediatamente a la siguiente vuelta, 
            #  sin ejecutar el resto del código.
            #- break: Comando que rompe completamente el condicional o bucle, no solo la iteración actual, sin afectar a los bucles/condicionales 
            #  exteriores, solo donde se encuentre contenido.
            #- pass: Comando que no hace nada, sirve para cuando Python exija al menos una instrucción dentro del bloque.
            continue
        else:
            #.append(): Comando que agrega un valor al final de una lista, su equivalente en diccionarios es .update() y en conjuntos es .add().
            resultado.append(i)
    print("1.-", resultado, "\n")
nums_pares(datos)


#Ejercicio 2: Dada una cadena de texto, devuelve un diccionario donde la clave sea cada carácter distinto y el valor sea el número de veces que 
#aparece.
texto = "programacion"
def frecuencia_letras(texto):
    diccionario_texto = {}
    for letra in texto:
        #diccionario.keys(): Método que devuelve una lista con todas las claves de un diccionario, ya sea que existan algunas o no.
        llaves = diccionario_texto.keys()
        if(letra in llaves):
            #diccionario[keys] = value: De esta forma se asigna un nuevo value a una clave existente o no existente.
            diccionario_texto[letra] += 1   #Si ya existe la letra en las llaves del diccionario, le suma un 1 y lo asigna como nuevo value.
        else:
            diccionario_texto[letra] = 1    #Si no existía la letra, se agrega como una nueva key y se le asigna el valor de 1.
    print("2.-", diccionario_texto, "\n")
frecuencia_letras(texto)


#Ejercicio 3: Dadas dos listas de enteros, devuelve una lista ordenada con: Los elementos comunes entre ambas y sin duplicados.
lista_a = [1, 2, 2, 3, 4, 5]
lista_b = [3, 4, 4, 5, 6, 7]
#set(): Método que sirve para convertir una lista o tupla de elementos nativos iterables (int, string, float, zip, etc.) en un 
#conjunto, el cual se caracteriza por no tener duplicados ni contener estructuras anidadas, con ellas se pueden realizar 
#operaciones lógicas de intersección (&), Unión (|), diferencia (A-B), etc.
sin_duplicados_a = set(lista_a); print(sin_duplicados_a)
sin_duplicados_b = set(lista_b); print(sin_duplicados_b)
#sorted(): Método para ordenar de menor a mayor los elementos de una estructura mutable (editable), como una lista, diccionario, conjunto etc.
elementos_comunes_sin_duplicados = sorted(list(sin_duplicados_a & sin_duplicados_b)); print("3.-", elementos_comunes_sin_duplicados, "\n")


#Ejercicio 4: Dado un diccionario de estudiantes y sus calificaciones, devuelve una lista con los nombres de los estudiantes cuyo promedio sea 
#mayor o igual a 8, ordenada alfabéticamente.
calificaciones = {
    "Ana": [9, 8, 10],
    "Luis": [7, 6, 8],
    "Sofía": [10, 9, 9],
    "Pedro": [6, 7, 6]
}
#Si se quiere recorrer las llaves o valores de un diccionario individualmente se debe hacer lo siguiente:
for nombre in calificaciones:                   #Recorrer solo keys, no poner nada en el bucle for es equivalente a utilizar el método .keys().
    print(nombre)
for notas in calificaciones.values():           #Recorrer solo values, para ello sí se debe utilizar explícitamente el método .values().
    print(notas)
#Si se quiere recorrer todas las llaves como los valores de un diccionario se debe utilizar el método .items():
def mejores_promedios(calificaciones):
    estudiantes_mas_de_ocho = []
    #diccionario.items(): Método que devuelve una lista de tuplas con los pares {key: value}, conteniendo dentro de las tuplas internas: 
    #lista = [(key, value)]. 
    #Aunque cabe mencionar que aunque se ve como una lista de tuplas, en realidad devuelve un tipo de dato especial llamado dict_items.
    for nombre, notas in calificaciones.items():    #Recorrer keys y values, para ello se utiliza el método .items().
        print(nombre, notas)
        #sum(): Suma todos los elementos de una lista.
        #len(): Obtiene el número de elementos de una lista (tamaño).
        promedio = sum(notas)/len(notas)
        if(promedio >= 8):
            estudiantes_mas_de_ocho.append(nombre)
    estudiantes_mas_de_ocho = sorted(estudiantes_mas_de_ocho)
    print("4.-", estudiantes_mas_de_ocho, "\n")
mejores_promedios(calificaciones)


#Ejercicio 5: Dada una lista de números, devuelve el primer número que se repite, aquí tenemos que considerar el tiempo de ejecución para usar 
#un algoritmo de menor tiempo de ejecución O(n), se podría utilizar búsqueda binaria.
numeros = [4, 2, 7, 3, 2, 5, 7]
def primer_repetido(numeros):
    #set(): Un conjunto es una colección desordenada, heterogénea y mutable de elementos únicos. No permite elementos duplicados ni tiene orden.
    vistos = set()          #Variable que almacena todos los elementos no repetidos, para compararlos entre ellos.
    for num in numeros:
        if num in vistos:
            return num
        vistos.add(num)
print("5.-", primer_repetido(numeros), "\n")


#Ejercicio 6: Dado un diccionario donde la clave es el nombre de un producto y el valor es otro diccionario con su información, Devuelve un 
#diccionario ordenado alfabéticamente con los nombres de los productos que: Tengan stock mayor a 0 y cuyo precio sea mayor o igual a 1000.
productos = {
    "Laptop": {"precio": 15000, "stock": 5},
    "Mouse": {"precio": 300, "stock": 0},
    "Teclado": {"precio": 800, "stock": 12},
    "Monitor": {"precio": 4000, "stock": 3}
}
def diccionario_productos(productos):
    result_product = {}
    #diccionario.items(): Método que devuelve una lista de tuplas con los pares {key: value}, conteniendo dentro de las tuplas internas: 
    #lista = [(key, value)]. 
    #Aunque cabe mencionar que aunque se ve como una lista de tuplas, en realidad devuelve un tipo de dato especial llamado dict_items.
    for nombre_producto, info in productos.items():
        #Como info es un diccionario interno, para extraer y separar sus valores se puede utilizar su key y guardarlo en variables.
        precio = info["precio"]
        stock = info["stock"]
        if(stock >= 0 and precio >= 1000):
            result_product[nombre_producto] = precio
    #sorted(): Método para ordenar de menor a mayor los elementos de una estructura mutable, como una lista, diccionario, conjunto, etc.
    #Nota: Cuando se esté utilizando en diccionarios, forzosamente se debe utilizar con el método dict.items().
    print("6.-", dict(sorted(result_product.items())), "\n")
diccionario_productos(productos)


#Ejercicio 7: Dado un diccionario donde la clave es el nombre de una persona y el valor es su edad, Crea un nuevo diccionario con la estructura:
#{
#    "mayores": [...],
#    "menores": [...]
#}
#Donde "mayores" contenga una lista ordenada con los nombres de las personas >= 18 y "menores" contenga una lista ordenada con los nombres de 
#las personas < 18.
edades = {
    "Ana": 22,
    "Luis": 17,
    "Pedro": 30,
    "Sofía": 16,
    "Carlos": 25
}
result_ages = {                                 #Creación del diccionario resultante.
    "menores": [],
    "mayores": []
}
for nombre, edad in edades.items():             
    if (edad <= 18):
        result_ages["menores"].append(nombre)   
    if (edad >= 18):
        result_ages["mayores"].append(nombre)   
print("7.-", result_ages, "\n")


#Ejercicio 8: Dado un diccionario donde la clave es el nombre de un alumno y el valor es una lista de materias aprobadas:
#materias = {
#    "Ana": ["Álgebra", "Cálculo", "Física"],
#    "Luis": ["Álgebra"],
#    "Sofía": ["Cálculo", "Física", "Programación", "Álgebra"],
#    "Pedro": []
#}
#Devuelve un diccionario nuevo donde la clave sea el nombre del alumno y el valor sea el número de materias aprobadas, excluyendo a los alumnos 
#que no aprobaron ninguna materia. Ejemplo esperado:
#{
#    "Ana": 3,
#    "Luis": 1,
#    "Sofía": 4
#}
materias = {
    "Ana": ["Álgebra", "Cálculo", "Física"],
    "Luis": ["Álgebra"],
    "Sofía": ["Cálculo", "Física", "Programación", "Álgebra"],
    "Pedro": []
}
alumnos_aprobados = {}
for nombre, lista_materias in materias.items():
    materias_aprobadas = len(lista_materias)
    if (materias_aprobadas > 0):
        alumnos_aprobados[nombre] = materias_aprobadas
print("8.-", alumnos_aprobados, "\n")


#Ejercicio 9: Se proporciona una estructura de datos que representa una memoria caché con capacidad fija, donde cache_data es un diccionario 
#cuyas claves y valores son cadenas de texto (str), esta caché debe comportarse como una LRU cache (Least Recently Used); la capacidad máxima 
#es de 10 elementos, donde el primer elemento representa el dato menos recientemente usado y el último elemento el más recientemente usado; 
#debemos implementar una función que cumpla las siguientes reglas: Si la key ya existe en la caché, debe devolver su valor y mover ese par 
#clave–valor a la última posición del diccionario (most recently used); si la key no existe y se proporciona un value, entonces se debe insertar 
#como el elemento más recientemente usado y, si la caché ya alcanzó su capacidad máxima, se debe eliminar primero el elemento menos 
#recientemente usado (el primero); si la key no existe y value es None, no se debe modificar la caché.
cache_data = {
    "1": "data1",
    "2": "data2",
    "3": "data3",
    "4": "data4",
    "5": "data5",
    "6": "data6",
    "7": "data7",
    "8": "data8",
    "9": "data9",
    "10": "data10"
}
new_data = ("4", "data11")
def insert_cache(new_data):
    cache_order = list(cache_data.keys())       #cache_order = ['1','2','3','4','5','6','7','8','9','10']
    CAPACITY = 10
    #new_data[0] = key; new_data[1] = value.
    if(new_data[0] in cache_order):             #Si la key de new_data ya existía, se actualiza su valor al nuevo y se mueve al final.
        #pop(): Método que sirve para borrar un elemento y retornar el índice del elemento que se eliminó si se utiliza en listas, pero 
        #cuando se usa en diccionarios, este recibe la key del elemento y retorna el valor eliminado.
        cache_data.pop(new_data[0])             #Se elimina su valor actual.
        cache_data[new_data[0]] = new_data[1]   #Se actualiza (agrega) el nuevo valor al key de new_data.
    else:                                       #Si la key es nueva, se agrega el nuevo valor y se actualiza la lista cache_order.
        if(len(cache_order) >= CAPACITY):       #Si además la memoria estaba llena, se elimina el primer elemento de cache_order y cache_data.
            #pop(): Método que elimina un elemento de un diccionario (key y value), para ello recibe su key y devuelve el value eliminado.
            least_used = cache_order.pop(0)
            cache_data.pop(least_used)
        cache_data[new_data[0]] = new_data[1]
        cache_order.append(new_data[0])
    print("9.-", cache_data, "\n")
insert_cache(new_data)
  

#Ejercicio 10: Dado un diccionario de 3 elementos donde la clave es el identificador del paciente, el segundo las notas del terapeuta y el 
#tercero es el score que sacó en la terapia, siendo un número de 0 a 100, saca el promedio del score de cada paciente y ordenalo de mayor a 
#menor en un diccionario final, que tenga por cada id, cual fue su promedio de score y lo ordene de mayor a menor, incluyendo al final, todas 
#una lista de las notas de su terapeuta:
#datos_pacientes = [
#    {"patient_id": "1", "therapy_notes": "ok", "score": 98},
#    {"patient_id": "1", "therapy_notes": "meh", "score": 20},
#    {"patient_id": "1", "therapy_notes": "good", "score": 30},
#    {"patient_id": "2", "therapy_notes": "ok", "score": 70},
#    {"patient_id": "2", "therapy_notes": "good", "score": 85},
#    {"patient_id": "2", "therapy_notes": "excellent", "score": 90},
#    {"patient_id": "3", "therapy_notes": "bad", "score": 40},
#    {"patient_id": "3", "therapy_notes": "ok", "score": 60},
#]
#Ejemplo esperado:
#{
#    "2": 81.6666, "therapy_notes": ["ok", "good", "excellent"],
#    "3": 50, "therapy_notes": ["bad", "ok"],
#    "1": 49.3333, "therapy_notes": ["ok", "meh", "good"]
#}
datos_pacientes = [
    {"patient_id": "1", "therapy_notes": "ok", "score": 98},
    {"patient_id": "1", "therapy_notes": "meh", "score": 20},
    {"patient_id": "1", "therapy_notes": "good", "score": 30},
    {"patient_id": "2", "therapy_notes": "ok", "score": 70},
    {"patient_id": "2", "therapy_notes": "good", "score": 85},
    {"patient_id": "2", "therapy_notes": "excellent", "score": 90},
    {"patient_id": "3", "therapy_notes": "bad", "score": 40},
    {"patient_id": "3", "therapy_notes": "ok", "score": 60},
]
def promedio_pacientes(datos_pacientes):
    pacientes = {}
    #Cuando en el JSON hay más de 2 elementos, todos se extraen en una misma variable llamada row o fila y luego se extrae individualmente su 
    #value por key.
    for fila in datos_pacientes:
        pid = fila["patient_id"]
        score = fila["score"]
        nota = fila["therapy_notes"]
        #Se crea manualmente el JSON interno de cada pacient_id si es que este no existe, si ya existe se va aumentando su score y se cuenta 
        #las veces que este haya aparecido, para luego sacar su promedio.
        if pid not in pacientes:
            pacientes[pid] = {
                "total_score": 0,
                "count": 0,
                "therapy_notes": []
            }
        pacientes[pid]["total_score"] += score
        pacientes[pid]["count"] += 1
        pacientes[pid]["therapy_notes"].append(nota)
    #Construimos resultado final con promedio
    resultado = {}
    for pid, info in pacientes.items():
        promedio = info["total_score"] / info["count"]
        resultado[pid] = {
            "average": promedio,
            "therapy_notes": info["therapy_notes"]
        }
    #sorted(iterable, key=..., reverse=...): Iterable se refiere a los elementos que se van a ordenar, la clave key indica que elemento se va a 
    #comparar para poder ordenarlo respecto a ese factor y el factor reverse indica el órden de acomodo, que normalmente su valor por default 
    #está como reverse = False, ordenando los valores de menor a mayor, pero si se quiere ordenar del mayor al menor se debe cambiar su valor a 
    #True.
    # - key: En esta parte debemos acceder al elemento que queremos comparar, para esto se suelen utilizar funciones lambda.
    #   - lambda: Es un tipo de función que no tiene nombre ni instrucción return, pero si parámetros y su sintaxis es la siguiente, donde en 
    #     vez de tener:
    #       def sumar(a, b):
    #           return a + b
    #     se tiene:
    #       lambda a, b: a + b
    #     En el caso de sorted, se utiliza una función lambda para acceder a un elemento del JSON, a través de cual se hará el acomodo. 
    resultado = dict(sorted(resultado.items(), key = lambda x: x[1]["average"], reverse = True))
    return resultado
print("10.-", promedio_pacientes(datos_pacientes), "\n")


#Ejercicio 11: Dado el siguiente listado de ventas, agrupa las ventas por seller_id, calculando el total vendido por vendedor y el número de 
#productos vendidos. Devuelve un diccionario ordenado de mayor a menor según el total vendido:
# El resultado debe verse así:
#{
#     "A2": {"total": 15300, "count": 2},
#     "A1": {"total": 19300, "count": 3},
#     "A3": {"total": 4800, "count": 2}
#}
ventas = [
    {"seller_id": "A1", "product": "Laptop", "amount": 15000},
    {"seller_id": "A2", "product": "Mouse", "amount": 300},
    {"seller_id": "A1", "product": "Monitor", "amount": 4000},
    {"seller_id": "A3", "product": "Teclado", "amount": 800},
    {"seller_id": "A2", "product": "Laptop", "amount": 15000},
    {"seller_id": "A3", "product": "Monitor", "amount": 4000},
    {"seller_id": "A1", "product": "Mouse", "amount": 300}
]
resultado = {}
for rows in ventas:
    sid = rows["seller_id"]
    sales = rows["amount"]
    product = rows["product"]
    if sid not in resultado:
        resultado[sid] = {
            "sales_amount": 0,
            "number_of_products": 0
        }
    resultado[sid]["sales_amount"] += sales
    resultado[sid]["number_of_products"] += 1
    resultado = dict(sorted(resultado.items(), key = lambda x: x[1]["sales_amount"], reverse = True))
print("11.-", resultado, "\n")


#Ejercicio 12: Dado un vector a, debemos generar un vector b de la misma longitud aplicando la siguiente transformación: 
# - Cada posición b[i] debe ser la suma del elemento actual a[i], el elemento anterior a[i-1] (si existe) y el elemento siguiente 
#   a[i+1] (si existe).
# - Si el elemento anterior no existe (cuando i == 0), no lo sumes.
# - Si el elemento siguiente no existe (cuando i es el último índice), no lo sumes.
# - La lista resultante debe tener exactamente la misma longitud que la original.
#En conclusión, para cada posición, suma el elemento y sus vecinos inmediatos; b[i] = izquierda + actual + derecha.
vector_a = [4, 0, 1, -2, 3]         #i = 0 → no hay izquierda → usar 0; i = último → no hay derecha → usar 0.
def vector_transformation(a):
    vector_b = []
    for i in range(0, len(a)):      #b[i] = izquierda + actual + derecha.
        posicion_b = a[i]           #b[i] = actual;                         Siempre existe el actual.
        if(i > 0):
            posicion_b += a[i - 1]  #b[i] = izquierda + actual;             i = 0 → no hay izquierda → usar 0.
        if(i < len(a) - 1):
            posicion_b += a[i + 1]  #b[i] = izquierda + actual + derecha;   i = len(a) = último → no hay derecha → usar 0.
        vector_b.append(posicion_b) #Para cada elemento del vector a, se crea la nueva posición del vector_b.
    return vector_b
print("12.-", vector_transformation(vector_a), "\n")


#Ejercicio 13 (Sliding window manual): Se nos dan dos strings; "pattern" que solo contiene caracteres '0' y '1' y "source" que contiene letras 
#minúsculas. El string pattern representa una regla donde: 
# - '0' significa que la letra debe ser una vocal; Las vocales son: a, e, i, o, u, y
# - '1' significa que la letra debe ser una consonante; Que son todas las letras no vocales.
#Debemos contar cuántas subcadenas consecutivas de source (del mismo tamaño que pattern) cumplen exactamente el patrón. Para ello debemos 
#recorrer source y extraer subcadenas del tamaño de pattern para compararlas carácter por carácter. Las subcadenas deben ser consecutivas y solo 
#se consideran subcadenas del mismo tamaño que pattern.
pattern = "010"         #0 = Vocal; 1 = Consonante; 1 = "010" = True;   2 = "010" = False;  3 = "010" = True;   4 = "010" = False;  5 = "010" = False.
source = "amazing"      #Subcadenas;                1 = "ama";          2 = "maz";          3 = "azi";          4 = "zin";          5 = "ing".
def subcadenas_vocales(pattern, source):
    vocales = {"a","e","i","o","u","y"}
    contador = 0
    for i in range(len(source) - len(pattern) + 1): #7-3+1 = 4+1 = 5 posibles subcadenas, recorriendo de 1 en 1 todas sus letras.
        cumple = True                               #Booleano, que suma 1 a 1 cuando las letras de la subcadena cumplan el patrón.
        for j in range(len(pattern)):               #Bucle que recorre los números del patrón para compararlos con las letras de las subcadenas.
            letra = source[i + j]                   #Bucle que avanza de 1 en 1 los caracteres de source, para crear las subcadenas.
            if(pattern[j] == "0"):
                if(letra not in vocales):           #Si el caracter del patrón es 0 pero la letra no es una vocal, cumple = False.
                    cumple = False
                    #- continue: Comando que interrumpe la iteración actual del condicional o bucle y salta inmediatamente a la siguiente 
                    #  vuelta, sin ejecutar el resto del código.
                    #- break: Comando que rompe completamente el condicional o bucle donde está contenido.
                    #- pass: Comando que no hace nada, sirve para cuando Python exige al menos una instrucción dentro del bloque.
                    break
            if(pattern[j] == "1" and letra in vocales): #Si el caracter del patrón es 1 pero la letra es una vocal, cumple = False.
                cumple = False
                break
        if(cumple == True):                         #Cada vez que la bandera cumple sea True, es porque la subcadena de source cumplió pattern.
            contador += 1                           #Y esto aumenta al contador.
    return contador
print("13.-", subcadenas_vocales(pattern, source), "\n")


#Ejercicio 14: Si una matriz field de tamaño 3x5 representa un tablero de Tetris, la cual solo contiene 0 y 1, indicando con 0 si una coordenada 
#se encuentra libre y con 1 si está ocupada. Debemos determinar en qué columnas y filas diferentes se puede dejar caer la figura de manera que, 
#después de caer completamente, se forme al menos una fila completamente llena de 1.
#Para ello, cada posición horizontal posible debe simular que la figura cae verticalmente hasta que toque el fondo o que toque otra pieza 
#existente en el tablero (un 1), una vez que la pieza se detiene debemos integrarla temporalmente al tablero, revisando si existe al menos una 
#fila completamente llena de 1. Contando si esa posición genera al menos una fila llena.
#Reglas importantes:
# 1.- Posiciones donde caer: No podemos salirnos de los límites del tablero.
# 2.- Simular caída: La figura no puede superponerse con 1 existentes (Revisar si hay choque y si es así, parar).
# 3.- Verificar fila llena: Una fila está llena si todos los valores son 1.
field = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [1, 0, 0],
         [1, 1, 0]]
figure = [[0, 0, 1],
         [0, 1, 1],
         [0, 0, 1]]
#tetris(): La tarea de la función es encontrar la posición de caída tal que se forme al menos una fila completa. Como posición de caída, debe 
#devolver el índice de la columna de la celda en el campo de juego que coincida con la fila superior de la matriz de la figura. Si hay varias 
#posiciones de caída que satisfacen la condición, se devolverá cualquiera de ellas. Si no hay tales posiciones de caída, se devolverá un -1.
def tetris(field, figure):
    height = len(field)
    width = len(field[0])           #Board_size = 5x3 = field[fila][columna]
    print("Tetris board:\t", height, "x", width)
    for fila in field:
        print(fila)
    figure_size = len(figure[0])    #Figure_size = nxn = 3x3.
    print("\nFigure:\t\t", figure_size, "x", figure_size)
    for fila in figure:
        print(fila)
    #1.- Posiciones donde caer: Para recorrer cada columna válida (eje x), debo restar el ancho del tablero menos el ancho de la figura + 1, así 
    #la figura no se sale del tablero.
    for column in range(width - figure_size + 1):   #En una matriz sus coordenadas son: matrix[fila][columna].
        #2.- Simular caída: Para ello la figura empieza a caer desde la fila de hasta arriba, contandola desde cero. 
        fila_actual = 0
        while(True):            #Bucle while controlado por la instrucción break, que nos sacaría cuando la pieza ya no pueda seguir bajando.
            puede_bajar = True  #Verificamos si puede bajar una fila más.
            for dx in range(figure_size):
                for dy in range(figure_size):       #las coordenadas dx y dy recorren todas las posiciones de la figura.
                    #Simulación de bajar, preguntándonos si la bajo una fila más, ¿chocará o no?, pero esta variable no se usa en la práctica, 
                    #en su lugar se utiliza el valor de la variable fila_actual.
                    nueva_fila = fila_actual + 1
                    #Verificar límites: Este condicional verifica que al bajar, la pieza no se salga del tablero. 
                    if(nueva_fila + dx >= height):  #nueva_fila + dy >= 5.
                        puede_bajar = False         #Si nueva_fila + dy es mayor a la altura del tablero, ya no se puede bajar más.
                        break
                    #Verificar choque: Observamos si en las coordenadas de la figura hay un 1 y también si las coordenadas actuales del tablero 
                    #hay un 1, comprobando que las piezas que ya habían en el tablero no vayan a chocar con la nueva que se está introduciendo.
                    if(figure[dx][dy] == 1 and field[nueva_fila + dx][column + dy] == 1):
                        #Si hay una pieza en la misma coordenada donde se quiere bajar la figura en el tablero, no se puede bajar más.
                        puede_bajar = False 
                        break
                #Si al realizar las verificaciones de límite y choque de la pieza en el tablero la bandera puede_bajar es False, se rompe la 
                #ejecución de los bucles dx y dy que recorren las coordenadas de la pieza y la intentan bajar.
                if(puede_bajar == False): 
                    break
            if puede_bajar: #Es igual a poner if(puede_bajar == True).
                fila_actual += 1                    #Si pasaron las pruebas de límite y choque, se puede bajar una fila más.
            else:
                break                               #Si la bandera puede_bajar == False, se rompe la ejecución del bucle while(True).
        #3.- Verificar fila llena: Una fila está llena si todos los valores son 1, para ello crearemos una copia del tablero.
        #Slicing [index_inicial:index_final_no_alcanzado]: Cuando se pone la instrucción [:] lo que se hace es acceder a todos los elementos 
        #de la lista, aquí lo que hace la expresión [fila[:] for fila in field] es acceder a todos los elementos de las filas de la matriz field
        #para crear una copia del tablero, esto porque queremos antes de modificarlo, ver si no rompe límites o choques de figuras.
        tablero_temp = [fila[:] for fila in field]
        #Colocar las piezas de la figura (unos 1), en su respectivo lugar en el tablero.
        for dx in range(figure_size):
            for dy in range(figure_size):           #las coordenadas dx y dy recorren todas las posiciones de la figura.
                #Si la figura tiene una pieza en una de sus coordenadas...
                if(figure[dx][dy] == 1):            
                    tablero_temp[fila_actual + dx][column + dy] = 1 #...Se coloca dicha pieza en la copia del tablero.
        #Verificar si alguna fila está llena: Para ello recorro todas las listas en la lista del tablero.
        for fila in tablero_temp:   #for elemento in lista: Recorre todos los elementos de una lista, pero esta es una lista de listas.
            #all(): Método que devuelve True si todos los elementos de su iterable interno son verdaderos y False si al menos uno es Falso.
            #Generator expression: Es un bucle que evalúa o convierte los elementos de un iterable, recorriéndolos uno por uno con la sintaxis:
            #   - condicion             for     variable_local      in      lista_tupla_diccionario_o_conjunto
            #   - transformacion_datos  for     variable_local      in      lista_tupla_diccionario_o_conjunto
            if all(valor == 1 for valor in fila):
                return column       #Si todos los elementos de la fila son 1, devuelve la coordenada de la columna de dicha fila.
    return -1                       #Si todos los elementos de la fila NO son 1, devuelve un -1.
print("14.-", tetris(field, figure), "\n")


#Ejercicio 15: Para cada valor n que se reciba, se debe crear un cuadrado con la siguiente forma, dependiendo del número de n, donde por 
#ejemplo para n = 3:
#resultado = ["***",
#             "* *",
#             "***"]



#Ejercicio 16: Dado un arreglo de enteros únicos numbers, debemos encontrar el número de pares de índices (i,j) donde: (i ≤ j) y la suma 
#numbers[i] + numbers[j] sea igual a alguna potencia de 2.
# - numbers[i] + numbers[j] sea una potencia de 2, para ello se permiten: 
#   - Pares donde i == j
#   - Se cuentan todos los pares válidos.
#La suma debe ser exactamente una potencia de 2, como por ejemplo:
#1, 2, 4, 8, 16, 32, 64, ...
#Contar pares cuya suma sea potencia de 2.



#Ejercicio 17:
# block_list = [("R","A"),("A","B"),("B","Y"),("A","B")]
# text = "BABY"
# letters_in_block = None
# for block in block_list:                    #1: (R,A);                          2:(R,A);
#     for letter in text:                     #1: 'B'                             2: 'A'
#         if(block[0] == letter):              #1: block[0] = R; letter = 'B'      2:break
#             text.remove(block[0])
#             break
#         elif(block[1] == letter):            #1: block[1] = A; letter = 'B'      2: block[1] = A; letter = 'A'
#             text.remove(block[0])
#             break
#         else:
#             break
#     if(text!=None):
#         letters_in_block = "no"
#     else:
#         letters_in_block = "yes"


#18.- Have the function PreorderTraversal(strArr) take the array of strings stored in strArr, which will represent a binary tree with 
#integer values in a format similar to how a binary heap is implemented with NULL nodes at any level represented with a #. Your goal is 
#to return the pre-order traversal of the tree with the elements separated by a space. For example, if strArr is: 
#["5", "2", "6", "1", "9", "#", "8", "#", "#", "#", "#", "#", "#", "4", "#"] then this tree looks like the following tree:
#For the input above, your program should return the string 5 2 1 9 6 8 4 because that is the pre-order traversal of the tree.



#19.- 
items = [
    {"category": "books", "value": 1},
    {"category": "electronics", "value": 2},
    {"category": "clothing", "value": 3},
    {"category": "food", "value": 4},
    {"category": "toys", "value": 5},
 
    {"category": "books", "value": 6},
    {"category": "electronics", "value": 7},
    {"category": "clothing", "value": 8},
    {"category": "food", "value": 9},
    {"category": "toys", "value": 10},
 
    {"category": "books", "value": 11},
    {"category": "electronics", "value": 12},
    {"category": "clothing", "value": 13},
    {"category": "food", "value": 14},
    {"category": "toys", "value": 15},
 
    {"category": "books", "value": 16},
    {"category": "electronics", "value": 17},
    {"category": "clothing", "value": 18},
    {"category": "food", "value": 19},
    {"category": "toys", "value": 20},
 
    {"category": "books", "value": 21},
    {"category": "electronics", "value": 22},
    {"category": "clothing", "value": 23},
    {"category": "food", "value": 24},
    {"category": "toys", "value": 25},
 
    {"category": "books", "value": 26},
    {"category": "electronics", "value": 27},
    {"category": "clothing", "value": 28},
    {"category": "food", "value": 29},
    {"category": "toys", "value": 30},
 
    {"category": "books", "value": 31},
    {"category": "electronics", "value": 32},
    {"category": "clothing", "value": 33},
    {"category": "food", "value": 34},
    {"category": "toys", "value": 35},
 
    {"category": "books", "value": 36},
    {"category": "electronics", "value": 37},
    {"category": "clothing", "value": 38},
    {"category": "food", "value": 39},
    {"category": "toys", "value": 40},
 
    {"category": "books", "value": 41},
    {"category": "electronics", "value": 42},
    {"category": "clothing", "value": 43},
    {"category": "food", "value": 44},
    {"category": "toys", "value": 45},
 
    {"category": "books", "value": 46},
    {"category": "electronics", "value": 47},
    {"category": "clothing", "value": 48},
    {"category": "food", "value": 49},
    {"category": "toys", "value": 50},
 
    {"category": "books", "value": 51},
    {"category": "electronics", "value": 52},
    {"category": "clothing", "value": 53},
    {"category": "food", "value": 54},
    {"category": "toys", "value": 55},
 
    {"category": "books", "value": 56},
    {"category": "electronics", "value": 57},
    {"category": "clothing", "value": 58},
    {"category": "food", "value": 59},
    {"category": "toys", "value": 60},
 
    {"category": "books", "value": 61},
    {"category": "electronics", "value": 62},
    {"category": "clothing", "value": 63},
    {"category": "food", "value": 64},
    {"category": "toys", "value": 65},
 
    {"category": "books", "value": 66},
    {"category": "electronics", "value": 67},
    {"category": "clothing", "value": 68},
    {"category": "food", "value": 69},
    {"category": "toys", "value": 70},
 
    {"category": "books", "value": 71},
    {"category": "electronics", "value": 72},
    {"category": "clothing", "value": 73},
    {"category": "food", "value": 74},
    {"category": "toys", "value": 75},
 
    {"category": "books", "value": 76},
    {"category": "electronics", "value": 77},
    {"category": "clothing", "value": 78},
    {"category": "food", "value": 79},
    {"category": "toys", "value": 80},
 
    {"category": "books", "value": 81},
    {"category": "electronics", "value": 82},
    {"category": "clothing", "value": 83},
    {"category": "food", "value": 84},
    {"category": "toys", "value": 85},
 
    {"category": "books", "value": 86},
    {"category": "electronics", "value": 87},
    {"category": "clothing", "value": 88},
    {"category": "food", "value": 89},
    {"category": "toys", "value": 90},
 
    {"category": "books", "value": 91},
    {"category": "electronics", "value": 92},
    {"category": "clothing", "value": 93},
    {"category": "food", "value": 94},
    {"category": "toys", "value": 95},
 
    {"category": "books", "value": 96},
    {"category": "electronics", "value": 97},
    {"category": "clothing", "value": 98},
    {"category": "food", "value": 99},
    {"category": "toys", "value": 100},
 
    {"category": "books", "value": 101},
    {"category": "electronics", "value": 102},
    {"category": "clothing", "value": 103},
    {"category": "food", "value": 104},
    {"category": "toys", "value": 105},
 
    {"category": "books", "value": 106},
    {"category": "electronics", "value": 107},
    {"category": "clothing", "value": 108},
    {"category": "food", "value": 109},
    {"category": "toys", "value": 110},
 
    {"category": "books", "value": 111},
    {"category": "electronics", "value": 112},
    {"category": "clothing", "value": 113},
    {"category": "food", "value": 114},
    {"category": "toys", "value": 115},
 
    {"category": "books", "value": 116},
    {"category": "electronics", "value": 117},
    {"category": "clothing", "value": 118},
    {"category": "food", "value": 119},
    {"category": "toys", "value": 120},
 
    {"category": "books", "value": 121},
    {"category": "electronics", "value": 122},
    {"category": "clothing", "value": 123},
    {"category": "food", "value": 124},
    {"category": "toys", "value": 125},
 
    {"category": "books", "value": 126},
    {"category": "electronics", "value": 127},
    {"category": "clothing", "value": 128},
    {"category": "food", "value": 129},
    {"category": "toys", "value": 130},
 
    {"category": "books", "value": 131},
    {"category": "electronics", "value": 132},
    {"category": "clothing", "value": 133},
    {"category": "food", "value": 134},
    {"category": "toys", "value": 135},
 
    {"category": "books", "value": 136},
    {"category": "electronics", "value": 137},
    {"category": "clothing", "value": 138},
    {"category": "food", "value": 139},
    {"category": "toys", "value": 140},
 
    {"category": "books", "value": 141},
    {"category": "electronics", "value": 142},
    {"category": "clothing", "value": 143},
    {"category": "food", "value": 144},
    {"category": "toys", "value": 145},
 
    {"category": "books", "value": 146},
    {"category": "electronics", "value": 147},
    {"category": "clothing", "value": 148},
    {"category": "food", "value": 149},
    {"category": "toys", "value": 150},
]
categories = []
values = []

for i in items:
    categories.append(i["category"])
    mylist = list(dict.fromkeys(categories))
    for j in items:
        values.append(j["value"])

print(mylist)

#Ejercicio 20: Find the number of times that each dev_ids appear on the list and create a function that returns the highest 2 devs.
# with k=2
# the result is [1, 4]
dev_ids = [1,3,4,5,4,5,5,4,6,1,1,1,2,1,2,7,8,9,4,5,4,6,2]
#devs = [1,2,3,4,5,6,7]
#concurrency = [0,2,3,4,3,4,5,3,5,0,0,0,2,0,2,6,8,9,3,4,3,5,2]

def get_top_devs(dev_ids, k):
    k+=1
    concurrency = []
    devs = list(set(sorted(dev_ids)))
    counter = 0
    dev_concurrency = []
    for i in dev_ids:
        for j in devs:
            if (dev_ids[i] == devs[j]):
                counter+=1
                print(counter)
            else:
                break
        concurrency.append(counter)
    dev_concurrency = list(zip(concurrency, devs))
    print(dev_concurrency)

get_top_devs(dev_ids, 2)


"""
===========================================================
Ejercicio 21: Reverse String + ChallengeToken Transformation
===========================================================

Problem:
- Reverse the input string
- Concatenate the ChallengeToken
- Replace every 3rd character with 'X'

Example:
Input:  "coderbyte"
Reverse: "etybredoc"
Final:   "etXbrXdoXc2Xu7X9"
"""

def StringChallenge_Reverse(strParam):
    challenge_token = "c2xu739"

    # Step 1: reverse the string
    reversed_str = strParam[::-1]

    # Step 2: concatenate the challenge token
    combined = reversed_str + challenge_token

    # Step 3: replace every 3rd character with 'X'
    final_output = ""
    for i, ch in enumerate(combined, start=1):
        if i % 3 == 0:
            final_output += "X"
        else:
            final_output += ch

    return final_output


# ---- Ejercicio 1 ----
print(StringChallenge_Reverse("coderbyte"))
print(StringChallenge_Reverse("I Love Code"))


"""
===========================================================
Ejercicio 22: String Rearrangement (Anagram Check)
===========================================================

Problem:
- Return "true" if characters from str1 can be rearranged
  to form str2 (using only a portion if needed)
- Otherwise return "false"

Example:
Input:  str1 = "cdore", str2 = "coder"
Output: "true"
"""

def StringChallenge_Rearrange(str1, str2):
    # Dictionary to count characters in str1
    char_count = {}

    for ch in str1:
        char_count[ch] = char_count.get(ch, 0) + 1

    # Check if str2 can be formed
    for ch in str2:
        if ch not in char_count or char_count[ch] == 0:
            return "false"
        char_count[ch] -= 1

    return "true"

# ---- Ejercicio 2 ----
print(StringChallenge_Rearrange("cdore", "coder"))
print(StringChallenge_Rearrange("h3llko", "hello"))


"""
===========================================================
Ejercicio 23: Public S3 Bucket File Finder + Token Processing
===========================================================

Problem:
- Access a public S3 bucket
- Find the file that starts with "__cb__"
- Append ChallengeToken
- Replace every 3rd character with 'X'
"""

import boto3
from botocore import UNSIGNED
from botocore.client import Config

def S3_Challenge():
    bucket_name = "coderbytechallengesandbox"
    challenge_token = "c2xu739"
    file_prefix = "__cb__"

    # Create anonymous S3 client
    s3 = boto3.client(
        "s3",
        config=Config(signature_version=UNSIGNED)
    )

    response = s3.list_objects_v2(Bucket=bucket_name)

    cb_file = ""
    for obj in response.get("Contents", []):
        if obj["Key"].startswith(file_prefix):
            cb_file = obj["Key"]
            break

    combined = cb_file + challenge_token

    # Replace every 3rd character with 'X'
    final_output = ""
    for i, ch in enumerate(combined, start=1):
        if i % 3 == 0:
            final_output += "X"
        else:
            final_output += ch

    return final_output


"""
===========================================================
MANUAL TESTING SECTION
(Uncomment what you want to test)
===========================================================
"""

# ---- Ejercicio 3 ----
print(S3_Challenge())


#HASH AND PERFORMANCE ALGORITHMS
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

#Investigar Memoria Caché.