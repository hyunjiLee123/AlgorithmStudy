num = 0
N, B = input().split()
l = list(N)
for i in range(len(l)):
    if ord(l[i]) <= 57 and ord(l[i]) >= 48:
        num = num + int(l[i]) * (int(B)**(len(l)-1-i))
    else:
        n = ord(l[i]) - 55
        num = num + n * (int(B)**(len(l)-1-i))

print(num)