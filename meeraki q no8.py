import json
list1=["neelam","programer","24","2400"]
list2=["komal","trainer","24","20000"]
list3=["anuradha","HR","25","40000"]
list4=["Abhishek","manager","29","63000"]
keys=["name","designation","age","salary"]
k={}
m={}
n={}
d={}
var=({"k":k,"m":m,"n":n,"d":d})
for i in range (len(list1)):
        k.update({keys[i]:list1[i]})
for j in range(len(list2)):
        m.update({keys[j]:list2[j]})
for p in range(len(list3)):
        n.update({keys[p]:list3[p]})
for f in range(len(list3)):
        d.update({keys[f]:list4[f]})
with open("meeraki q no8",'w')as g:
        json.dump(var,g,indent=2)



# n=input("enter the name-:")
# i=0
# c = 0
# while i< len(n):
#     if n[i] == "a":
#         c+=1
#     i=i+1
# if c >1:
#     print("yes")
# else:
#     print("no")


# i=1
# while i<30:
#     if i**3<30:
#         print(i,i**2)
#     i=i+1


# import json
# emp1={ "name":"nilam",
#        "Designation":"programmer",
#        "Age":"34",
#        "salary":"24000",}
# emp2={ "name":"komal",
#         "Designation":"Trainee",
#         "Age":"24",
#         "salary":"20000" ,}
# emp3={ "name":"anuradha",
#          "Designation":"HR",
#          "Age":"25",
#          "salary":"40000",}
# emp4={ "name":"Abhishek",
#          "Designation":"Manager",
#          "Age":"29",
#          "salary":"63000"}
# k=json.dumps(emp1)
# m=json.dumps(emp2)
# l=json.dumps(emp3)
# o=json.dumps(emp4)
# print(k)
# print(m)
# print(l)
# print(o)
 