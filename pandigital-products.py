num1 = list(range(1,31428))
num2 = num1

#print(num1)
panDigi = []

def isPanDigi(num):
    digits = 0
    count = 0
    while(num > 0):
        tmp = digits
        if tmp  == (digits |= 1 << num%10):
            return false
        count+=1
        num /= 10
    return digits == 1 << count-1

print(isPanDigi(123456789))
'''

for i in num1:
    for j in num2:
'''
