from sqlalchemy.orm import Session
from sqlalchemy import update
from model import engine
from model import User
from model import Address
from sqlalchemy import select
import math

def createUser(name,fullname,email,money):
    with Session(engine) as session:
     perzon = User(
        name=name,
        fullname=fullname,
        addresses=[Address(email_address=email,money=money)],
    )
    session.add(perzon)
    session.commit()
    return True
    print(perzon)

def modifyUzer(**kwargs):
   with Session(engine) as session:
    uzerdata = {}
    for i, value in kwargs.items():
      if i != "money" and i !="email_address":
        uzerdata[i] = value
    val = update(User).where(User.name == kwargs["name"]).values(uzerdata).returning(User.id)
    uzer = session.execute(val).scalar() 
    session.commit()
    getMoneyRezult = select(Address).join(User).where(User.name == kwargs["name"]).where(User.fullname == kwargs["fullname"])
    finalMoney = session.execute(getMoneyRezult).scalar() 
    finalmoney2 = abs(int(finalMoney.money) + int(kwargs["money"]))
    kwargs["money"] = finalmoney2
    session.commit()
    updateMoney = update(Address).where(Address.id == uzer).values(money = kwargs["money"])
    session.execute(updateMoney)
    session.commit()
    return finalmoney2

def checkUzer(name,fullname):
  with Session(engine) as session:
    user = session.scalar(
            select(User)
            .where(User.name == name)
            .where(User.fullname == fullname)
            .limit(1)
        )
    
    if user:
      return True
    



    
   
         
    
