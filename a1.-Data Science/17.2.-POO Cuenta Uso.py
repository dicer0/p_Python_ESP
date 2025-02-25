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

#Importación de la clase Acount del archivo que originalmente era 11.-POO_Cuenta y se cambió porque Python no 
#puede manejar bien este nombre de archivo para importar

#USO DE LA CLASE ACCOUNT: Cuando se quiera importar una clase, el nombre de esta no puede empezar con un número, 
#sino cuando la quiera importar obtendré un error y se va accediendo a las carpetas o también llamados paquetes 
#en la programación orientada a objetos (POO), por medio de puntos:
# - Directorio normal:      carpeta1/carpeta2/carpeta3
# - Directorio paquetes:    carpeta1.carpeta2.carpeta3
#La parte del directorio se coloca después de la palabra reservada from y la clase a importar después de import.
from Clases_Personalizadas.POO_17_2_Account.POO_Account_Declaración import Account

#Objetos o Instancias de la clase Account: Reciben los parámetros del constructor de la clase Account, que son 
#el nombre, número de cuenta y cantidad inicial de la cuenta.
a1 = Account("Helmer Homero", "1234", 20000)
a2 = Account("Pita amor", "5678", 2000)

#Métodos: Para utilizar los métodos de una clase se debe usar la siguiente nomenclatura:
# - nombreObjeto.nombreMétodo(parámetro1, parámetro2, ..., parámetro_n).
#MÉTODO DEPOSIT: Sirve para hacer un deposito en la cuenta, osea sumar a su cantidad inicial o actual.
a1.deposit(1000)        #Depósito en la cuenta del Objeto 1 = 20000 + 1000 = 21000

#MÉTODO WITHDRAW: Sirve para hacer un retiro de la cuenta, osea restar a su cantidad inicial o actual.
a1.withdraw(4000)       #Retiro en la cuenta del Objeto 1 = 21000 - 4000 = 17000
a2.withdraw(10500)      #Retiro en la cuenta del Objeto 2 = 2000 - 10500 = -8500
a1.withdraw(3500)       #Retiro en la cuenta del Objeto 1 = 17000 - 3500 = 13500

#MÉTODO DUMP: Sirve para imprimir en consola el estado (balance) de la cuenta.
a1.dump()               #Balance de la cuenta del Objeto 1 = 13500
a2.dump()               #Balance de la cuenta del Objeto 2 = -8500

#ENCAPSULAMIENTO: Todos los atributos (variables de la clase) están encapsulados, esto significa que no pueden 
#ser accedidos desde fuera de la clase, esto solamente puede ser burlado cuando existe un método que sirva para 
#editar dicho valor o cuando se ponga el nombre del atributo sin un doble guión antes de su nombre.
# - nombreObjeto.__nombreAtributo: Atributo encapsulado.
# - nombreObjeto.nombreAtributo: Atributo sin encapsular.
a2.__balance = 10000    #Esto no se podrá hacer porque está encapsulado el atributo (variable) la clase
a2.dump()               
a2.balance = 10000      #Si se quita el doble guión en la clase Account si se podrá cambiar el valor
a2.dump()