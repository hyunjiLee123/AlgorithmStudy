a, b, c = map(int, input().split())
l = [a, b, c]
l.sort()

if (l[2] < l[0]+l[1]):
    print(a+b+c)
else:
    print(2*(l[0]+l[1])-1)