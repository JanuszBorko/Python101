import os

DIRECTORIO =  os.getcwd()

def CreateDir(x):

    if os.path.exists(os.path.join(os.getcwd(),x)) == False:
        os.mkdir(x)
        DIRECTORIO = os.path.join(os.getcwd(),x)
        os.chdir(DIRECTORIO)

    else:
        DIRECTORIO = os.path.join(os.getcwd(),x)
        os.chdir(DIRECTORIO)

CreateDir("Users")
USERS = os.getcwd()
print(DIRECTORIO)
User = input("Come te llamas? ")
CreateDir(User)

print(DIRECTORIO)

print(os.chdir("Tom"))


#check(User)

# if os.path.exists(DIRECTORIO):
#     print("no se puede")

