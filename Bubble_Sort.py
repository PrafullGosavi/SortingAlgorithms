def bubble_sort(data_list):
    for r in range(1,len(data_list)):
        for i in range(len(data_list)-r):
            if data_list[i]>data_list[i+1]:
                data_list[i],data_list[i+1] = data_list[i+1],data_list[i]


l = [78,65,32,12,34,42,11]
bubble_sort(l)
print(l)
print(len(l))