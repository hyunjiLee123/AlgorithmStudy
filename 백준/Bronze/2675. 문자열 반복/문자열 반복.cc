#include <iostream>
using namespace std;

int main() {
	int t, r;
	string s;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> r >> s;
		for (int j = 0; j < s.size(); j++) {
			//반복출력
			for (int k = 0; k < r; k++) {
				cout << s[j];
			}
		}
		cout << '\n';
	}
}