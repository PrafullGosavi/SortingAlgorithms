def selection_sort(l):
    n = len(l)
    for i in range(n): # start form 0 index to 6
        min_item = i   # min is 0 index that is 64
        for j in range(i+1,n):  # start from the 1st index to 6.i.e. 35 to 14
            if l[j]<l[min_item]: #if index[1]<index[0] then goes in and swap
                min_item = j
        l[i],l[min_item] = l[min_item],l[i]

list1 = [64,35,89,21,72,13]
selection_sort(list1)
print(list1)