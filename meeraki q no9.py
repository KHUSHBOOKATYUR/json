import json
TXT= '''name simran
class 12
roll no 4
subject maths
school  goverment 
''' 
list1 = []
list2 = []
k = ""
c = 0
for i in TXT:
    if i == " ":
        k+=i
        c+=1
        if c == 1 :
            list1.append(k)
            k=""
    elif i == "\n":
        list2.append(k)
        k=""
        c=0
    else:
        k+=i
dict1 = {}
i = 0
while i < len(list1):
    dict1[list1[i]] = list2[i]
    i+=1
print(dict1)
with open("khu.json","w") as f :
    json.dump(dict1,f,indent=4)