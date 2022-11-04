combination = [2,0,1,3]
flag = 0
c = 0
s_l = 2
l = 4
c_e = c+s_l
while c < s_l: #filter for take before deliver
    for i in range(l):  #search for the first start location
        if combination[i] == c:
            start_p = i
        elif combination[i] == c_e:
            end_p = i 
    if start_p > end_p:
        print('remove')
        break
    c += 1
    c_e = c+s_l