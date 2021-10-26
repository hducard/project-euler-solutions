def sumOfSpiralDiagonals(n):
    #do something
    if (n%2) == 0:
        print("not possible")
    else:
        sum = 1
        for i in range(2,int((n+1)/2)+1):
            index = (2*i - 1)**2
            sum = sum + 4*index - 6*2*(i-1)
        return sum



answer = sumOfSpiralDiagonals(1001)
print(answer)
