#include <iostream>
using namespace std;

int main() {
	int n, a[1000000], minn, maxn;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	minn = a[0];
	maxn = a[0];
	for (int i = 0; i < n; i++) {
		if (a[i] < minn) minn = a[i];
		if (a[i] > maxn) maxn = a[i];
	}
	cout << minn << " " << maxn;
}