lst = [1, 2, 2, 3, 4, 4, 5] # list created

new_list = []

for i in lst:  # taking list in i
    if i not in new_list: #remove the duplicates
        new_list.append(i) #add a list 

print(new_list) #list printed