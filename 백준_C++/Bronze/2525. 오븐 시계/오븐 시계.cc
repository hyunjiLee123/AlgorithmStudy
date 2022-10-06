#include <iostream>
using namespace std;

// m+t가 60분이거나 넘을 때 -> h는 (m+t)/60의 몫만큼 증가, m은 (m+t)/60의 나머지가 되야함
// m+t가 60분 안넘을 때 -> h 증가 없고, m=m+t하면 됨


int main() {
	int h, m, t;
	cin >> h >> m >> t;

	if (m + t >= 60) {
		h += (m + t) / 60;
		m = (m + t) % 60;
		if (h >= 24) h -= 24;
	}
	else {
		m += t;
	}
	cout << h << " " << m;
}