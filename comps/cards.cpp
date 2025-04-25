#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    vector<int> cards(n);
    for (int i = 0; i < n; i++) {
        cin >> cards[i];
    }
    
    long long sum = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (cards[i] < cards[j]) {
                sum += cards[i] + cards[j];
            }
        }
    }
    
    cout << sum << endl;
    return 0;
}
