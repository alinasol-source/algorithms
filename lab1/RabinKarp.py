import time

def Rabin_Karp_Matcher(text, pattern):
    startTime = time.time()
    operationsCount = 0
    d = 1007
    q = 113
    n = len(text)
    m = len(pattern)
    h = pow(d, m-1) % q
    p = 0
    t = 0
    result = []
    for i in range(m):
        p = (d*p+ord(pattern[i])) % q
        t = (d*t+ord(text[i])) % q
    for s in range(n-m+1):
        operationsCount += 1
        if p == t:
            match = True
            for i in range(m):
                if pattern[i] != text[s+i]:
                    match = False
                    break
            if match:
                totalTime = time.time() - startTime
                result = s
        if s < n-m:
            t = (t-h*ord(text[s])) % q
            t = (t*d+ord(text[s+m])) % q
            t = (t+q) % q
    return result, operationsCount, totalTime
