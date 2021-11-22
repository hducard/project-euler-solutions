array = []
with open('input-p22.txt') as f:
    array = f.readlines()
array = array[0].split(',')

array.sort()
print(array)


asciA = ord('A')
print("ascii A:", asciA)
answer = 0
for i in range(0, len(array)):
    sum = 0
    for letter in array[i]:
        if letter == '"':
            continue
        print(letter, ord(letter))
        sum += ord(letter) - asciA +1
    answer += (sum)*(i+1)

print(answer)


