from array import *

arr=array('i', [])

n = int(input("Eneter the length of the array:-"))
a=0

while a<n:
    for i in range(n):    
        x=int(input("Enter the {} array element".format(a+1)))
        a=a+1
        arr.append(x)
        
print(arr)
k=0
val=int(input("Enter the element you want to search the index value"))
for e in arr:
    if e == val:
        print(k)
        break
    k+=1
