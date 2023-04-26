str = input()
for s in range(len(str)):
    if str[s].islower():
        print(str[s].upper(), end='')
    else:
        print(str[s].lower(), end='')