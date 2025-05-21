def greedy_graph_coloring(graph):
    colors = {}
    for node in graph:
        neighbor_colors = {colors[neighbor] for neighbor in graph[node] if neighbor in colors}
        color = 1
        while color in neighbor_colors:
            color += 1
        colors[node] = color
    return colors, max(colors.values()) if colors else 0

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

coloring, num_colors = greedy_graph_coloring(graph)
print(f"Раскраска вершин: {coloring}")
print(f"Минимальное количество цветов (жадный алгоритм): {num_colors}")