#include "iostream"

using namespace std;

int main() {
    int N, K;
    cin >> N >> K;
    int A[N];
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }
    int li[N+1];
    for (int i = 0; i < N; i++) {
        li[i+1] = li[i] + A[i];
    }
    int cnt = 0;
    for (int i = 0; i < N + 1; i++) {
        for (int j = 0; j < i; j++) {
            if (li[i] - li[j] == K) {
                cnt += 1;
            }
        }
    }
    cout << cnt << endl;
    return 0;
}
