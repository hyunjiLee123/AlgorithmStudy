x = int(input())
arr = [[0 for _ in range(101)] for _ in range(101)]         # **2차원 배열 선언하기
answer = 0

for i in range(x):
    a, b = list(map(int, input().split()))

    for row in range(a, a+10):
        for col in range(b, b+10):
            arr[row][col] = 1

for a in arr:
    answer += a.count(1)            # a.count(x) : 배열 내 x 개수 세는 방법

print(answer)