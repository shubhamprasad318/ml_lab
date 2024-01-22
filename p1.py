import heapq

romania_map = {'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140}, 'Zerind': {'Arad': 75, 'Oradea': 71}, 'Oradea': {'Zerind': 71, 'Sibiu': 151}, 'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80}, 'Timisoara': {'Arad': 118, 'Lugoj': 111}, 'Lugoj': {'Timisoara': 111, 'Mehadia': 70}, 'Mehadia': {'Lugoj': 70, 'Drobeta': 75}, 'Drobeta': {'Mehadia': 75, 'Craiova': 120}, 'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138}, 'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97}, 'Fagaras': {'Sibiu': 99, 'Bucharest': 211}, 'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101}, 'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85}, 'Giurgiu': {'Bucharest': 90}, 'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98}, 'Hirsova': {'Urziceni': 98, 'Eforie': 86}, 'Eforie': {'Hirsova': 86}, 'Vaslui': {'Urziceni': 142, 'Iasi': 92}, 'Iasi': {'Vaslui': 92, 'Neamt': 87}, 'Neamt': {'Iasi': 87}}

heuristic = {'Arad': 366, 'Zerind': 374, 'Oradea': 380, 'Sibiu': 253, 'Timisoara': 329, 'Lugoj': 244, 'Mehadia': 241, 'Drobeta': 242, 'Craiova': 160, 'Rimnicu Vilcea': 193, 'Fagaras': 176, 'Pitesti': 100, 'Bucharest': 0, 'Giurgiu': 77, 'Urziceni': 80, 'Hirsova': 151, 'Eforie': 161, 'Vaslui': 199, 'Iasi': 226, 'Neamt': 234}

def a_star_search(graph, start, goal, heuristic):
    open_list, closed_set, g_score = [(0, start, [])], set(), {loc: float('inf') for loc in graph}
    g_score[start] = 0
    
    while open_list:
        current_g, current_node, path = heapq.heappop(open_list)
        if current_node == goal:
            return g_score[goal], path + [goal]
        if current_node in closed_set:
            continue
        closed_set.add(current_node)
        for neighbor, distance in graph[current_node].items():
            tentative_g = g_score[current_node] + distance
            if tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic[neighbor]
                heapq.heappush(open_list, (f_score, neighbor, path + [current_node]))
    
    return float('inf'), []

start, goal = 'Arad', 'Bucharest'
distance, path = a_star_search(romania_map, start, goal, heuristic)

if distance < float('inf'):
    print(f"Shortest distance from {start} to {goal}: {distance} km")
    print("Shortest path:", path)
else:
    print(f"No path found from {start} to {goal}")
