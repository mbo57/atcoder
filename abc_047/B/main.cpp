#include <bits/stdc++.h>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++ (i))
#define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++ (i))
#define REP_R(i, n) for (int i = (int)(n) - 1; (i) >= 0; -- (i))
#define REP3R(i, m, n) for (int i = (int)(n) - 1; (i) >= (int)(m); -- (i))
#define ALL(x) ::std::begin(x), ::std::end(x)
using namespace std;


int64_t solve(int64_t W, int64_t H, int N, const std::vector<int64_t> &x, const std::vector<int64_t> &y, const std::vector<int64_t> &a) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int64_t W, H;
    int N;
    std::cin >> W >> H >> N;
    std::vector<int64_t> x(N), y(N), a(N);
    REP (i, N) {
        std::cin >> x[i] >> y[i] >> a[i];
    }
    auto ans = solve(W, H, N, x, y, a);
    std::cout << ans << '\n';
    return 0;
}