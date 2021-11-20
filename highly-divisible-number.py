
import numpy as np
'''

num = 2
maxN = 2
primes=[1]
while maxN <= 500:
    count = 1
    tsum = (num*(num+1))/2
    for i in primes:
        if i == 1:
            count += 1
        else:
            j = i
            while(j < tsum):
                j *= i
                count += 1

    if count == 1:
        print("primes: ", primes)
        primes.append(num)
    if count > maxN:
        print(maxN, num)
        maxN = count
    num += (num+1)
'''
num = 3
tsum = 6
primes = [2,3]
maxDiv = 4

while maxDiv <= 500:
    num += 1
    tsum += num
    # find all primes upto tsum
    for i in range(primes[-1]+1, num+1):
        notDiv = True
        for j in primes:
            if notDiv == False:
                break
            if i % j == 0:
                notDiv = False
                continue
        if notDiv == True:
            primes.append(i)

    primeArrNum=[]
    #print(num, primes)
    for prime in primes:
        if tsum % prime == 0:
            it = prime
            expt = 1
            while(tsum%it == 0):
                expt += 1
                it *= prime
            primeArrNum.append(expt)
    # print(primeArrNum)
    count = np.prod(primeArrNum)
    if count > maxDiv:
        maxDiv = count
        print("Update: ", maxDiv, num)



print("MaxDiv ",maxDiv," num ", num," tsum ", tsum)

