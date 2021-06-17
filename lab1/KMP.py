import time

def KMP(string, pattern):
    startTime = time.time()
    operationsCount = 0

    t = pattern
    p = [0] * len(t)
    j = 0
    i = 1
    while i < len(t):
        if t[j] == t[i]:
            p[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                p[i] = 0
                i += 1
            else:
                j = p[j - 1]

    a = string
    m = len(t)
    n = len(a)
    i = 0
    j = 0
    while i < n:
        operationsCount += 1
        if a[i] == t[j]:
            i += 1
            j += 1
            if j == m:
                totalTime = time.time() - startTime
                return i-m, operationsCount, totalTime
        else:
            if j > 0:
                j = p[j - 1]
            else:
                i += 1

    if i == n and j != m:
        return -1, -1, -1
