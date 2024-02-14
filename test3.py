import os
print(os.getcwd())

os.chdir("dir1")
print(os.getcwd())
print(os.listdir())

with open("file1.txt" , "w") as f:
    f.write("hola")
