N = int(input())
log = {}
for i in range(N):
    a, b = input().split()
    if b == 'enter':
        log[a] = True
    else:
        del log[a]

log = sorted(log.keys(), reverse=True)

for ans in log:
    print(ans)