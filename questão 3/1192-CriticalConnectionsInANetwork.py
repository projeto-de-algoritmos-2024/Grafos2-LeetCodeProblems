class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = {key:[] for key in range(n)}
        for node_a, node_b in connections:
            graph[node_a].append(node_b)
            graph[node_b].append(node_a)
        visited = [0] * n
        timestamp = visited[0] = 1
        ret = []
        def dfs(node, parent):
            nonlocal timestamp
            highest_reach = timestamp
            timestamp += 1
            for next_node in graph[node]:
                if not visited[next_node]:
                    visited[next_node] = timestamp
                    highest_reach = min(highest_reach, dfs(next_node, node))
                elif next_node != parent:
                    highest_reach = min(highest_reach, visited[next_node])
            if node != 0 and highest_reach == visited[node]:
                ret.append([node, parent])
            return highest_reach
        dfs(0, -1) 
        return ret