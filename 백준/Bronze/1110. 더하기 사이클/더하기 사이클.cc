#include <iostream>
using namespace std;
int main() {
	int n, a, b, c;
	int cnt = 0;
	int temp = 100;
	cin >> n;
	a = n / 10;
	b = n % 10;
	while (temp != n) {
		c = (a + b) % 10;
		
		temp = b * 10 + c;
		cnt += 1;
		a = temp / 10;
		b = temp % 10;
	}
	cout << cnt << endl;
}