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
    return "*成功设置内容"

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
    return "*成功创建路径"

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
    return "*成功删除路径"
print("*PuDatabase Version1.0*")
print("*" + time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
print("*" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

if os.path.isfile("database.pud") == False:
    db = open("database.pud",mode="w")
    db.write(". ''''''")
    db.close()
    print("*ERROR*未找到数据库文件，已新建数据库*")
else:
    print("*已导入数据库'database.pud'*")

while 1:
    ins = input("*请输入指令：")

    if ins == "":
        ins = "pass"

    if ins[0] == ".":
        lins = ins.split(" ",2)

        if len(lins) == 1:
            print("*ERROR*请在路径后输入指令")
        elif lins[1] == "read":
            if icheckpath(lins[0]) == 0:
                print("*ERROR*未找到目标路径")
            else:
                print(iread(lins[0]))
        elif lins[1] == "set":
            if len(lins) < 3:
                print("*ERROR*未找到参数，请输入完整的参数")
            elif icheckpath(lins[0]) == 0:
                print("*ERROR*未找到目标路径")
            else:
                text = lins[2]
                if len(text.split("'''")) > 3:
                    print("*ERROR*一个文本最多可使用两个三单引号")
                elif len(text) < 6:
                    print("*ERROR*请使用三单引号括起文本，如：'''example'''")
                elif text[:3] != "'''" or text[-3:] != "'''":
                    print("*ERROR*请使用三单引号括起文本，如：'''example'''")
                else:
                    print(iset(lins[0],text))
        elif lins[1] == "mkdir":
            if len(lins) < 3:
                print("*ERROR*未找到参数，请输入完整的参数")
            elif icheckpath(lins[0]) == 0:
                print("*ERROR*未找到目标路径")
            else:
                dirname =lins[2]
                if dirname.find(" ") > -1 or dirname.find("/") > -1:
                    print("*ERROR*路径名不应含有' '或'/'")
                elif dirname == "":
                    print("*ERROR*路径名不应为空")
                elif dirname[-1] == ".":
                    print("*ERROR*路径名不应以根路径'.'结尾")
                else:
                    print(imkdir(lins[0],dirname))
        elif lins[1] == "ls":
            if len(lins) < 3:
                print("*ERROR*未找到参数，请输入完整的参数")
            elif icheckpath(lins[0]) == 0:
                print("*ERROR*未找到目标路径")
            else:
                method =lins[2]
                if method != "0" and method != "1" and method != "2" and method != "3":
                    print("*ERROR*无效的参数\n0-列出下一级路径名 1-列出下一级完整路径名 2-列出所有子路径路径名 3-列出所有子路径完整路径名")
                else:
                    print(ils(lins[0],method))
        elif lins[1] == "del":
            if icheckpath(lins[0]) == 0:
                print("*ERROR*未找到目标路径")
            elif lins[0] == "." or lins[0] == "./":
                print("*ERROR*根路径不能被删除")
            else:
                if input("*Warning*您确定要删除此路径与它所有的子路径吗？输入'1'以确定：") == "1":
                    print(idel(lins[0]))
                else:
                    print("*已取消删除")
    else:
        if ins == "exit":
            break
    print("")