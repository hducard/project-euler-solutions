lines = []
with open('input-p13.txt') as f:
    lines = f.readlines()
sumTotal = 0
for strnum in lines:
    sumTotal = sumTotal + (int) (strnum)
print(sumTotal)
