import heapq

def dijkstra(graph, start):
    # Initialize distances with infinity for all nodes
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue to keep track of the nodes to visit next
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if we've already found a shorter path
        if current_distance > distances[current_node]:
            continue

        # Iterate through neighbors of current_node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If this path is shorter than the current shortest path, update distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example graph
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 3, 'B': 2, 'D': 4, 'E': 2},
    'D': {'B': 1, 'C': 4, 'E': 1},
    'E': {'C': 2, 'D': 1}
}

start_node = 'A'
shortest_distances = dijkstra(graph, start_node)
print("Shortest distances from node", start_node + ":")
for node, distance in shortest_distances.items():
    print(node + ":", distance)
