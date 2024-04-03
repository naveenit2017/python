import re
text="naveen This is naveen varma from Bengalore"

pattern="naveen"
search=re.search(pattern,text)
if search :
    print("pattern found ",search.group())
else :
    print("the required pattern not found")

txt="sai hello sai ram"
pattern1=r"sai" 

match = re.match(pattern1,txt)
if match :
    print("mtch found",match.group())

else :
    print("match not found")


    #match--> If the search pattern starting with that pattern
    #search -->If the search word is there in that particular line then it will dispaly 
    
text2 = "hello naveen varma garu"
patern = r"garu"
rep = "saiiiiii"
subst = re.sub(patern,rep,text2)
print("new modifed content",subst)