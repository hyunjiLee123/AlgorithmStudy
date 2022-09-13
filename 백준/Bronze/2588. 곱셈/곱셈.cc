#include <iostream>
using namespace std;

int main() {
	int a, b;
	cin >> a >> b;
	int c, d, e;
	c = b % 10;
	d = (b % 100) / 10;
	e = b / 100;
	cout << a * c << endl;
	cout << a * d << endl;
	cout << a * e << endl;
	cout << (a * c) + (a * d * 10) + (a * e * 100) << endl;
}