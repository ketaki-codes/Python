my_list=[] #empty list
print(my_list)

fruits=["apple","banana","Cherry"]#with items
print(fruits)

num=[10,20,30,40] #with index
print(num[0])
print(num[-2])

color=["red","blue"] #append
color.append("green")
print("After adding at last",color)

color.insert(1,"Yellow")#insert at specific location
print("After insertion at second position",color)

print("Before Remove",color)#remove element the last items
color.remove("red")
print("remove it before ",color)  

last_color=color.pop()#pop element at specific location
print(last_color)
print("It will remove at last ",color) 



