#include <iostream>
using namespace std;

int main() {
	int n, x, num;
	int a[10000];
	cin >> n >> x;
	for (int i = 0; i < n; i++) {
		cin >> num;
		a[i] = num;
	}
	for (int i = 0; i < n; i++) {
		if (x > a[i]) cout << a[i] << " ";
	}
}