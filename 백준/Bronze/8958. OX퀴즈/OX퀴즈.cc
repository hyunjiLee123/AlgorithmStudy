#include <iostream>
#include <string>
using namespace std;

int main() 
{
    int n =0, score = 0, sum = 0;
    string str, score_array;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> str;
        
        for (int j = 0; j < str.length(); j++) {
            if (str[j] == 'O') 
            {
                score++;
                sum += score;
            }
            else if (str[j] == 'X')
            {
                score = 0;
            }
        }
        
        cout << sum << endl;
        sum = 0;
        score = 0;
    }
    return 0;
}