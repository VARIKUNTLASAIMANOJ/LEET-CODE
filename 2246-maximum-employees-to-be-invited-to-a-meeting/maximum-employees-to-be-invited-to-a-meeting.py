class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        in_degree = [0] * n
        for f in favorite:
            in_degree[f] += 1
        queue = deque()
        longest_chain = [1] * n
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
        while queue:
            node = queue.popleft()
            fav = favorite[node]
            longest_chain[fav] = max(longest_chain[fav], longest_chain[node] + 1)
            in_degree[fav] -= 1
            if in_degree[fav] == 0:
                queue.append(fav)
        visited = [False] * n
        longest_cycle = 0
        sum_of_mutual_chains = 0
        for i in range(n):
            if visited[i]: 
                continue
            cycle_nodes = set()
            current = i
            while current not in cycle_nodes and not visited[current]:
                cycle_nodes.add(current)
                visited[current] = True
                current = favorite[current]
            if current in cycle_nodes:
                cycle_length = 0
                start = current
                while True:
                    cycle_length += 1
                    current = favorite[current]
                    if current == start:
                        break
                if cycle_length == 2:  
                    a, b = start, favorite[start]
                    sum_of_mutual_chains += longest_chain[a] + longest_chain[b]
                else:
                    longest_cycle = max(longest_cycle, cycle_length)
        return max(longest_cycle, sum_of_mutual_chains)