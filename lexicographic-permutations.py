def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)



i = [0,1,2,3,4,5,6,7,8,9]




perm_num = 999999

permutation_order=[]
num_of_variables = len(i)
print (num_of_variables)

for k in range(0,10):
    index = int(perm_num/factorial(num_of_variables-1))
    permutation_order.append(i[index])
    print(i[index])
    perm_num = perm_num%factorial(num_of_variables-1)
    num_of_variables = num_of_variables -1
    i.remove(i[index])

print("  ")
print(permutation_order)
