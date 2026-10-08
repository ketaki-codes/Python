print("Output of while loop")#while loops
count =0
while count < 5:
    print(count)
    count+=1

print("Output of for loop")#for loop
for i in range(5):
    print(i)  

#keyword of for loop

for i in range(5):#pass is use to pause,it do nothing,kind of placeholder 
    pass

print("Output of for loop")#continue keep the current iteration 
for i in range(5):
    if i == 2:
        continue
    print(i) 
    
    print("Output of for loop")# exits the loops
for i in range(5):
    if i == 2:
        break
    print(i) 

#loop else
print("Output of for loop with else")
for i in range(3):
    print(i)
else:
    print("loops finished without break"  ) 


