lines = []
with open('input-p67.txt') as f:
     lines = f.readlines()
i = 0
for n in lines:
    lines[i] = n.split(" ")
    i = i+1

l_DP = [[int(lines[0][0])]]
i = 0

for n in lines[1:]:
    temp_list=[]

    for k in range(0,len(n),1):
        #print(k)
        if k == 0:
            temp_list.append(int(n[k])+l_DP[i][k])
        elif k == len(n)-1:
            temp_list.append(int(n[k])+l_DP[i][k-1])
        else:
            temp_list.append(max(int(n[k])+l_DP[i][k],int(n[k])+l_DP[i][k-1]))
    i = i+1
    l_DP.append(temp_list)

last_line = len(l_DP)
answer = max(l_DP[last_line-1])
print(answer)
