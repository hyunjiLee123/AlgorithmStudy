S = input()
answer = []

for cnt in range(1, len(S)):
    for s in range(len(S)):
        answer.append(S[s:s+cnt])

print(len(set(answer))+1)