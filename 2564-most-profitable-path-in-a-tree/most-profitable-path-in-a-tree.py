class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        bob_time = {bob: 0}
        def find_bob_path(node, parent, time):
            if node == 0: 
                return True 
            for neighbor in tree[node]:
                if neighbor != parent:
                    bob_time[neighbor] = time + 1
                    if find_bob_path(neighbor, node, time + 1):
                        return True
            bob_time.pop(node) 
            return False
        find_bob_path(bob, -1, 0)
        max_profit = float('-inf')
        def dfs_alice(node, parent, time, profit):
            nonlocal max_profit
            if node in bob_time:
                bob_arrival = bob_time[node]
                if time < bob_arrival:  
                    profit += amount[node]
                elif time == bob_arrival:  
                    profit += amount[node] // 2
            else:
                profit += amount[node]  
            if len(tree[node]) == 1 and node != 0:
                max_profit = max(max_profit, profit)
                return
            for neighbor in tree[node]:
                if neighbor != parent:
                    dfs_alice(neighbor, node, time + 1, profit)
        dfs_alice(0, -1, 0, 0)  
        return max_profit