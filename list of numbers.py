lst=[]
n=int(input("enter the number of elements : "))
for i in range (0,n):
    elements=int(input())
    lst.append(elements)
print(lst)
a=lst
for num in a :
    if num >= 0:
        print("output : ",num)
    
