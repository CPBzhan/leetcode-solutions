#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll INF = 1e18;

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<pair<int,int>>> graph(n);
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        graph[u].push_back({v, w});
    }

    vector<ll> dist(n, INF);
    dist[0] = 0;

    priority_queue<
        pair<ll,int>,
        vector<pair<ll,int>>,
        greater<pair<ll,int>>
    > pq;

    pq.push({0, 0}); // (distance, node)

    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();

        // 如果这个状态已经不是最优，丢掉
        if (d > dist[u]) continue;

        // 用 u 去松弛它的所有出边
        for (auto [v, w] : graph[u]) {
            if (dist[v] > dist[u] + w) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }

    // dist[i] 就是 0 → i 的最短路
}

/*
vector<bool> vis(n, false);
        vector<int> dist(n, 1e9);
        
        priority_queue<pair<int,int> > Q;
        Q.push({0, 0});
        dist[0] = 0;
        while(!Q.empty()){
            int u = Q.top().second;
            Q.pop();
            if(vis[u]) continue;
            vis[u] = true;
            for(auto [v, w] : G[u]){
                if(dist[u] + w < dist[v]){
                    dist[v] = dist[u] + w;
                    Q.push({-dist[v], v});
                }
            }
        }
        return dist[n - 1] == 1e9 ? -1 : dist[n - 1];
*/