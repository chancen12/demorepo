def divBySeven(m):
    
    arr=[]
  
    print("The List: ",m)
    for i in m:
        if(i%7==0):
            arr.append(i)
    return arr
x=input("Enter Comma separated numbers")
#print("the Numbers divisible by 7 are:",divBySeven(x))
arr2=x.split(",")
arr3=[]
for a in arr2:
    int(a)
    arr3.append(int(a))
print(arr3)
