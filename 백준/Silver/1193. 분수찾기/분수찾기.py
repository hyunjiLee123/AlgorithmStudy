x = int(input())
line = 1
a = 1
b = 1

while(x > line):
    x -= line
    line += 1

#line이 곧 main num
if line % 2 == 0:   #짝수
    a = x
    b = line - x + 1
else:
    a = line - x + 1
    b = x

answer = str(a) + '/' + str(b)

print(answer)