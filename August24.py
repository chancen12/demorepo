def newArray(m,n):
    
    
    print("The 1st List: ",m)
    print("The 2nd List:",n)
    arr=[]
    for i in m:
        if(i%2==0):
            arr.append(i)
    for i in n:
        if(i%2!=0):
            arr.append(i)
    return arr
x=[14,34,28,73,71,32,43]
y=[3,11,28,70,16,23,42]
print("the Numbers are:",newArray(x,y))

