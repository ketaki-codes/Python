#1
students ={
101:{"Name":"Aditi","Scores":[78,85,90]},
102:{"Name":"Om","Scores":[30,20,42]},
103:{"Name":"Ram","Scores":[89,77,89]},
104:{"Name":"Mahi","Scores":[95,89,59]},
105:{"Name":"Neha","Scores":[48,50,20]},

}

#calculate average score and flag pass/fail
for sid ,details in students.items():
    avg=sum(details["Scores"])/len(details["Scores"])
    details["Average"] = avg
    details["Passed"] = avg >=50 #Boolean Flag

#print names of students who passed
print("Students who passed :")
for sid ,details in students.items():
    if details["Passed"]:   
        print(details["Name"])

#2
library ={

}  
 
#3 make a word from our name 
name = "KETAKI"
word = name[1] + name[3] + name[2]
print("Meaningful word:", word)

#4 replace all vowels from  name into z
name = "Ketaki"
for vowel in "aeiouAEIOU":
    name = name.replace(vowel, "z")
print(name)

#5 create a list of numbers and string accept the values from user sperate the list from max num display name in a decending order
names = []
numbers = []

n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter name: ")
    num = int(input("Enter number: "))

    names.append(name)
    numbers.append(num)

result = list(zip(numbers, names))
result.sort(reverse=True)
print("Names in descending order:")
for num, name in result:
    print(name, num)