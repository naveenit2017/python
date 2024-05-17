'''
we can define dictionary {}
it will follow the key,value structure
it won't support the indexing
keys are immutable 
keys are unique
'''
d={
    1:"naveen",
    2:"sai",
    3:"raji",
    "jobs":"IT"
}
print(d)
print(type(d))
for i ,j in d.items():
    print(i,j)

d.update({1:"navee"})
#print(d)
#print(d.get("jobs"))
#print(d.pop("jobs"))
#print(d)
students_info=[
    {"name":"naveen",
     "no":"107",
     "marks":1000
     },
      {"name":"sai",
     "no":"108",
     "marks":100
     },
      {"name":"raji",
     "no":"109",
     "marks":1100
     }
     ]
print(type(students_info))
for i in students_info:
    print(i["name"])


