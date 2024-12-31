# def Quick_Sort(list1):
#     if len(list1)<= 1:
#         return list1
#     else:
#         pivot = list1[0]
#         lesser = [x for x in list1[1:] if x<=pivot]
#         greter = [x for x in list1[1:] if x>pivot]

#         return Quick_Sort(lesser)+[pivot]+Quick_Sort(greter)

# mylist = [53,11,72,68,41,25,18,37,44,80]
# mylist = Quick_Sort(mylist)
# print(mylist)


def Quick_Sort(list1):
    if len(list1)<=1:
        return list1
    else:
        pivot = list1[0]
        lesser = []
        greter = []

        for x in list1[1:]:
            if x<=pivot :
                lesser.append(x)
            else:
                greter.append(x)
        return Quick_Sort(lesser)+[pivot]+Quick_Sort(greter)
    
mylist = [12,43,21,3,33,2,5,6,56]
mylist = Quick_Sort(mylist)
print(mylist)
