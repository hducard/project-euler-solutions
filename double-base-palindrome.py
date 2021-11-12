# Runtime can be significantly reduced by pruning search space wherein
# I need to geenrate base10 palindromes and check



answer = 0

ansL = []
#for i in range(2,1000001):
for i in range(1,1000001):
    # check if number is palindrome
    istr= str(i)
    if istr != istr[::-1]:
        continue
    ibin = ''
    temp_num = i
    while temp_num > 0:
        ibin = str(temp_num%2)+ibin
        temp_num = int(temp_num/2)
    if ibin != ibin[::-1]:
        continue

    answer += i
    ansL.append([i, ibin])


    # check if binary number is palindrom
    #add to answer

print(answer)
print(ansL)


