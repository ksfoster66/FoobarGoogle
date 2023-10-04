def solution(x,y):
    x.sort()
    y.sort()
    length = len(x) if len(x) < len(y) else len(y)

    for i in range(length):
        if (x[i] != y[i]):
            if (len(y) > i + 1 and x[i] != y[i+1] ):
                return x[i];
            else:
                if (len(x) > i+1 and x[i+1] == y[i]):
                    return x[i]
            if (len(x) > i + 1 and y[i] != x[i+1] ):
                return y[i];
            else:
                if (len(y) > i+1 and y[i+1] == x[i]):
                    return y[i]

    if (len(x) > length): return x[length];
    if (len(y) > length): return y[length];

x = [13, 5, 6, 2, 5]
y = [5, 2, 5, 13]

res = solution(x, y)
print(res)