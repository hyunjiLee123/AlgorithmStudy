def solution(code):
    answer = ''
    mode = 0
    for i in range(0, len(code)):
        if code[i] == '1':
            if mode == 0:
                mode = 1
                continue
            else:
                mode = 0
                continue
        if mode == 1:
            if i % 2 != 0:
                answer += code[i]
            else:
                continue
        if mode == 0:
            if i % 2 == 0:
                answer += code[i]
            else:
                continue
    if len(answer) == 0:
        answer = "EMPTY"
    return answer