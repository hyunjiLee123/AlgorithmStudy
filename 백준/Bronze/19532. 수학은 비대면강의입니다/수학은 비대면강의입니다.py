a, b, c, d, e, f = map(int, input().split())

answer_x = (c*e-f*b)/(a*e-b*d)
answer_y = (c*d-f*a)/(b*d-e*a)

print(int(answer_x), int(answer_y))