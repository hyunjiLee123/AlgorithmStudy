a, b, c = map(int, input().split())
while (a!=0 and b!=0 and c!=0):
    l = [a, b, c]
    l.sort()

    if (l[2] >= l[0] + l[1]):
        print("Invalid")
    else:
        if (a==b and b==c and c==a):
            print("Equilateral")
        elif (l[0]==l[1] and l[2] != l[1]):
            print("Isosceles")
        elif (l[0] != l[1] and l[1]==l[2]):
            print("Isosceles")
        elif (l[0] != l[1] and l[1] != l[2]):
            print("Scalene")
    a, b, c = map(int, input().split())