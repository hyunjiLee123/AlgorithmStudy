#include<iostream>
#include<algorithm>
#include<vector>
#include<limits>
using namespace std;
int dp[31][31];

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	for (int i = 1; i <= 30; i++)
		dp[1][i] = i;

	for (int i = 2; i <= 30; i++) {
		for (int j = i; j <= 30; j++) {
			for (int k = j - 1; k >= 1; k--) {
				dp[i][j] += dp[i - 1][k];
			}
		}
	}

	int t; cin >> t;
	while (t--) {
		int n, m; cin >> n >> m;
		cout << dp[n][m] << "\n";
	}
	return 0;
}