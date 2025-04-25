#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>
using namespace std;
// Note: translated from python to c++ by ChatGPT for efficiency

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, q;
    cin >> n >> q;
    
    // Build the tree as an adjacency list.
    vector<vector<int>> graph(n + 1);
    for (int i = 1; i < n; i++){
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    
    // Compute depth and immediate parent using BFS.
    vector<int> depth(n + 1, -1);
    vector<int> parent(n + 1, 0);
    int root = 1; // Choose node 1 as the root.
    depth[root] = 0;
    parent[root] = 0; // 0 indicates no parent.
    
    queue<int> qu;
    qu.push(root);
    
    while (!qu.empty()){
        int cur = qu.front();
        qu.pop();
        for (int nxt : graph[cur]){
            if (depth[nxt] == -1){
                depth[nxt] = depth[cur] + 1;
                parent[nxt] = cur;
                qu.push(nxt);
            }
        }
    }
    
    // Precompute binary lifting table.
    int max_power = floor(log2(n)) + 1;
    // dp[i][j] is the 2^j-th ancestor of node i.
    vector<vector<int>> dp(n + 1, vector<int>(max_power + 1, 0));
    for (int i = 1; i <= n; i++){
        dp[i][0] = parent[i];
    }
    
    for (int j = 1; j <= max_power; j++){
        for (int i = 1; i <= n; i++){
            dp[i][j] = dp[dp[i][j - 1]][j - 1];
        }
    }
    
    // Function to compute the LCA of two nodes.
    auto lca = [&](int a, int b) -> int {
        if (depth[a] < depth[b]) swap(a, b);
        int diff = depth[a] - depth[b];
        for (int i = 0; i <= max_power; i++){
            if (diff & (1 << i)){
                a = dp[a][i];
            }
        }
        if (a == b) return a;
        for (int i = max_power; i >= 0; i--){
            if (dp[a][i] != dp[b][i]){
                a = dp[a][i];
                b = dp[b][i];
            }
        }
        return parent[a];
    };
    
    // Process queries.
    for (int i = 0; i < q; i++){
        int a, b;
        cin >> a >> b;
        int ancestor = lca(a, b);
        int dist = depth[a] + depth[b] - 2 * depth[ancestor];
        cout << dist << "\n";
    }
    
    return 0;
}
