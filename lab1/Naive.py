import time

def naive(string, pattern):
    patternIndex = []
    operationsCount = 0
    stringSize = len(string)
    patternSize = len(pattern)
    start = time.time()
    for i in range(stringSize - patternSize + 1):
        matchCount = 0
        for j in range(patternSize):
            r = i + j
            operationsCount += 1
            if string[r] == pattern[j]:
                matchCount += 1
            else:
                break
            if matchCount == patternSize:
                patternIndex.append(i)
                totalTime = time.time() - start
    return patternIndex, operationsCount, totalTime