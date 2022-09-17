#include <iostream>
using namespace std;

// C++을 사용하고 있고 cin/cout을 사용하고자 한다면, 
// cin.tie(NULL)과 sync_with_stdio(false)를 둘 다 적용해 주고, endl 대신 개행문자(\n)를 쓰자.

int main() {
	int t, a, b;
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> a >> b;
		cout << a + b << '\n';
	}
}