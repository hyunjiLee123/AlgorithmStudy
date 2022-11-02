#include <iostream>
using namespace std;

int main() {
	int n;
	int aa = 0;
	int a[31] = { 0, };
	int v[2] = { 0,0 };
	//입력받고, 숫자 있는거는 1로 바꾸기
	for (int i = 0; i < 28; i++) {
		cin >> n;
		a[n] = 1;
	}
	//a가 0인 i를 v에 넣기
	for (int i = 1; i <= 30; i++) {
		if (a[i] == 0) {
			v[aa++] = i;
		}
	}
	
	//오름차순으로 출력
	if (v[0] > v[1]) {
		cout << v[1] << '\n' << v[0];
	}
	else {
		cout << v[0] << '\n' << v[1];
	}
}