norm_yr = [3,0,3,2,3,2,3,3,2,3,2,3]
leap_yr = [3,1,3,2,3,2,3,3,2,3,2,3]


day = 0
count = 0
for i in range(1901, 2001):
    if i % 4 != 0:
        # use normal year
        for k in norm_yr:
            day = (day+k)%7
            if day == 6 :
                count += 1
    else:
        if i % 400 != 0:
            #use normal year
            for k in norm_yr:
                day = (day+k)%7
                if day == 6 :
                    count += 1
        else:
            #use leap year
            for k in leap_yr:
                day = (day+k)%7
                if day == 6 :
                    count += 1

print(count)
