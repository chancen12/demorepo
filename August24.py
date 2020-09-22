def newArray(m,n):
    
    
    #print("The 1st List: ",m)
   #print("The 2nd List:",n)
    arr=[]
    arr1=[]
    for i in m:
        if(i%2==0):
            arr.append(i)
    for i in n:
        if(i%2!=0):
            arr.append(i)
    #return arr
x=input("Enter Array: ")
y=input("Enter Array:")
for d in x:
    x=int(d.split(","))
for e in x:
    y=int(e.split(","))
print("The 1st List: ",x)
print("The 2nd List:",y)

