#TIPOS DE ESTRUCTURAS DE DATOS EN PYTHON: La gran diferencia entre ellos, es que algunos tienen cierto órden 
#(índice y valor) y otros no, además de que algunos son editables o mutables, donde se les puede agregar, eliminar, 
#o modificar elementos y otros son inmutables, donde sus datos no se pueden cambiar.
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
#ALGORITMOS Y ESCTRUCTURAS DE DATOS BigO:
#Complejidad Constante (O(1)): Este tipo de operación siempre toma en ejecutarse la misma cantidad de tiempo, sin 
#importar el tamaño del array.
#Acceso a un elemento específico en un array.
def get_element(arr, index):
    return arr[index]

arr = [1, 2, 3, 4, 5]
print(get_element(arr, 2))  #Output: 3


#Complejidad Lineal (O(n)): Este tipo de operación toma en ejecutarse un tiempo proporcional al tamaño del array.
#Recorrer todos los elementos de un array.
def print_all_elements(arr):
    for element in arr:
        print(element)

arr = [1, 2, 3, 4, 5]
print_all_elements(arr)


#Complejidad Logarítmica (O(log n)): Este tipo de operación es eficiente porque reduce el espacio de búsqueda a 
#la mitad en cada paso.
#Búsqueda binaria en un array ordenado.
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
print(binary_search(arr, 4))  # Output: 3 (índice del elemento 4)


#Complejidad Exponencial (O(2^n)): Este tipo de operación es muy costosa y se vuelve impracticable para tamaños 
#grandes de entrada.
#Generar todas las combinaciones posibles de un array.
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
print(generate_subsets(arr))
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


#Hip Tree Algorithms: Los Hip trees son una variante de los árboles binarios balanceados, diseñados para optimizar 
#ciertas operaciones específicas.
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
#Los algoritmos de recorrido se utilizan para visitar todos los nodos en una estructura de datos, como un árbol o un grafo.
#Pueden ser utilizados para búsquedas, ordenamientos y otras operaciones que requieren visitar cada nodo.
#Ejemplo: Recorrido en preorden de un árbol binario (ver más arriba en el código).

#Divide y Conquista (Divide and Conquer)
#Este enfoque divide un problema en subproblemas más pequeños y manejables, los resuelve de manera recursiva, y luego combina los resultados.
#Es útil para algoritmos de ordenamiento, búsqueda y otras operaciones complejas.
#Ejemplo: Búsqueda binaria (ver más arriba en el código).

#Breadth-First Search (BFS - Búsqueda en Amplitud)
#Algoritmo que explora un grafo nivel por nivel desde el nodo inicial.
#Es útil para encontrar el camino más corto en un grafo no ponderado y para búsquedas de amplitud en estructuras jerárquicas.
#Ejemplo de código: BFS en un grafo (ver más arriba en el código).

#Depth-First Search (DFS - Búsqueda en Profundidad)
#Algoritmo que explora un grafo tan profundo como sea posible antes de retroceder.
#Es útil para la detección de ciclos, el recorrido de todas las posibles rutas y la búsqueda en profundidad en estructuras jerárquicas.
#Ejemplo de código: DFS en un grafo (ver más arriba en el código).