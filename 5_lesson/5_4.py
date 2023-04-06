data = [1,6,2,3,7,8,11,12]
data_sort = sorted(data)

big_list = []
small_list = []
for i in range(1,len(data_sort)):
    if data_sort[i-1] == (data_sort[i] - 1):
        small_list.append(data_sort[i-1])
        if i == (len(data_sort)-1):
            small_list.append(data_sort[i])
            big_list.append(small_list)
    else:
        small_list.append(data_sort[i-1])
        big_list.append(small_list)
        small_list=[] 

str_list = []  
big_str_list = []
for j in big_list:
    for k in range(len(j)):
        if k==0:
            str_list.append(str(j[k]))
            str_list.append("-")
        elif k==(len(j)-1):
            str_list.append(str(j[k]))
            big_str_list.append(str_list)
            str_list = []

itog = []        
for d in range(len(big_str_list)):
    if d < (len(big_str_list)-1):   
        for e in range(len(big_str_list[d])):
            itog.append(big_str_list[d][e])
            if e == (len(big_str_list[d])-1):
                itog.append(",")
            else:
                continue
    else:
        for e in range(len(big_str_list[d])):
            itog.append(big_str_list[d][e])    
            
#Это чтобы посмотреть промежуточные результаты
#print(data_sort)
#print(big_list)
#print(big_str_list) 

print(''.join(itog))
