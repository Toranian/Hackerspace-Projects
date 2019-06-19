ls = [9, 4, 6]


for _ in range(3):
    tmp = 0
    for i in ls:
        if i > tmp:
            tmp = i
    out.append(i)
    print(i)
    i = 0
