
# Завдання 3. Дерева, алгоритм Дейкстри
# Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, 
# використовуючи бінарну купу. Завдання включає створення графа, використання піраміди 
# для оптимізації вибору вершин та обчислення найкоротших шляхів від початкової вершини до всіх інших.

import networkx as nx
import heapq
from typing import Dict, Tuple, List

def dijkstra_with_paths(graph: nx.Graph, start: str) -> Tuple[Dict[str, int], Dict[str, List[str]]]:
    # Ініціалізація відстаней до всіх вершин як нескінченність, окрім стартової
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    
    # Словник для зберігання маршрутів
    paths = {node: [] for node in graph.nodes}
    paths[start] = [start]

    # Черга пріоритетів для вибору вершини з мінімальною відстанню
    priority_queue = [(0, start)]
    heapq.heapify(priority_queue)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Якщо знайдена коротша відстань, ігноруємо старий варіант
        if current_distance > distances[current_node]:
            continue
        # Перевірка всіх сусідів
        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight

            # Оновлення, якщо знайдено коротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[current_node] + [neighbor]
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, paths

# Створення графа за допомогою networkx та додавання зважених ребер
G = nx.Graph()
edges = [
    ("A", "B", 5), 
    ("A", "C", 2), 
    ("B", "C", 1), 
    ("B", "D", 2), 
    ("C", "D", 7), 
    ("C", "E", 4), 
    ("D", "E", 3)
]
G.add_weighted_edges_from(edges)

# Виклик алгоритму Дейкстри для графа
start_vertex = "A"
shortest_distances, shortest_paths = dijkstra_with_paths(G, start_vertex)

print(f"Найкоротші відстані та маршрути від вершини {start_vertex}:")
for vertex, distance in shortest_distances.items():
    print(f"Вершина {vertex}: Відстань = {distance}, Маршрут = {' -> '.join(shortest_paths[vertex])}")
