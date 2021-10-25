import math

###
def isPalindrome(a):
    return a == a[::-1]
###


###
import timeit


#Your statements here

###


maxlimit = 1000000

candidate =  (int) (math.sqrt(maxlimit))

candidate = candidate - (candidate%11)

start = timeit.default_timer()
## run loop with two numbers wherein candidate is reduced by 11 and other number by 1
maxAns = 1
for i in range(100,999,1):
    #print(i)
    for j in range(110,990,11):
        #print (j)
        mult = i*j
        if mult > maxAns and isPalindrome(str(mult)):
            maxAns = mult

stop = timeit.default_timer()

print('Time: ', stop - start)

print (maxAns)
