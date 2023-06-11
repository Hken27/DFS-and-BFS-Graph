from collections import defaultdict


class Kegiatan3:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        visited.add(v)
        print(v, end=" ")

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = set()
        self.dfs_util(start, visited)

    def bfs(self, start):
        visited = set()
        queue = []

        queue.append(start)
        visited.add(start)

        while queue:
            v = queue.pop(0)
            print(v, end=" ")

            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)


# objek graf
g = Kegiatan3()

# edge pada graf
g.add_edge(1, 2)
g.add_edge(1, 4)
g.add_edge(2, 1)
g.add_edge(2, 5)
g.add_edge(4, 6)
g.add_edge(5, 2)
g.add_edge(5, 3)
g.add_edge(5, 7)
g.add_edge(5, 9)
g.add_edge(6, 7)
g.add_edge(7, 6)
g.add_edge(7, 11)
g.add_edge(8, 9)
g.add_edge(8, 11)
g.add_edge(9, 5)
g.add_edge(9, 8)
g.add_edge(11, 10)
g.add_edge(11, 7)

print("DFS traversal: ")
g.dfs(1)

print("\nBFS traversal: ")
g.bfs(1)
