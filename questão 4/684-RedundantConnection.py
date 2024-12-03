class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        graph = defaultdict(set)
        for i in edges:
            graph[i[0]].add(i[1])
            graph[i[1]].add(i[0])
        keys = len(graph.keys())
        
        for i in edges[-1::-1]:
            graph[i[0]].remove(i[1])
            graph[i[1]].remove(i[0])
            l = []
            stack = [i[0]]
            visited = {i[0]}
            while stack:
                s = stack.pop()
                l.append(s)
                for j in graph[s]:
                    if j not in visited:
                        visited.add(j)
                        stack.append(j)
            if len(l)==len(graph.keys()):
                return i

            graph[i[0]].add(i[1])
            graph[i[1]].add(i[0])