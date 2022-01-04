# -*- coding: utf-8 -*-
"""

@author: Yudhis
"""

def fibonaci(num):
    n1=0
    n2=1 
    count=0
    list=[]
    while count < num:
        list.append(n1)     #masukkan bilangan kedalam  list
        temp = n1 + n2      #inisiasi bilangan selanjutnya
        n1 = n2             #ubah n1 menjadi n2
        n2 = temp           #ubah n2 menjadi temp
        count += 1          #tambahkan batasan
        
    for i in range(len(list)):
        return list

num = int(input("input number: "))

a = fibonaci(num)
print(a)

# while count < num:
#     list.append(n1)
#     temp = n1 + n2
#     n1 = n2
#     n2 = temp
#     count += 1
    
# for i in range(len(list)): print(list[i])