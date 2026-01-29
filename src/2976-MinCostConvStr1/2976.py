#Solution
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = float('inf')
        dist = [[INF] * 26 for _ in range(26)]

        for i in range(26):
            dist[i][i] = 0

        for o, c, w in zip(original, changed, cost):
            v = ord(o) - ord('a')
            u = ord(c) - ord('a')
            dist[v][u] = min(dist[v][u], w)

        for k in range(26):
            for i in range(26):
                if dist[i][k] < INF:
                    dik = dist[i][k]
                    for j in range(26):
                        if dist[k][j] < INF:
                            dist[i][j] = min(dist[i][j], dik + dist[k][j])
        
        total = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            u, v = ord(s) - ord('a'), ord(t) - ord('a')
            if dist[u][v] == INF:
                return -1
            total += dist[u][v]
        return total
