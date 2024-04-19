#algoritham
#1.Read input from the user ,input method will execute at runtime.
#2.use for loop to list the directories
#3.Identitfy module ,os
#

import os
list_folders=input("enter the folder with space separatore :").split( )

for folder in list_folders:
    try:
        files=os.listdir(folder)
    except FileNotFoundError:
        print("provide valide file  name")
print("=============================the list files under the :",folder)
for file in files:
        print(file)