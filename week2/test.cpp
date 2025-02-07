#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    
    vector<long long> prefix_sums(n, 0);
    long long sum = 0;
    
    for (int i = 0; i < n; i++) {
        sum += nums[i];
        prefix_sums[i] = sum;
    }
    
    if (sum % 3 != 0) {
        cout << 0 << endl;
        return 0;
    }
    
    long long sub_sum = sum / 3;
    int count = 0;
    
    for (int r1 = 0; r1 < n - 2; r1++) {
        for (int r2 = r1 + 1; r2 < n - 1; r2++) {
            if (prefix_sums[r1] == sub_sum && prefix_sums[r2] == sub_sum * 2) {
                count++;
            }
        }
    }
    
    cout << count << endl;
    return 0;
}