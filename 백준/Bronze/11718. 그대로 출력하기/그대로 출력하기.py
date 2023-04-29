while True:
    try:
        A = input()
        print(A)
        if (A == '\n'):
            break
    except EOFError:
        break