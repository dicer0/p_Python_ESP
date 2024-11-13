#TIPOS DE ESTRUCTURAS DE DATOS EN PYTHON - DSA (DATA STRUCTURES AND ALGORITHMS): 
#La gran diferencia entre ellos, es que algunos tienen cierto órden (índice y valor) y otros no, además de que 
#algunos son editables o mutables, donde se les puede agregar, eliminar, o modificar elementos y otros son 
#inmutables, donde sus datos no se pueden cambiar.
# - Listas (list): Una lista es una colección ordenada (con índice y valor) y mutable (editable) de elementos. Se 
#   definen utilizando corchetes [].
#       Ejemplo: mi_lista = [1, 2, "hola", True].
# - Tuplas (tuple): Una tupla es una colección ordenada e inmutable de elementos. Se definen utilizando 
#   paréntesis ().
#       Ejemplo: mi_tupla = (1, 2, "hola", True).
# - Diccionarios (dict): Un diccionario es una colección desordenada y mutable de pares clave-valor. Se definen 
#   utilizando llaves {} y separando cada par clave-valor por dos puntos(:).
#       Ejemplo: mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}.
# - Conjuntos (set): Un conjunto es una colección desordenada y mutable de elementos únicos. No permite elementos 
#   duplicados y no tiene un orden definido. Se definen utilizando llaves {} o utilizando la función set().
#       Ejemplo: mi_conjunto = {1, 2, 3, 4, 5}.

#MÉTODOS COMÚNES ARRAYS:
#array[index]: Acceder al elemento o array interno que se encuentre en cierto índice o posición que se cuenta 
#desde 0.
#array.append(element): Añade un elemento al final de la lista.
#array.extend(array): Extiende la lista añadiendo todos los elementos de una lista dada, osea otro array.
#array.insert(index, element): Inserta un elemento en una posición o índice específico.
#array.remove(element): Elimina el primer elemento con el valor especificado.
#array.pop(index, element): Elimina y devuelve el elemento en la posición especificada (por defecto, el último 
#elemento).
#array.clear(): Elimina todos los elementos de la lista.
#array.index(element): Devuelve el índice del primer elemento con el valor especificado.
#array.count(element): Devuelve el número de veces que aparece un valor especificado en la lista.
#array.sort(): Ordena la lista de menor a mayor.
#array.reverse(): Invierte el orden de los elementos en la lista.
#array.copy(): Devuelve una copia de la lista.

#Ejemplo numérico: Por ejemplo, para extraer todos los dígitos de un número, podemos utilizar un bucle for de una 
#sola línea para que de esta manera se cree una lista de los dígitos pertenecientes a un número:
#Bucle for en una sola línea: [instrucción      for   variable_local   in   range(inicio, final)]
#Bucle for en una sola línea: [instrucción      for   variable_local   in   array_a_recorrer]
digits = 12345
digits_str = str(digits)
array_digitos = [int(digit) for digit in digits_str]
print("Ejemplo Arrays: " + str(array_digitos))

#MÉTODOS COMÚNES STRINGS:
#string.capitalize(str): Convierte el primer carácter a mayúsculas.
#string.lower(str): Convierte todos los caracteres a minúsculas.
#string.upper(str): Convierte todos los caracteres a mayúsculas.
#string.title(str): Convierte el primer carácter de cada palabra a mayúsculas.
#string.strip(str): Elimina los caracteres de espacio en blanco al inicio y al final.
#string.lstrip(str): Elimina los caracteres de espacio en blanco al inicio.
#string.rstrip(str): Elimina los caracteres de espacio en blanco al final.
#string.split(char): Divide la cadena en una lista de subcadenas utilizando el caracter especificado (por defecto, 
#el string de espacio).
#string.join(char): Une una lista de cadenas con un delimitador especificado.
#string.replace(strOriginal, strReemplazo): Reemplaza todas las ocurrencias de una subcadena con otra subcadena.
#string.find(str): Devuelve el índice de la primera aparición de una subcadena. Devuelve -1 si no se encuentra.
#string.count(str): Devuelve el número de veces que aparece una subcadena en la cadena.
#string.startswith(str): Devuelve True si la cadena empieza con la subcadena especificada.
#string.endswith(str): Devuelve True si la cadena termina con la subcadena especificada.
#string.isnumeric(): Devuelve True si todos los caracteres de la cadena son numéricos.
#string.isalnum(): Devuelve True si todos los caracteres de la cadena son alfanuméricos.
#string.isalpha(): Devuelve True si todos los caracteres de la cadena son alfabéticos.


#ALGORITMOS Y ESCTRUCTURAS DE DATOS Big O Notation:
#Complejidad Constante (O(1)): Este tipo de operación siempre toma en ejecutarse la misma cantidad de tiempo, sin 
#importar el tamaño del array.
#Ejemplo 1.1.- Acceso a un elemento específico en un array.
def get_element(arr, index):
    return arr[index]
arr = [1, 2, 3, 4, 5]
print("Ejemplo 1.1.- Big O Notation Complejidad Constante: " + str(get_element(arr, 2)))    #Output: 3

#Complejidad Lineal (O(n)): Este tipo de operación toma en ejecutarse un tiempo proporcional al tamaño del array.
#Ejemplo 2.1.- Recorrer todos los elementos de un array.
def print_all_elements(arr):
    for element in arr:
        print("Ejemplo 2.1.- Big O Notation Complejidad Lineal: " + str(element))
arr = [1, 2, 3, 4, 5]
print_all_elements(arr)    #Output: 1, 2, 3, 4, 5

#Complejidad Logarítmica (O(log n)): Este tipo de operación es eficiente porque reduce el espacio de búsqueda a 
#la mitad en cada paso.
#Ejemplo 3.1.- Búsqueda binaria en un array ordenado.
def binary_search(arr, value):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1
arr = [1, 2, 3, 4, 5]
print("Ejemplo 3.1.- Big O Notation Complejidad Lineal: " + str(binary_search(arr, 4)))
#Output: 3 (índice del elemento 4)

#Complejidad Exponencial (O(2^n)): Este tipo de operación es muy costosa y se vuelve impracticable para datos de 
#entrada grandes, osea de muchos elementos.
#Ejemplo 4.1.- Generar todas las combinaciones posibles de un array.
def generate_subsets(arr):
    subsets = []
    n = len(arr)
    def backtrack(start, path):
        subsets.append(path)
        for i in range(start, n):
            backtrack(i + 1, path + [arr[i]])
    backtrack(0, [])
    return subsets
arr = [1, 2, 3]
print("Ejemplo 4.1.- Big O Notation Complejidad Lineal: " + str(generate_subsets(arr)))
# Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

#Árboles Binarios: Los árboles binarios son estructuras de datos jerárquicas donde cada nodo tiene a lo sumo 
#dos hijos.
#Definición y recorrido en preorden de un árbol binario.
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def preorder_traversal(root):
    if root:
        print(root.value, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
preorder_traversal(root)
#Output: 1 2 4 5 3

#BINARY TREE: Un árbol binario es una estructura de datos jerárquica en la que cada nodo tiene a lo sumo dos 
#hijos, conocidos como el hijo izquierdo y el hijo derecho. Los árboles binarios son una estructura fundamental 
#en la informática debido a su eficiencia para ciertas operaciones y su capacidad para representar relaciones 
#jerárquicas.
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
#Función para insertar un nuevo nodo con la clave dada
def insert(root, key):
    #Si el árbol está vacío, retornar un nuevo nodo
    if root is None:
        return Node(key)
    #De lo contrario, recurrir por el árbol
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    #Retornar el nodo (sin cambios)
    return root
#Función para realizar un recorrido en orden
def in_order_traversal(root):
    if root:
        # Recorrer el subárbol izquierdo
        in_order_traversal(root.left)
        # Imprimir el valor del nodo
        print(root.val, end=" ")
        # Recorrer el subárbol derecho
        in_order_traversal(root.right)
#Crear un nuevo árbol binario e insertar algunos nodos
root = Node(50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)
#Realizar un recorrido en orden
print("In-order traversal of the binary tree is:")
in_order_traversal(root)  #Output: 20 30 40 50 60 70 80


#Grafos: Los grafos son estructuras de datos que consisten en nodos conectados por aristas.
#Recorridos DFS y BFS en un grafo.
from collections import deque
#Grafo como diccionario de listas
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

#DFS (Búsqueda en Profundidad): Algoritmo que explora un grafo tan profundo como sea posible antes de retroceder.
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
print("DFS Traversal:")
dfs(graph, 'A')  # Output: A B D E F C

#BFS (Búsqueda en Amplitud): Algoritmo que explora un grafo nivel por nivel desde el nodo inicial.
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
print("\nBFS Traversal:")
bfs(graph, 'A')  # Output: A B C D E F


#Matrices
#Recorrer una matriz imprimiendo cada elemento.
#Las matrices son colecciones bidimensionales de datos organizadas en filas y columnas.
def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_matrix(matrix)


#Listas Enlazadas
#Definición y recorrido de una lista enlazada.
#Las listas enlazadas son colecciones de nodos donde cada nodo contiene un valor y un enlace al siguiente nodo.
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
print_linked_list(head)
#Output: 1 -> 2 -> 3 -> None


#Hip Tree Algorithms: Los Hip trees son una variante de los árboles binarios balanceados, diseñados para 
#optimizar ciertas operaciones específicas.
class HipTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.balance_factor = 0
#Funciones específicas para operaciones en Hip Tree pueden ser muy técnicas y específicas.


#Estructuras Jerárquicas: Las estructuras jerárquicas organizan datos en niveles o capas.
#Representación y recorrido de un árbol de directorios.
class Directory:
    def __init__(self, name):
        self.name = name
        self.subdirectories = []
def print_directory_structure(directory, indent=0):
    print(" " * indent + directory.name)
    for subdirectory in directory.subdirectories:
        print_directory_structure(subdirectory, indent + 2)
root = Directory("root")
home = Directory("home")
user = Directory("user")
documents = Directory("documents")
pictures = Directory("pictures")
root.subdirectories.extend([home, user])
user.subdirectories.extend([documents, pictures])
print_directory_structure(root)
# Output:
# root
#   home
#   user
#     documents
#     pictures

#Algoritmos de Recorrido (Traversal)
#Los algoritmos de recorrido se utilizan para visitar todos los nodos en una estructura de datos, como un árbol o 
#un grafo.
#Pueden ser utilizados para búsquedas, ordenamientos y otras operaciones que requieren visitar cada nodo.
#Ejemplo: Recorrido en preorden de un árbol binario (ver más arriba en el código).

#Divide y Conquista (Divide and Conquer)
#Este enfoque divide un problema en subproblemas más pequeños y manejables, los resuelve de manera recursiva, y 
#luego combina los resultados.
#Es útil para algoritmos de ordenamiento, búsqueda y otras operaciones complejas.
#Ejemplo: Búsqueda binaria (ver más arriba en el código).

#Breadth-First Search (BFS - Búsqueda en Amplitud)
#Algoritmo que explora un grafo nivel por nivel desde el nodo inicial.
#Es útil para encontrar el camino más corto en un grafo no ponderado y para búsquedas de amplitud en estructuras 
#jerárquicas.
#Ejemplo de código: BFS en un grafo (ver más arriba en el código).

#Depth-First Search (DFS - Búsqueda en Profundidad)
#Algoritmo que explora un grafo tan profundo como sea posible antes de retroceder.
#Es útil para la detección de ciclos, el recorrido de todas las posibles rutas y la búsqueda en profundidad en 
#estructuras jerárquicas.
#Ejemplo de código: DFS en un grafo (ver más arriba en el código).