array = [1,1,2,6,24,120,720,5040,40320, 362880, 3628800]

answer = 0
aL = []

for i in range(1, 10000000):
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


