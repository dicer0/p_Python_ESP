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
#2.-Account: Clase que sirve para realizar depósitos, retiros y balances de cuenta de una persona.

#DECLARACIÓN DE LA CLASE ACCOUNT:
class Account:
    #CONSTRUCTOR O INICIALIZADOR DE LA CLASE: En él se declaran los atributos que se reutilizarán en los demás 
    #métodos y que además, deben a fuerza de tener un valor.
    def __init__(self, name, account_number, initial_amount): 
    #Los parámetros del constructor de la clase Account son el nombre, número de cuenta y cantidad inicial.
        #self es distinto a this, por eso no debe tener el mismo nombre que el parámetro que está recibiendo el
        #constructor, se puede renombrar la variable que llega a la clase por medio del constructor.
        #self lo que hace es referenciar métodos o datos de la clase donde nos encontramos, es una referencia 
        #a lo que sea que pertenezca a esta clase.
        self.name = name                #Atributo 1 de la clase Account = name = Nombre
        self.no = account_number        #Atributo 2 de la clase Account = account_number = número de cuenta
        self.balance = initial_amount   #Atributo 3 de la clase Account = initial_amount = cantidad inicial

    #MÉTODO DEPOSIT: Recibe como parámetros los mismos que el constructor (name, account_number e initial_amount), 
    #pero además la variable amount. Sirve para hacer un deposito en la cuenta.
    def deposit(self, amount):
        self.balance = self.balance + amount
    
    #MÉTODO WITHDRAW: Recibe como parámetros los mismos que el constructor (name, account_number e initial_amount), 
    #pero además la variable amount. Sirve para hacer un retiro de la cuenta.
    def withdraw(self, amount):
        self.balance = self.balance - amount

    #MÉTODO DUMP: Recibe como parámetros los mismos que el constructor (name, account_number e initial_amount). 
    #Sirve para imprimir en consola el estado (balance) de la cuenta.
    def dump(self):
        s = "%s, %s, balance: %s" %(self.name, self.no, self.balance)
        #print(): Imprimir un mensaje en consola.
        print(s)
#Fin de la clase Acount