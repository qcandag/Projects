import random

start = 9
stop = 99
step = 3
limit = 8

list1 = [random.randint(start,stop) for iter in range(limit)]
list2, list3, list4 = list(),list(),list()

print("My list length is {}\n".format(len(list1)))
print("List1 (Orginal list):")
print(list1,"\n")

for i in range(len(list1)):
    if i == 0:
        list2.append(list1[i]+list1[i+1])
    elif i == len(list1)-1:
        list2.append(list1[i]+list1[i-1])
    else:
        list2.append(list1[i-1]+list1[i]+list1[i+1])

print("List2 (Sum of neighbors of List1):")
print(list2,"\n")    
for i in range(len(list1)):
    list3.append(list1[i])
    list3.append(list2[i])
    
print("List3 (List1 and List2 merged):")
print(list3,"\n")
    
liste = list()
for i in list3:
    if i % 2 == 0:
        liste.append(i)
   
list3 = liste
print("List3 with odd numbers removed:")
print(list3,"\n")


for i in range(int(len(list3)/2)+1):
    if len(list3) % 2 == 0:
        list4.append(list3[i]+list3[-(i+1)])
    else:
        if i == int(len(list3)/2):
            list4.append(list3[i])
        else:
            list4.append(list3[i]+list3[-(i+1)])

print("List4 (Summing List3 from two sides):")
print(list4,"\n")
liste = list()
for i in range(len(list4)):
    liste.append(max(list4))
    list4.remove(max(list4))
    
list4 = liste
print("List4 sorted in descending order:")
print(list4,"\n")

