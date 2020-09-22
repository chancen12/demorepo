def example(m):
     
     
     return(list(set(m)))

arr3=[]
arr4=[]
arr5=[]
x=input("Enter array")
arr3=x.split(",")
for a in arr3:
    arr4.append(int(a))   
print(arr4.sort())

print("Sorted numbers are: ",arr4)
print("smallest number",arr4[0])
print("maximum number",arr4[-1])


 


example(x)
#example(x)
    
