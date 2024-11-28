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

#POO: La programación orientada a objetos es una forma de estructurar programas y aplicaciones de tal forma que 
#los datos y las operaciones con estos se agrupan en clases para que se puedan acceder a estos por medio de 
#objetos.
#3.-Polynomial: Clase que sirve para crear ecuaciones polinomiales, evaluar su resultado si se sustituye el valor 
#de x por un entero, sumar, multiplicar, derivar polinomios e imprimir su resultado en consola.

#DECLARACIÓN DE LA CLASE POLYNOMIAL:
class Polynomial:
    #CONSTRUCTOR O INICIALIZADOR DE LA CLASE: En él se declaran los atributos que se reutilizarán en los demás 
    #métodos y que además, deben a fuerza de tener un valor.
    def __init__(self, coefficients): 
    #El parámetro del constructor de la clase son los coeficientes, que se ingresan en forma de vector.
        #self es distinto a this, por eso no debe tener el mismo nombre que el parámetro que está recibiendo el
        #constructor, se puede renombrar la variable que llega a la clase por medio del constructor.
        #self lo que hace es referenciar métodos o datos de la clase donde nos encontramos, es una referencia 
        #a lo que sea que pertenezca a esta clase. 
        #El parámetro coefficients deberá ser una lista (vector), sino arrojará un error el programa.
        self.coeff = coefficients
        #Un polinomio es descrito como: p(x) = a0 + a1*x + a2*x^2 + a3*x^3 + ... + an*x^n, donde los 
        #coeficientes del polinomio son: a0, a1, a2, a3, ..., an.
        #Por ejemplo, el polinomio: p(x) = 1-x^2+2x^3, tiene como coeficientes el vector: [1, 0, -1, 2]
    
    

    #EVALUAR EL RESULTADO SI SE SUSTITUYE EL VALOR DE X POR UN VALOR ENTERO: A través del método call se evalúa 
    #un polinomio sustituyendo su variable x por un valor numérico.
    #MÉTODO CALL: Este método es propio del lenguaje de programación Python y para utilizarze se declarar el 
    #nombre del objeto y sus parámetros, a diferencia de los demás donde se declara el nombre del objeto más el 
    #nombre del método:
    # - ObjetoClase(parámetro1, parámetro2, ..., parámetro_n)                       Método call
    # - ObjetoClase.NombreMétodo(parámetro1, parámetro2, ..., parámetro_n)          Método cualquiera
    #Solo puede existir un método call por clase y este trabaja con los atributos del constructor y puede 
    #incluir otros.
    def __call__(self, x):
        #Variable temporal que evalúa cada una de las multiplicaciones de los coeficientes del polinomio con la 
        #variable x (que ahora tiene un valor numérico).
        sigma = 0
        for i in range(len(self.coeff)):
            sigma = sigma + self.coeff[i]*x**i
        return sigma
    


    #SOBRECARGANDO LOS OPERADORES: Esto se refiere a asignar un método a los símbolos de suma, resta, 
    #multiplicación, etc. para realizar en este caso operaciones matemáticas con los polinomios, esto se realiza 
    #a través de los siguientes nombres de métodos:
    # - __add__: Corresponde al símbolo +
    # - __sub__: Corresponde al símbolo -
    # - __mul__: Corresponde al símbolo *
    # - __str__: Corresponde a cuando se usa el método print() o str()

    #MÉTODO __ADD__: Método para sumar polinomios.
    def __add__(self, other):
        #Si el primer polinomio en la suma es mayor en tamaño que el segundo, entonces ese es el que se debe 
        #asignar a la variable result_coeff, ya que en el bucle for que se incluye dentro, se recorrerán solo 
        #los coeficientes del polinomio menor para realizar la operación, así dejando sin tocar a los polinomios 
        #de mayor grado.
        if(len(self.coeff) > len(other.coeff)):             #Polinomio_1 > Polinomio_2
            #[:]: Recordemos que el valor de coeff es una lista, con la instrucción [indice_inicio:indice_final], 
            #se puede crear una copia de estos elementos y asignarlos a otra variable, obteniendo así un 
            #subconjunto de la lista, pero si a esta instrucción no se indica un índice de inicio y final, se 
            #copian todos los elementos.
            result_coeff = self.coeff[:]                    #result_coeff = Polinomio_1
            #Bucle que recorre los elementos del polinomio de menor tamaño y los suma con los elementos del 
            #polinomio de mayor grado.
            for i in range(len(other.coeff)):
                result_coeff[i] += other.coeff[i]           #result_coeff = Polinomio_1 + Polinomio_2
        #Si el primero polinomio en la suma es de menor tamaño que el segundo, entonces ese es el que se 
        #asigna a la variable result_coeff, ya que en el bucle for que se incluye dentro, se recorrerán solo los 
        #coeficientes del polinomio menor para realizar la operación, así dejando sin tocar a los polinomios de 
        #mayor grado.
        else:                                               #Polinomio_2 > Polinomio_1
            result_coeff = other.coeff[:]                   #result_coeff = Polinomio_2
            #Bucle que recorre los elementos del polinomio de menor tamaño y los suma con los elementos del 
            #polinomio de mayor grado.
            for i in range(len(self.coeff)):
                result_coeff[i] += self.coeff[i]            #result_coeff = Polinomio_2 + Polinomio_1
        return Polynomial(result_coeff)
    


    #MÉTODO __SUB__: Método para restar polinomios.
    def __sub__(self, other):
        #[:]: Recordemos que el valor de coeff es una lista, con la instrucción [indice_inicio:indice_final], 
        #se puede crear una copia de estos elementos y asignarlos a otra variable, obteniendo así un subconjunto 
        #de la lista, pero si a esta instrucción no se indica un índice de inicio y final, se copian todos los 
        #elementos.
        result_coeff = self.coeff[:]                        #result_coeff = Polinomio_1
    
        #Condicional que ajusta la longitud de la lista de coeficientes del segundo polinomio agregando ceros al 
        #final si es necesario cuando este es de menor tamaño, osea de menor grado, esto para que ambos 
        #polinomios tengan la misma cantidad de términos para poder restar los coeficientes correctamente en el 
        #siguiente bucle for.
        if len(other.coeff) < len(result_coeff):            #Polinomio_1 > Polinomio_2
            #Primero se calcula la diferencia de tamaños entre las listas de coeficientes: 
            #   len(result_coeff) - len(other.coeff) = Tamaño Polinomio_1 - Tamaño Polinomio_2
            #Esta resta siempre será positiva, confirmando que el segundo polinomio tiene menos términos que el 
            #primero.
            #Ahora multiplicamos una lista de ceros [0] por la diferencia de longitudes utilizando la expresión:
            #   [0] * (Tamaño Polinomio_1 - Tamaño Polinomio_2).
            #Esto crea una lista de ceros con una cantidad igual a la diferencia de longitudes. 
            #Por ejemplo, si la diferencia es 2, se generará el vector [0, 0] y por medio de la operación += se 
            #agregarán los ceros al final de la lista del Polinomio_2 para que tenga la misma longitud que 
            #Polinomio_1.
            other.coeff += [0] * (len(result_coeff) - len(other.coeff))  #Tamaño Polinomio_2 = Tamaño Polinomio_1
        elif len(other.coeff) > len(result_coeff):          #Polinomio_2 > Polinomio_1
            #Se repite el mismo proceso hecho con el Polinomio_2 cuando Polinomio_1 > Polinomio_2, pero ahora se 
            #aplica al Polinomio_1, ya que en este caso es de menor tamaño que el Polinomio_2.
            result_coeff += [0] * (len(other.coeff) - len(result_coeff)) #Tamaño Polinomio_1 = Tamaño Polinomio_2
        #Ya habiendo hecho igual el tamaño de los coeficientes de ambos polinomios, se realiza la resta:
        for i in range(len(result_coeff)): 
            result_coeff[i] -= other.coeff[i]               #Polinomio_1 - Polinomio_2
        return Polynomial(result_coeff)



    #MÉTODO __MUL__: Método para multiplicar polinomios.
    def __mul__(self, other):
        c = self.coeff                      #Polinomio_1
        d = other.coeff                     #Polinomio_2
        #len(): Método que devuelve la longitud de una lista.
        M = len(c) - 1        #Número de índices del polinomio, por eso es que se resta un 1 al tamaño.
        N = len(d) - 1        #Número de índices del polinomio, por eso es que se resta un 1 al tamaño.
        import numpy as np #Librería numpy: Realiza operaciones matemáticas complejas (matriciales).
        #numpy.zeros(): Método que crea un vector o matriz lleno de ceros, en el primer parámetro se indica el 
        #tamaño del eje x (número de columnas), en el segundo el tamaño del eje y (número de filas) y en el 
        #terceroel tipo de dato de los elementos que conforman la matriz, los demás parámetros del método casi 
        #no se usan.
        #Se crea un vector con la suma de ambos índices de los coeficientes de ambos polinomios + 1, para así 
        #obtener un tamaño donde se pueda almacenar el resultado de la multiplicación de polinomios. Cada índice 
        #corresponde al grado máximo (exponente máximo) de cada polinomio.
        result_coeff = np.zeros( M + N + 1) #Vector resultante de la multiplicación
        
        #Recorre los índices del primer polinomio partiendo desde cero
        for i in range(M + 1):              #Recorrer todos los coeficientes del Polinomio_1
            #Recorre los índices del segundo polinomio partiendo desde cero
            for j in range(N + 1):          #Recorrer todos los coeficientes del Polinomio_2
                #Dentro de este bucle for se calcula el producto de los coeficientes correspondientes a los 
                #dos polinomios, es decir, c[i] * d[j]. 
                #Luego se suma este producto al coeficiente correspondiente al vector resultante en su índice i+j. 
                #Esto se hace para acumular los términos de la multiplicación en la posición adecuada dentro del 
                #polinomio resultante.
                result_coeff[i+j]=result_coeff[i+j]+c[i]*d[j]
        return Polynomial(result_coeff)
    


    #MÉTODO DERIVATE: Método para obtener la derivada de un polinomio, para ello se apoya en un método que obtiene 
    #su diferencial.
    #differentiate(): Funcion para obtener el diferencial de un polinomio.
    def differentiate(self):
        #Recorre los índices del polinomio partiendo desde 1 hasta el número de su tanaño, que siempre es 1 más 
        #al número de índices, se recorre desde 1 para que se pueda seguir la fórmula del diferencial que es la sig:
        #d/dx((i=0;i=n)∑ci*x) = (i=1;i=n)∑i*ci*x^(i-1)
        for i in range(1, len(self.coeff)): #Recorrer todos los coeficientes del Polinomio_1
            #d/dx = (i=1;i=n)∑i*ci*x^(i-1); Recordemos que el grado de x^(i-1) se accede a través del índice del 
            #coeficiente perteneciente al polinomio.
            self.coeff[i-1]=i*self.coeff[i]
        #del: Permite eliminar uno o varios elementos de una lista, e incluso la misma lista. Esto se hace porque la 
        #derivada reduce el grado máximo del polinomio en uno y se realiza utilizando el método del indicando la 
        #posición [-1], el índice -1 en Python se utiliza para hacer referencia al último elemento de una lista.
        del self.coeff[-1]
    #derivate(): Funcion para derivar un polinomio
    def derivate(self):
        #Objeto o Instancia de la clase Polynomial: Recibe el parámetros del constructor de la clase Polynomial, que 
        #es simplemente el vector de coeficientes del polinomio. 
        dpdx = Polynomial(self.coeff[:])
        #Luego se le aplica el método differentiate() al objeto y de esta forma se obtiene la derivada del polinomio.
        dpdx.differentiate()
        return dpdx
    

    
    #MÉTODO __STR__: Función para imprimir el resultado de la operación de polinomios correctamente en consola.
    def __str__(self):
        s="" #String s vacío que se utilizará para construir la representación del polinomio en consola.
        #Recorre los índices del polinomio partiendo desde cero
        for i in range(len(self.coeff)):
            #Dentro del bucle for, se verifica si el coeficiente en la posición actual es diferente de cero, esto 
            #porque los coeficientes que tengan un cero no aparecerán en la representación del polinomio.
            if(self.coeff[i] != 0):
                #Si el coeficiente no es cero, se agrega un string a la variable "s" que represente el término 
                #correspondiente a la multiplicación de la constante (coeficiente) por la variable del polonomio 
                #elevada al exponente que le corresponde, ya que los polinomios son descritos como: 
                #p(x) = a0 + a1*x + a2*x^2 + a3*x^3 + ... + an*x^n, 
                #donde los coeficientes del polinomio son: a0, a1, a2, a3, ..., an.
                #Por ejemplo, el polinomio: p(x) = 1-x^2+2x^3, tiene como coeficientes el vector: [1, 0, -1, 2]
                s += " + %g*x^%d" %(self.coeff[i],i)
            #replace(): Método que reemplaza un caracter que se encuentra en un string por otro declarado por 
            #nosotros, esto se ejecutará todas las veces que dicho caracter aparezca en el string.
            #A continuación, se realizan una serie de reemplazos en la cadena s utilizando el método replace() para 
            #mejorar la presentación del polinomio:
            s= s.replace("+ -","- ")    #"+ -" se reemplaza por "- " para eliminar la redundancia de signos.
            s= s.replace("x^0","1")    #"x^0" se reemplaza por " " para representar el término constante.     
            s= s.replace("1*", " ")     #"1*" se reemplaza por " " para simplificar la representación de una constante.
            s= s.replace("x^1","x")     #"x^1" se reemplaza por "x" para representar x elevada a la primera potencia.
            #Después de realizar los reemplazos, se verifican algunas condiciones en la cadena s para ajustar el 
            #formato:
            if(s[0:3]==" + "):
                #Si los primeros tres caracteres de s son " + ", estos se eliminan para evitar que aparezca un signo + 
                #innecesario al comienzo de la expresión.
                s = s[3:]
            if(s[0:3]==" - "):
                #Si los primeros tres caracteres de s son " - ", se reemplazan por un "-" para tener un signo menos al 
                #comienzo de la expresión cuando esta sea negativa.
                s = "-" + s[3:]
        return s