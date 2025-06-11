a, b = map(int, input().split())
A = a
B = b

while (b > 0):
    temp = b
    b = a % b
    a = temp

print(A*B//a)

