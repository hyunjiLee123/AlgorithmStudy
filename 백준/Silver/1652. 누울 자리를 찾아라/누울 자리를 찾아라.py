N = int(input())
col = 0
row = 0
room = []
for i in range(N):
    l = input()
    room.append(l)

for j in range(N):
    c_count = 0
    r_count = 0
    for k in range(N):
        if room[j][k] == '.':
            c_count += 1
        else:
            c_count = 0
        if c_count == 2:
            col += 1

        if room[k][j] == '.':
            r_count += 1
        else:
            r_count = 0
        if r_count == 2:
            row += 1

print(col, row)