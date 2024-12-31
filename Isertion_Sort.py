def Insertion_sort(list1):
    n = len(list1)
    for i in range(1,n):
        temp = list1[i]
        j=i-1
        while j>=0 and temp<list1[j]:
            list1[j+1] = list1[j]
            j= j-1
        list1[j+1] = temp
    
l = [32,12,43,2,54,65,98,90]
Insertion_sort(l)
print(l)
print(len(l))