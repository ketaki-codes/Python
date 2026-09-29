arr=[5,12,15,19,20,2,8,16,45]
min=arr[0]
max=arr[0]
for num in arr:
    if num<min:
        
        min=num
    if num<max:
        
        max=num 
print("Mininum :" ,min)
print("Maxinum :" ,max)          
