import requests
import sys
from collections import deque

s = requests.Session()
BASE_URL = 'http://127.0.0.1:8000/'

""" Consumo de API, obtiene los seguidores de un nombre de usuario dado como parámetro
"""
def get_following(username):
    response = s.request('GET', BASE_URL + username + '/following')
    json = response.json()
    return json['Following']


""" Carga los nodos de un Grafo Social haciendo llamadas al método que invoca al API
"""
def load_social_graph(graph, username):
    if not graph.get(username):
        following = get_following(username)
        graph[username] = following
        for usr in following:
            load_social_graph(graph, usr)


""" Implementación de algoritmo Breath-First Search para búsqueda de camino más corto entre dos nodos/vertices de un grafo
https://medium.com/@yasufumy/algorithm-breadth-first-search-408297a075c9
"""
def execute_bfs(graph, start_node, end_node):
    queue = deque([start_node])
    level = {start_node: 0}
    parent = {start_node: None}
    i = 1
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in level:
                queue.append(neighbor)
                level[neighbor] = i
                parent[neighbor] = vertex
        i += 1
        if level.get(end_node):
            return level, parent
    return level, parent


""" Llama a los metodos necesarios para calcular distancia entre usuarios
"""
def get_user_distance(username_from, username_to):
    social_graph = dict()
    load_social_graph(social_graph, username_from)
    bfs_result = execute_bfs(social_graph, username_from, username_to)
    print("La distancia entre %s y %s es %i" % (username_from, username_to, bfs_result[0][username_to]))


username_from = sys.argv[1]
username_to = sys.argv[2]
get_user_distance(username_from, username_to)
