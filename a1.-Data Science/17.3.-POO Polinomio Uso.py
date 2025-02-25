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

#Importa de la clase Acount del archivo que originalmente era 11.-POO_Cuenta y se cambió porque Python no 
#puede manejar bien este nombre de archivo para importar
from Clases_Personalizadas.POO_17_3_Polynomial.POO_Polinomio_Declaración import Polynomial

#Objetos o Instancias de la clase Polynomial: Recibe el parámetros del constructor de la clase Polynomial, 
#que es el vector (lista) de coeficientes del polinomio.
p1 = Polynomial([1,-1])
p2 = Polynomial([0,1,0,0,-6,-1])
#print(): Imprimir un mensaje en consola, la forma de concatenar este mensaje puede ser añadiendo un símbolo 
#de +  una coma entre el string que se quiere concatenar y las variables.
print("p1(x) =", p1)
print("p2(x) =", p2)

#SOBRECARGANDO LOS OPERADORES: Esto se refiere a asignar un método a los símbolos de suma, resta, multiplicación, 
#etc. para realizar en este caso operaciones matemáticas con los polinomios.

#MÉTODO __ADD__: Método para sumar polinomios, corresponde al símbolo +.
p3 = p1 + p2
print("p3 = p1 + p2 =", p3)

#MÉTODO __SUB__: Método para restar polinomios, corresponde al símbolo -.
p4 = p1 - p2
print("p4 = p1 - p2 =", p4)

#MÉTODO __MUL__: Método para multiplicar polinomios, corresponde al símbolo *.
p5 = p1 * p2
print("p5 = p1 * p2 =", p5)

#MÉTODO DERIVATE: Método para obtener la derivada de un polinomio.
p6 = p2.derivate()
print("dp2/dx =", p6)

#EVALUAR EL RESULTADO DE UN POLINOMIO SI SE SUSTITUYE LA VARIABLE X POR UN VALOR ENTERO: A través del método 
#call se evalúa un polinomio sustituyendo su variable x por un valor numérico, para ello se debe declarar el 
#valor de x, usar una instancia de la clase y posteriormente pasar como parámetro la variable x.
x = 1
#print(): Imprimir un mensaje en consola, la forma de concatenar este mensaje puede ser añadiendo un símbolo 
#de +  una coma entre el string que se quiere concatenar y las variables o además se puede utilizar la 
#nomenclatura de %g, donde se coloca este signo cada que se quiera colocar el valor de una variable entre un 
#string (denotado entre comillas), luego se coloca un signo de % y finalmente un paréntesis con las variables 
#u objetos que se quiera concatenar, separados entre comillas y colocados en el órden en el que se hayan 
#colocado en el string. 
print("p1(x=%g) = %g"%(x, p1(x)))
print("p2(x=%g) = %g"%(x, p2(x)))