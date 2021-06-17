import time

def boyer(string, pattern):
    startTime = time.time()
    operationsCount = 0
    t = pattern

    S = set()
    M = len(t)
    d = {}
    for i in range(M-2, -1, -1):
        if t[i] not in S:
            d[t[i]] = M-i-1
            S.add(t[i])
    if t[M-1] not in S:
        d[t[M-1]] = M
    d['*'] = M

    a = string
    N = len(a)
    if N >= M:
        i = M-1
        while(i < N):
            k = 0
            j = 0
            flBreak = False
            for j in range(M-1, -1, -1):
                operationsCount += 1
                if a[i-k] != t[j]:
                    if j == M-1:
                        off = d[a[i]] if d.get(a[i], False) else d['*']
                    else:
                        off = d[t[j]]
                    i += off
                    flBreak = True
                    break
                k += 1
            if not flBreak:
                totalTime = time.time() - startTime
                return i-k+1, operationsCount, totalTime
        else:
            return -1, -1, -1
    else:
        return -1, -1, -1

