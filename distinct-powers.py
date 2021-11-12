num1 = list(range(2,101))
num2 = num1
#print(num1)

ansList = []
for i in num1:
    for j in num2:
        k = i**j
        if k not in ansList:
            ansList.append(k)

answer = len(ansList)
print(answer)

