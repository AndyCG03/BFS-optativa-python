#Implementación del BFS para recorrer un laberinto

#A diferencia de la solución del DFS el BFS utiliza como estructura para ir guardando los datos una cola en lugar de una pila

from collections import deque

def bfsAnswer(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    queue = deque([start])
    visited = set([start])

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Abajo, derecha, arriba, izquierda
    answer = {}

    while queue:
        current = queue.popleft()
        if current == goal:
            break #Ya llegué a mi destino por tanto no es necesario seguir

        for direction in directions:
            next_row, next_col = current[0] + direction[0], current[1] + direction[1]
            if (0 <= next_row < rows and 0 <= next_col < cols and
                maze[next_row][next_col] == 0 and
                (next_row, next_col) not in visited):
                queue.append((next_row, next_col))
                visited.add((next_row, next_col))
                answer[(next_row, next_col)] = current  

    
    if goal in answer:
        reverse_path = []
        while goal != start:
            reverse_path.append(goal)
            goal = answer[goal]
        reverse_path.append(start)
        return reverse_path[::-1]  # Invertir el camino y lo devuelvo
    else:
        return None  # No se encontró un camino


#Demostración de la implementación
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)  # Nodo inicial
goal = (4, 4)   # Nodo objetivo

answer = bfsAnswer(maze, start, goal)
print(answer)