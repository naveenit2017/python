#File read and operations
#with open("/tmp/1.txt","w")
#with open("/tmp/1.txt","r")

def update_config(file_path,key,value):
    
    with open(file_path,"r") as file:
        lines=file.readlines()
    
    with open(file_path,"w") as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")

            else:
                file.write(line)


update_config("server.conf","MAX_CNNECTIONS","1000")

