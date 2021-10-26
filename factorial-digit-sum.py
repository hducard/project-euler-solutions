def calcFactorial(n):
    if n == 1:
        return n
    else:
        return n*calcFactorial(n-1)

numFac = calcFactorial(100)
print(numFac)
d= list(str(numFac))
d = [int(i) for i in d]
answer = sum(d)
print(answer)
