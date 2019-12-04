## El problema
Una plataforma de Red Social, permite las siguientes operaciones a sus usuarios: post, follows, re-post
La plataforma provee a los desarrolladores de aplicaciones, el siguiente API:

 GET /{username}/followers
```javascript
{ "user": "username",  "Followers": ["user1", "user2",….. "user n"] }
```
GET /{username}/following
```javascript
{ "user": "username",  "Following": ["user1", "user2",….. "user n"] }
```
 Implemente un algoritmo en cualquier lenguaje de programación, que calcule la distancia entre 2 usuarios.

### Ejemplo:
Dado: user1 >> user2 >> user3
> User 1, sigue a User 2. Y User 2, sigue a User 3

> Distancia entre User 1 y User 3, es: 2
## Solución propuesta
1. LLenar un Grafo social de forma exhaustiva consumiendo el API referido 
1. Ejecutar una búsqueda Breath-First Search en el grafo hasta que se encuentre la primera ocurrencia del usuario de 
destino, esta será la distancia más corta.

## Ejecución
```bash
python user_distance.py <username_origen> <username_destino>
```

## Referencias de solución:
* https://www.python.org/doc/essays/graphs/
* https://realpython.com/api-integration-in-python/
* https://realpython.com/python-requests/
* https://www.codespeedy.com/breadth-first-search-algorithm-in-python/
* https://medium.com/@yasufumy/algorithm-breadth-first-search-408297a075c9
