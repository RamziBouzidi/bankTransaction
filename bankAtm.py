from UtilExprezz import negChecker
from zervicezDb import checkUzer,modifyUzer,createUser
from tkinter import Tk


data = {"name":"temporary","fullname":"temp","email_address":None,"money":None}

while True:
    print("Hello welcome to our bank What do you want?")
    print("1. Deposit")
    print("2. WithDraw")
    print("3. Info")

    try:
        number = int(input())
    except ValueError:
        print("Pleaze type a number")
    else:
        if number == 1:
            print("Pleaze depozit your cazh")
            break
        elif number == 2:
            print("How much would you like to withdraw")
            print("10\n20\n50\n100\n200\nCuzton value")
            anzwer = int(input())
            if anzwer:
                print("give me your name")
                name = input()
                if name:
                    data["name"] = name
                print("fullName?")
                fullname = input()
                if fullname:
                    data["fullname"] = fullname
                    print("email?")
                    emailo = input()
                    data["email_address"] = emailo
                    boo = checkUzer(name,fullname)
                    data["money"] = anzwer
                    
                    if boo == True:
                     manay =  modifyUzer(**data)
                     print(manay)
                        
                    else:
                        print("data baze doeznt exizt")
                        data["money"] = 0
                        createUser(data["name"],data["fullname"],data["email_address"],data["money"])
        elif number == 3:
            print("Pleaze go to thiz location that iz zhown on the zcreen for any further detailz")
            break

        





    