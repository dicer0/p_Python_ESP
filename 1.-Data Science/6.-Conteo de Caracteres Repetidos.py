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

#CÓDIGO PARA VER LA FRECUENCIA DE LETRAS QUE EXISTEN EN UNA SOLA PALABRA:
#STRING SLICING: Es el proceso de extraer y separar todas las letras de un string, indicando sus coordenadas. 
st = "google.com" #Palabra de ejemplo a analizar


#PROCESO:
#1.- CONTAR EL NÚMERO TOTAL DE CARACTERES.
#len(): El método len() sirve para calcular el tamaño de una cadena de caracteres, lista o array
stLenght = len(st)
#Variable auxiliar que guarda cada caracter de forma individual para 
lastChar = ""
#Vector con una longitud igual al número de caracteres de la palabra de ejemplo, donde se guardan los índices en 
#donde por primera vez apareció un carácter en la palabra analizada.
chIndex = [] 
#Los índices positivos lo que hacen es ir de derecha a izquierda
#a = st[0]
#print(a)
#Los índices negativos lo que hacen es ir de izquierda a derecha
#b = st[-3]
#print(b)


#2.- IDENTIFICAR LOS ÍNDICES DE LOS CARACTERES QUE SE REPITEN. POR EJEMPLO, en google.com SE TIENEN 9 CARACTERES, 
#DONDE EL ÍNDICE 0 CORRESPONDE A LA LETRA g, EL ÍNDICE 1 A LA PRIMERA LETRA o Y ASÍ SUCESIVAMENTE HASTA EL ÍNDICE 9 
#QUE CORRESPONDE A LA LETRA m. ENTONCES EL VECTOR CON LOS ÍNDICES DE LOS CARACTERES QUE SE REPITEN QUEDA COMO 
#[0, 1, 1, 0, 4, 5, 6, 7, 1, 9], DONDE EL 0 CORRESPONDE A LA LETRA g (la cual aparece dos veces), EL 1 CORRESPONDE A 
#LA LETRA o, QUE APARECE TRES VECES, EL ÍNDICE 4 CORRESPONDE A LA LETRA 1 Y ASÍ SUCESIVAMENTE. ESTO SE REALIZA A 
#TRAVÉS DE DOS BUCLES FOR ANIDADOS DONDE SE COMPARAN LAS LETRAS UNA A UNA CON TODAS LAS LETRAS DEL STRING Y EL ÍNDICE 
#GUARDADO EN EL VECTOR ES EL DE LA PRIMERA VEZ DONDE APARECIÓ LA LETRA ANALIZADA.
#Bucle for con rango definido: Cuando en un bucle for se ponen dentro del paréntesis del range un primer y segundo 
#valor separados por comas, se le está indicando al bucle de qué valor a que valor va a contar para repetir la 
#ejecución del bucle.
for i in range(0, stLenght):
    #Guarda de uno en uno los caracteres correspondientes a los índices de 0 hasta el tamaño de la palabra de ejemplo.
    lastChar = st[i]
    #En el bucle for anidado se recorre caracter a caracter el string. Si st[i] = st[j], osea que la letra identificada 
    #en el primer bucle for sea igual a la reconocida en el segundo bucle for, se rompe el ciclo anidado for con 
    #índice j y se guarda el valor numérico del índice j en el vector chIndex, pasando así a analizar el siguiente 
    #caracter de st.
    for j in range(0, stLenght):
        if(lastChar == st[j]): #st[i] = st[j], osea que la letra analizada en el primer y segundo for sean iguales
            chIndex.append(j) #append(): El método append() sirve para agregar valores a una lista, array o diccionario
            break #Se rompe el ciclo anidado for con índice j

print("1 y 2.- Los índices de los caracteres que se repiten en el string son: \n", chIndex)


#3.- REORDENAR EL VECTOR GENERADO EN EL PROCESO 2 DE VALOR MENOR A MAYOR POR MEDIO DE LA FUNCIÓN SORT.
#sort(): El método sort() sirve para ordenar de menor a mayor los elementos numéricos de una lista o diccionario.
chIndexSort = sorted(chIndex)
print("3.- Los índices de los caracteres que se repiten ordenados de mayor a menor son: \n", chIndexSort)


#4.- GENERAR UN NUEVO VECTOR QUE ELIMINA LOS ÍNDICES REPETIDOS, ESTO PARA PODER AL FINAL ASOCIAR A CADA LETRA DE LA 
#PALABRA ANALIZADA LA FRECUENCIA CON LA QUE APARECE EN LA PALABRA.
index = 0
#Vector donde se guardan los índices no repetidos de la lista chIndexSort.
chNewIndex = []
#Se agrega el primer elemento de la lista chIndexSort que contiene los índices ordenados de menor a mayor a la lista 
#chNewIndex que incluye los mismos índices pero sin que estos se repitan.
chNewIndex.append(chIndexSort[0])
#Bucle for exterior: En este se recorre toda la palabra inicial y se crean dos variables auxiliares:
#hold: Variable auxiliar para analizar individualmente cada valor de la lista chIndexSort y compararlo con todos sus 
#demás valores.   
#comp: Variable auxiliar para empezar el segundo bucle for anidado desde donde no se haya encontrado valores repetidos.
#Recordemos que el tamaño de la palabra original, el vector chIndex y chIndexSort es el mismo ya que en él se analizaron 
#los índices de todas las letras de la palabra donde se repitiera cada letra.
for i in range(0, stLenght): #stLenght = len(st) = len(chIndex) = len(chIndexSort)
    hold = chIndexSort[index] #Variable que guarda uno a uno los valores contenidos en la lista chIndexSort.
    comp = index #Variable que guarda el índice de la lista chIndexSort donde no se encontraron valores repetidos.
    #Bucle for anidado: En este se recorre toda la palabra inicial, partiendo desde el índice guardado en la variable 
    #comp, que cambia de valor cuando no encuentra valores repetidos en la lista chIndexSort.
    for j in range(comp, stLenght):
        #En el bucle anidado solo se ejecuta algo cuando el valor del 
        if(hold != chIndexSort[j]):
            #Cambio de valor de la variable index y comp por el índice donde no se encontró valores repetidos
            index = j #index = comp = j, cuando el valor actual de la lista es distinto al que le sigue
            #Cuando no se repiten valores en la lista chIndexSort se agregan a la lista chNewIndex y se sale del 
            #bucle for anidado j
            chNewIndex.append(chIndexSort[j])
            break

print("4.- Los índices de los caracteres que se repiten ordenados de mayor a menor y sin índices repetidos son: \n", chNewIndex)


#5.- DETERMINAR LA FRECUENCIA DE CADA UNO DE LOS CARACTERES, EN BASE AL VECTOR CREADO EN EL PROCESO 4.
freq = [] #Vector donde se guarda la frecuencia de cada letra analizada perteneciente a la palabra original.
#Bucle for exterior: Este parte de 0 hasta el tamaño de la lista chNewIndex, que contiene todos los índices no repetidos 
#y ordenados de menor a mayor de la lista que indica la posición en donde por primera vez apareció un carácter en la 
#palabra analizada, en este se crea una variable auxiliar que indicará la frecuencia con la que aparece cada letra en 
#la palabra original.
#stLenght != len(chNewIndex)
for i in range(0, len(chNewIndex)):
    #Variable auxiliar que indica la frecuencia de cada letra, esto se logra comparando los valores de los vectores 
    #chNewIndex y chIndexSort, ya que cada vez que un valor de la lista chNewIndex sea igual a un valor la lista 
    #chIndexSort es porque la letra aparece una vez en la palabra original.
    sumFreq = 0
    #Bucle anidado: En este se compara cada índice de la lista chNewIndex con cada índice de la lista chIndexSort, cada 
    #vez que sean iguales los valores, se le sumará un 1 a la variable sumFreq para saber la frecuencia de esa letra en 
    #específico, al ya no cumplirse esa condición, el programa se saldrá del bucle anidado y agregará un valor a la lista 
    #freq, el segundo bucle for parte desde 0 hasta el tamaño de la palabra original porque: 
    #stLenght = len(st) = len(chIndex) = len(chIndexSort)
    for j in range(0, stLenght):
        #Comparación de los índices de la lista chIndexSort y chNewIndex para saber la frecuencia de cada letra.
        if(chIndexSort[j] == chNewIndex[i]):
            sumFreq += 1 #Se suma un 1 a la variable sumFreq cada que sea igual un índice de ambas listas
    freq.append(sumFreq) #append(): El método append() sirve para agregar valores a una lista, array o diccionario.

print("5.- Las frecuencias de las letras que se repiten en la palabra son: \n", freq)


#6.- IMPRIMIR EN CONSOLA LOS CARACTERES SIN QUE SE REPITAN Y SU FRECUENCIA, ADEMÁS DE ASOCIARLOS TODOS DENTRO DE UN 
#DICCIONARIO.
freq_caract = {} #Diccionario que contiene cada letra de la palabra junto con la frecuencia con la que aparece.
letras = [] #Vector donde se guardarán las letras de los índices no repetidos de la palabra original.

#Bucle for para crear la lista letras que contiene todas las letras no repetidas en la palabra
for i in range(0, len(chNewIndex)):
    letras.append(st[chNewIndex[i]])

#zip(): El método lo que hace es crear un tipo de dato llamado tupla, una tupla es un conjunto de datos del mismo o 
#diferente tipo, si se quisiera .
tupla = zip(letras, freq)
#tuple(): El método crea un objeto tuple para que se le puedan aplicar los métodos correspondientes o en este caso se 
#pueda imprimir en consola
lista2D = tuple(tupla)
print("6.- Tupla: ", lista2D)
#Convertir dos listas en un diccionario Python: Python tiene una función incorporada llamada zip(), que agrega tipos de 
#datos iterables en una tupla y la función dict() crea un diccionario a partir de la colección dada, para lograr esto se 
#debe realizar todo en una misma línea de código o usar el método tuple como paso intermedio.
freq_caract = dict(lista2D) # = freq_caract = dict(zip(letras, freq))
print("6.- Diccionario: ",freq_caract)

#Imprimir en consola el key y value de un diccionario
#Operación para imprimir de una por una las ciudades del diccionario
for letra in freq_caract:
    print("6.- Letra: ", letra , ", Frecuencia: ", freq_caract[letra])