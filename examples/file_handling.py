'''
Reading wrting,deleting,creating of a files is called file handling,
open->open()
read/write
close
modes:
r-read
w-write
r+-read,write
w+-write ,read
seek(0) --cursor move from file to terminal
'''
s = open('sample.txt',mode='r+')
print(s.read())
print("\n")
s.write("this is my latest updated file")
print(s.read())
s.close()