import time
import os

cmd = os.listdir("./start")

for i in range(len(cmd)):
    print(i+1,":",cmd[i])

user = input("SHELL>")

try:
    int(user)
    it_is = True
except ValueError:
    it_is = False

if it_is :
    user = int(user) 
    if user > len(cmd) : 
        print("-[!]incorect number-")
    else :
        user = user - 1
        os.system("start start\\"+cmd[user])