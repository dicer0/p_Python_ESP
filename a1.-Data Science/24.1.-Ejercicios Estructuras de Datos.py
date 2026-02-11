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
            #continue: Comando que interrumpe la iteración actual del condicional o bucle y salta inmediatamente a la siguiente vuelta, sin 
            #ejecutar el resto del código.
            #break: Comando que rompe completamente el condicional o bucle, no solo la iteración actual.
            #pass: Comando que no hace nada, sirve para cuando Python exige al menos una instrucción dentro del bloque.
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
def nums_pares(numeros):
    datos_ord = sorted(numeros)
    resultado = []
    #Operador de módulo (%): Calcula el resto de una división entera entre dos números, siendo una herramienta fundamental para determinar 
    #divisibilidad, alternar acciones (pares/impares) o limitar rangos de valores, su sintaxis es: 
    #       divisor/dividendo = cociente
    #       divisor%dividendo = resultado_operador_modulo;  7/2 = 3, con cociente = 1, por lo tanto 7%2 = 1, esto indica que 7 es impar.
    for i in datos_ord:
        if(i%2 == 1):
            #continue: Comando que interrumpe la iteración actual del condicional o bucle y salta inmediatamente a la siguiente vuelta, sin 
            #ejecutar el resto del código.
            #break: Comando que rompe completamente el condicional o bucle, no solo la iteración actual.
            #pass: Comando que no hace nada, sirve para cuando Python exige al menos una instrucción dentro del bloque.
            break
        else:
            resultado.append(i)
    return resultado
print("5.-", nums_pares(numeros), "\n")


#Ejercicio 6: Dado un diccionario donde la clave es el nombre de un producto y el valor es otro diccionario con su información, Devuelve un 
#diccionario ordenado alfabéticamente con los nombres de los productos que: Tengan stock mayor a 0 y cuyo precio sea mayor o igual a 1000.
productos = {
    "Laptop": {"precio": 15000, "stock": 5},
    "Mouse": {"precio": 300, "stock": 0},
    "Teclado": {"precio": 800, "stock": 12},
    "Monitor": {"precio": 4000, "stock": 3}
}
result_product = {}
def diccionario_productos(productos):
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
    print("6.-", sorted(result_product), "\n")
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
#Devuelve un diccionario nuevo donde la clave sea el nombre del alumno, el valor sea el número de materias aprobadas, excluyendo a los alumnos 
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
    if(new_data[0] in cache_data):              #Si la key de data ya existía en la memoria, se actualiza y se remueve el último elemento.
        cache_data[new_data[0]] = new_data[1]
        #remove(): Método que sirve para borrar un elemento y no retorna nada.
        cache_order.remove(new_data[0])
        cache_order.append(new_data[0])
    else:                                       #Si la key de data es nueva y la memoria estaba llena.
        if(len(cache_order) >= CAPACITY):
            #pop(): Método que sirve para borrar un elemento y retornar el índice del elemento que eliminó.
            least_used = cache_order.pop(0)
            cache_data.pop(least_used)
        cache_data[new_data[0]] = new_data[1]
        cache_order.append(new_data[0])
    print("9.-", cache_data, "\n")
insert_cache(new_data)
    

#Ejercicio 10: Dado un diccionario donde la clave es el nombre de un alumno y el valor es una lista de materias aprobadas:
#materias = {
#    "Ana": ["Álgebra", "Cálculo", "Física"],
#    "Luis": ["Álgebra"],
#    "Sofía": ["Cálculo", "Física", "Programación", "Álgebra"],
#    "Pedro": []
#}
#Devuelve un diccionario nuevo donde la clave sea el nombre del alumno, el valor sea el número de materias aprobadas, excluyendo a los alumnos 
#que no aprobaron ninguna materia. Ejemplo esperado:
#{
#    "Ana": 3,
#    "Luis": 1,
#    "Sofía": 4
#}
datos = [
    {"patient_id": "1", "therapy_notes": "ok", "score": 98},
    {"patient_id": "1", "therapy_notes": "meh", "score": 20},
    {"patient_id": "1", "therapy_notes": "good", "score": 30},
    {"patient_id": "2", "therapy_notes": "ok", "score": 70},
    {"patient_id": "2", "therapy_notes": "good", "score": 85},
    {"patient_id": "2", "therapy_notes": "excellent", "score": 90},
    {"patient_id": "3", "therapy_notes": "bad", "score": 40},
    {"patient_id": "3", "therapy_notes": "ok", "score": 60},
]
scores_por_paciente = {}
for fila in datos:
    pid = fila["patient_id"]
    score = fila["score"]
    if pid not in scores_por_paciente:
        scores_por_paciente[pid] = []
    scores_por_paciente[pid].append(score)
print("10.-", scores_por_paciente, "\n")


#Ejercicio 10:


#11.-
import re
def texttonum(input):
    nums = re.findall(r'\d+', input)
    # Source - https://stackoverflow.com/a
    # Posted by cheeken, modified by community. See post 'Timeline' for change history
    # Retrieved 2025-12-22, License - CC BY-SA 4.0
    nums = list(map(int, nums))
    print(nums, "sum:", sum(nums))
    return nums
usefun = texttonum("105 test4more 35k2 0292 AVVC")

#10.- 
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

#Ejercicio 12: Find the number of times that each dev_ids appear on the list and create a function that returns the highest 2 devs.
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
Ejercicio 13: Reverse String + ChallengeToken Transformation
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
Ejercicio 14: String Rearrangement (Anagram Check)
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
Ejercicio 15: Public S3 Bucket File Finder + Token Processing
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