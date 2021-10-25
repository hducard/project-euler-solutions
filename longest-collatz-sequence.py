def nCollatz(a):
    numCollatz = 0
    if a <= 1:
        return numCollatz
    else:
        while a > 1:
            #print(a)
            if (a % 2) == 0:
                a = (int) (a/2)
            else:
                a = (3*a)+1
            numCollatz = numCollatz +1
    return numCollatz
#print(nCollatz(1))

### imporvement can be done wherein pre-calculated values are stored in a dictionary/map



largest_collatz = 0
answer_num = 0
for i in range(1000000,1,-1):
    collatz_id = nCollatz(i)
    if collatz_id > largest_collatz:
        largest_collatz = collatz_id
        answer_num = i
print (answer_num)

