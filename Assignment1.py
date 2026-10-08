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