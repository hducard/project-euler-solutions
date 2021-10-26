FibArray = [0,1]

def fibonacciNumber(n):
    if (n <=0):
        print("bad input. Recheck!")
    elif n <= len(FibArray):
        return FibArray[n-1]
    else:
        temp_fib = fibonacciNumber(n-1)+fibonacciNumber(n-2)
        FibArray.append(temp_fib)
        return temp_fib

#print(fibonacciNumber(10))

is1000digit = False
i = 3
while is1000digit == False:
    a = str(fibonacciNumber(i))
    if (len(a)) >=1000:
        print(a)
        print("Index is ", i)
        break
    else:
        i=i+1
