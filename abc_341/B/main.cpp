#include <bits/stdc++.h>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++ (i))
#define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++ (i))
#define REP_R(i, n) for (int i = (int)(n) - 1; (i) >= 0; -- (i))
#define REP3R(i, m, n) for (int i = (int)(n) - 1; (i) >= (int)(m); -- (i))
#define ALL(x) ::std::begin(x), ::std::end(x)
using namespace std;


int64_t solve(int N, const std::vector<int64_t> &A, const std::vector<int64_t> &S, const std::vector<int64_t> &T) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int N;
    std::cin >> N;
    std::vector<int64_t> A(N), S(N - 1), T(N - 1);
    REP (i, N) {
        std::cin >> A[i];
    }
    REP (i, N - 1) {
        std::cin >> S[i] >> T[i];
    }
    auto ans = solve(N, A, S, T);
    std::cout << ans << '\n';
    return 0;
}
