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

===========
import re
text="naaveen naveen varma how are you naaveen"
word="naaveen"
serch=re.match(word,text)
if serch :
    print("match found the searched ",serch.group())
else :
    print("The match not found")

text1 = "I am thinking to change my name as naveen" 
pat="naveen"
ot=text1.replace(pat,"varma")
print(ot)

mytext = "hello madam how are you wat are you doing"
opt=mytext.split(" ")
print("splited words are ",opt)

stext = "my name is anna"
ss=r"anna"
rr="naveen varma"
fot=re.sub(ss,rr,stext)
print(fot)