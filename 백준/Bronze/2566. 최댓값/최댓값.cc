#include <iostream>
using namespace std;

int main() {
	int col, row;
	int max = 0;
	int a[9][9];
	//입력받기
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			cin >> a[i][j];
		}
	}
	//최대값 max찾고, 그때 i+1, j+1값 col, row에 넣기
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			if (a[i][j] >= max) {
				max = a[i][j];
				col = i + 1;
				row = j + 1;
			}
		}
	}
	//max, col, row출력
	cout << max << endl;
	cout << col << " " << row;
}