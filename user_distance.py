import requests
import sys
from collections import deque
from time import sleep

# Definimos la URL base para la API.
BASE_URL = 'http://127.0.0.1:8000/'
s = requests.Session()

# Establecemos un tiempo de espera para las solicitudes.
TIMEOUT = 10  # en segundos

def get_following(username):
    """Obtiene los usuarios que siguen a un usuario."""
    try:
        response = s.get(BASE_URL + username + '/following', timeout=TIMEOUT)
        response.raise_for_status()  # Lanzará un error si la respuesta no es exitosa (status code 4xx/5xx)
        return response.json().get('Following', [])
    except requests.RequestException as e:
        print(f"Error al obtener los seguidores de {username}: {e}")
        return []

def load_social_graph(graph, username, visited=None, max_depth=3):
    """Carga el grafo social de forma recursiva, limitando la profundidad."""
    if visited is None:
        visited = set()
    
    if username in visited or max_depth == 0:
        return
    
    # Añadimos el usuario a los visitados
    visited.add(username)
    
    # Obtenemos los seguidores de este usuario
    following = get_following(username)
    graph[username] = following
    
    # Llamamos recursivamente para cargar los seguidores de los seguidores
    for usr in following:
        load_social_graph(graph, usr, visited, max_depth - 1)

def execute_bfs(graph, start_node, end_node):
    """Realiza un BFS para encontrar el camino más corto entre dos usuarios."""
    queue = deque([start_node])
    level = {start_node: 0}
    parent = {start_node: None}

    while queue:
        vertex = queue.popleft()
        for neighbor in graph.get(vertex, []):
            if neighbor not in level:  # Si el vecino no ha sido visitado
                queue.append(neighbor)
                level[neighbor] = level[vertex] + 1
                parent[neighbor] = vertex

                # Si llegamos al nodo final, devolvemos los resultados
                if neighbor == end_node:
                    return level, parent

    return level, parent

def get_user_distance(username_from, username_to, max_depth=3):
    """Obtiene la distancia entre dos usuarios en la red social."""
    social_graph = dict()
    load_social_graph(social_graph, username_from, max_depth=max_depth)
    
    if username_to not in social_graph:
        print(f"No se pudo encontrar el usuario {username_to} en el grafo.")
        return

    bfs_result = execute_bfs(social_graph, username_from, username_to)
    level, parent = bfs_result

    if username_to in level:
        print(f"La distancia entre {username_from} y {username_to} es {level[username_to]}")
    else:
        print(f"No se encontró un camino entre {username_from} y {username_to}.")

if __name__ == "__main__":
    try:
        username_from = sys.argv[1]
        username_to = sys.argv[2]
        get_user_distance(username_from, username_to, max_depth=3)  # Limitar la recursión a 3 niveles
    except IndexError:
        print("Por favor, proporciona dos nombres de usuario como argumentos.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


"""
Mi Solucion se trata en  propones busca encontrar la "distancia"
 o número de pasos entre dos usuarios en una red social, 
 utilizando un grafo social donde los nodos son usuarios y las aristas representan 
 a las personas a las que siguen. Usa BFS para encontrar el camino más corto en términos
  de cantidad de relaciones entre esos usuarios.
"""
