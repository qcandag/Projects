
kelime = input("Lütfen bir cümle giriniz: ")

list3 = []
print("")
for i in kelime:
    list1 = []
    list2 = []
    list1.append(i)
    
    for k in list1:
        list2.append(ord(k))
    
    for j in list2:
        list3.append(j+3)
list4 = []
list5 = []
list6 = [] 
list7 = []   

for i in list3:
    list4.append(chr(i))
print(''.join(list4))

print("")

for tekrar in list4:
    list5.append(ord(tekrar))
    
for rakam in list5:
    list6.append(rakam-3)
    
for dongu in list6:
    list7.append(chr(dongu))
print(''.join(list7))
print("")
    
    



    
