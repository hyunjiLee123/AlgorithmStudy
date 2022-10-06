#include <iostream>
using namespace std;

int main() {
	int a[9], maxn, n;
	for (int i = 1; i <= 9; i++) {
		cin >> a[i];
	}
	maxn = a[1];
	n = 1;
	for (int i = 1; i <= 9; i++) {
		if (maxn < a[i]) {
			maxn = a[i];
			n = i;
		}
	}
	cout << maxn << '\n' << n;
}