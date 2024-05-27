code = input()
code_list = [char for char in code]
answer = ''

for c in code_list:
    asc = ord(c)
    if asc >= 65 and asc <= 77:
        asc += 13
    elif asc >= 78 and asc <= 90:
        asc -= 13
    elif asc >= 97 and asc <= 109:
        asc += 13
    elif asc >= 110 and asc <= 122:
        asc -= 13
    answer += chr(asc)

print(answer)