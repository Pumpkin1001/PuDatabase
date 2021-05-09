import os,time

def icheckpath(path):
    if path[-1] == "/":
        path = path[:-1]
    db = open("database.pud",mode="r")
    dball = db.read()
    dball = dball.split("\n")
    for line in dball:
        if line.find(path + " ") != -1:
            return 1
    return 0

def iread(path):
    if path[-1] == "/":
        path = path[:-1]
    db = open("database.pud",mode="r")
    dball = db.read()
    dball = dball.split("\n")
    for line in dball:
        if line.find(path + " ") != -1:
            line = line.split(" ",1)
            line = line[1]
            return line[3:-3]

def iset(path,text):
    if path[-1] == "/":
        path = path[:-1]
    db = open("database.pud",mode="r")
    dball = db.read()
    dball = dball.split("\n")
    new = ""
    for line in dball:
        if line.find(path + " ") != -1:
            line = line.split(" ",1)
            line = line[0] + " " + text
        new = new + line + "\n"
    new = new[:-1]
    db.close()
    db = open("database.pud",mode="w")
    db.write(new)
    db.close()
    return "*Set content successfully"

def imkdir(path,dirname):
    if path[-1] == "/":
        path = path[:-1]
    db = open("database.pud",mode="r")
    dball = db.read()
    dball = dball.split("\n")
    new = ""
    for line in dball:
        if line.find(path + " ") != -1:
            ident = line.split(".",1)
            ident = ident[0]
            line = line + "\n" + ident + "~" + path + "/" + dirname + " ''''''"
        new = new + line + "\n"
    new = new[:-1]
    db.close()
    db = open("database.pud",mode="w")
    db.write(new)
    db.close()
    return "*Successfully created path"

def ils(path,method):
    if path[-1] != "/":
        path = path + "/"
    db = open("database.pud",mode="r")
    dball = db.read()
    dball = dball.split("\n")
    pathls = ""
    for line in dball:
        if line.find(path) != -1:
            line = line.split(path)
            line = line[1]
            line = line.split(" ")
            line = line[0]
            if method == "0" and line.find("/") == -1:
                pathls = pathls + line + "\n"
            elif method == "1" and line.find("/") == -1:
                pathls = pathls + path + line + "\n"
            elif method == "2":
                pathls = pathls + line + "\n"
            elif method == "3":
                pathls = pathls + path + line + "\n"
    return pathls[:-1]

def idel(path):
    if path[-1] == "/":
        path = path[:-1]
    db = open("database.pud",mode="r")
    dball = db.read()
    dball = dball.split("\n")
    new = ""
    for line in dball:
        if line.find(path) != -1:
            line = line.split(" ",1)
            line = line[0]
            if line.find(path) == -1:
                new = new + line + "\n"
        else:
            new = new + line + "\n"
    new = new[:-1]
    db.close()
    db = open("database.pud",mode="w")
    db.write(new)
    db.close()
    return "*Successfully deleted path"
print("*PuDatabase Version1.0*")
print("*" + time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
print("*" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

if os.path.isfile("database.pud") == False:
    db = open("database.pud",mode="w")
    db.write(". ''''''")
    db.close()
    print("*ERROR*The database file was not found, a new database has been created*")
else:
    print("*Database imported'database.pud'*")

while 1:
    ins = input("*Please enter the instruction：")

    if ins == "":
        ins = "pass"

    if ins[0] == ".":
        lins = ins.split(" ",2)

        if len(lins) == 1:
            print("*ERROR*Please enter the command after the path")
        elif lins[1] == "read":
            if icheckpath(lins[0]) == 0:
                print("*ERROR*Target path not found")
            else:
                print(iread(lins[0]))
        elif lins[1] == "set":
            if len(lins) < 3:
                print("*ERROR*The parameter was not found, please enter the complete parameter")
            elif icheckpath(lins[0]) == 0:
                print("*ERROR*Target path not found")
            else:
                text = lins[2]
                if len(text.split("'''")) > 3:
                    print("*ERROR*A text can use up to two triple single quotes")
                elif len(text) < 6:
                    print("*ERROR*Please use triple single quotes to enclose the text, such as：'''example'''")
                elif text[:3] != "'''" or text[-3:] != "'''":
                    print("*ERROR*Please use triple single quotes to enclose the text, such as：'''example'''")
                else:
                    print(iset(lins[0],text))
        elif lins[1] == "mkdir":
            if len(lins) < 3:
                print("*ERROR*The parameter was not found, please enter the complete parameter")
            elif icheckpath(lins[0]) == 0:
                print("*ERROR*Target path not found")
            else:
                dirname =lins[2]
                if dirname.find(" ") > -1 or dirname.find("/") > -1:
                    print("*ERROR*The path name should not contain ' ' or '/'")
                elif dirname == "":
                    print("*ERROR*Path name should not be empty")
                elif dirname[-1] == ".":
                    print("*ERROR*The path name should not end with the root path'.'")
                else:
                    print(imkdir(lins[0],dirname))
        elif lins[1] == "ls":
            if len(lins) < 3:
                print("*ERROR*The parameter was not found, please enter the complete parameter")
            elif icheckpath(lins[0]) == 0:
                print("*ERROR*Target path not found")
            else:
                method =lins[2]
                if method != "0" and method != "1" and method != "2" and method != "3":
                    print("*ERROR*Invalid parameter\n0-List the next-level path name\n1-List the next-level full path name\n2-List all sub-path path names\n3-List all sub-path full path names")
                else:
                    print(ils(lins[0],method))
        elif lins[1] == "del":
            if icheckpath(lins[0]) == 0:
                print("*ERROR*Target path not found")
            elif lins[0] == "." or lins[0] == "./":
                print("*ERROR*The root path cannot be deleted")
            else:
                if input("*Warning*Are you sure you want to delete this path and all its subpaths? Enter '1' to confirm：") == "1":
                    print(idel(lins[0]))
                else:
                    print("*cancelled delete")
    else:
        if ins == "exit":
            break
    print("")