from pathlib import Path
import os

def readfileandfolder():
    path = Path(' ')
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")


def createFile():
    readfileandfolder()
    name = input("enter the name of the file")
    p = Path(name)
    with open(p,"w") as fs:
        data = input("what you want to write")
        fs.write(data)


    print("file created sucessfully")

def readfile():
    readfileandfolder()
    name = input("which fiel you want to read ")
    p = Path(name)
    if p.exists() and p.is_file():
        with open(p,'r') as fs:
            data = fs.read()
            print(data)
        print("read sucessfully")
    else:
        print("file does not exist")
def updatefile():
    readfileandfolder()
    name = input("which file you want to update")
    p = Path(name)
    if p.exists() and p.is_file():
        print("press 1 for changing the name of your file")
        print("press 2 for overwriting the data of your file")
        print("press 3 for appending some content in the file")
        res = int(input("tell your response"))
        if res == 1:
            name2 = input("tell your new file name")
            p2 = Path(name2)
            p.rename(p2)
        if res == 2:
            with open(p,'w') as fs:
                data = input("this will overwrite data")
                fs.write(data)
        if res == 3:
            with open(p,'a') as fs:
                data = input("what you want to append")
                fs.write(data)
def deleteFile():
    readfileandfolder()
    name = input("which file you want to delete ")
    p = Path('')
    if p.exists() and  p.is_file():
        os.remove(p)
        print("file removed sucessfully")
    else:
        print("no such file exist")


print("press 1 for create a file")
print("press 2 for reading in a file")
print("press 3 for updating a file")
print("press 4 for delete a file")

check = int(input("what do you want to do?"))

if check == 1:
    createFile()
if check == 2:
    readfileandfolder()
if check == 3:
    updatefile()

if check == 4:
    deleteFile()