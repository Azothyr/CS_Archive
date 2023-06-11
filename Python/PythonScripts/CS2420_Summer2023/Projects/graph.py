class Graph:
    def __init__(self):
        self.graph = {}

    def __str__(self):
        result = 'digraph G {\n'
        for src, edges in self.graph.items():
            for dest, weight in edges.items():
                result += f'   {src} -> {dest} [label="{weight}",weight="{weight}"];\n'
        result += '}'
        return result

    def add_vertex(self, label):
        if not isinstance(label, str):
            raise ValueError("label must be a string")
        if label not in self.graph:
            self.graph[label] = {}
        return self

    def add_edge(self, src, dest, w):
        if not isinstance(src, str) or not isinstance(dest, str) or not isinstance(w, (int, float)):
            raise ValueError("Invalid input")
        if src not in self.graph or dest not in self.graph:
            raise ValueError("Both vertices must be in the graph")
        self.graph[src][dest] = w
        return self

    def get_weight(self, src, dest):
        if src not in self.graph or dest not in self.graph:
            raise ValueError("Both vertices must be in the graph")
        return self.graph[src].get(dest, float('inf'))

    def dfs(self, starting_vertex):
        if starting_vertex not in self.graph:
            raise ValueError("The starting vertex must be in the graph")
        visited = set()
        stack = [starting_vertex]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                yield vertex
                stack.extend(sorted(self.graph[vertex].keys(), reverse=True))

    def bfs(self, starting_vertex):
        if starting_vertex not in self.graph:
            raise ValueError("The starting vertex must be in the graph")
        visited = {starting_vertex}
        queue = [starting_vertex]
        while queue:
            vertex = queue.pop(0)
            yield vertex
            for next_vertex in sorted(self.graph[vertex].keys()):
                if next_vertex not in visited:
                    visited.add(next_vertex)
                    queue.append(next_vertex)

    def dsp(self, src, dest):
        if src not in self.graph or dest not in self.graph:
            raise ValueError("Both vertices must be in the graph")
        shortest_paths = {src: (None, 0)}
        current_vertex = src
        visited = set()

        while current_vertex != dest:
            visited.add(current_vertex)
            destinations = self.graph[current_vertex]
            weight_to_current_vertex = shortest_paths[current_vertex][1]

            for next_vertex, weight in destinations.items():
                if next_vertex not in visited:
                    old_weight = shortest_paths.get(next_vertex, (None, float('inf')))[1]
                    new_weight = weight_to_current_vertex + weight
                    if new_weight < old_weight:
                        shortest_paths[next_vertex] = (current_vertex, new_weight)

            next_destinations = {vertex: shortest_paths[vertex] for vertex in shortest_paths if vertex not in visited}
            if not next_destinations:
                return float('inf'), []
            current_vertex = min(next_destinations, key=lambda k: next_destinations[k][1])

        path = []
        while current_vertex is not None:
            path.append(current_vertex)
            next_vertex = shortest_paths[current_vertex][0]
            current_vertex = next_vertex
        path = path[::-1]
        return shortest_paths[dest][1], path

    def dsp_all(self, src):
        all_paths = {}
        for dest in self.graph:
            dsp = self.dsp(src, dest)
            all_paths[dest] = dsp[1]
        return all_paths


def main():
    graph = Graph()
    graph.add_vertex('A').add_vertex('B').add_vertex('C').add_vertex('D').add_vertex('E').add_vertex('F')
    graph.add_edge('A', 'B', 2.0).add_edge('A', 'F', 9.0)
    graph.add_edge('B', 'C', 8.0).add_edge('B', 'D', 15.0).add_edge('B', 'F', 6.0)
    graph.add_edge('C', 'D', 1.0)
    graph.add_edge('E', 'D', 3.0).add_edge('E', 'C', 7.0)
    graph.add_edge('F', 'B', 6.0).add_edge('F', 'E', 3.0)

    print(graph)

    print("\nStarting DFS with Vertex A")
    for vertex in graph.dfs("A"):
        print(vertex, end="")
    print()

    print("\nStarting BFS with Vertex A")
    for vertex in graph.bfs("A"):
        print(vertex, end="")
    print()

    print("\nShortest path from vertex 'A' to 'F' using Djikstra’s shortest path algorithm:")
    path_length, path_vertices = graph.dsp("A", "F")
    print("Path length: ", path_length)
    print("Path: ", "".join(path_vertices))
    print(f"({int(path_length)}, {path_vertices})")

    print("\nShortest paths from 'A' to each other vertex:")
    all_paths = graph.dsp_all("A")
    print(all_paths)
    for dest, path_vertices in all_paths.items():
        print("{" + f"{dest}: {path_vertices}" + "}")


if __name__ == "__main__":
    main()
