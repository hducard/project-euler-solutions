array = [0,1,32,243,1024,3125,7776,16807,32768, 59049, 100000]



# try combinations and check if sum of combinations == fifth-power sum of digits
# narrows the search range - 2^10 = 1024 combinations

answer = 0
aL = []
for i in range(1, 1000000):
    digit_sum = 0
    p_num = i
    while p_num > 0:
        digit_sum += array[int(p_num%10)]
        if digit_sum > i:
            break
        p_num = int(p_num/10)
    if digit_sum == i:
        answer += i
        aL.append(i)

print(answer)
print(aL)


