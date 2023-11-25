N, B = map(int, input().split())
l = []
answer = ''
while (N >= B):
    n = N % B
    l.append(n)
    N = N // B
l.append(N)
l.reverse()

for num in l:
    if num >= 10:
        num = num + 55
        print(chr(num), end='')
    else:
        print(str(num), end='')