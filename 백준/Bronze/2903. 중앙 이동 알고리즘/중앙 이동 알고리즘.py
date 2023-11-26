a = 2
b = 1
answer = []
for i in range(16):
    a = a + b
    answer.append(a**2)
    b = b * 2

N = int(input())
print(answer[N-1])