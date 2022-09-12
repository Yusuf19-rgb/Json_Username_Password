# Muhammad Yusuf
# 5220600048

import json


print("LoginSystem @mvtthis")
myRL = input("Do you want to do a register?\n")


if myRL == "Register":
    User, PW = input("Username and Password\n").split()
    # PW = input("Password:")

    if(PW == PW):
        print("Registration successfully.\n")
        print("Username :", User)
        print("Password :", PW)
        
        with open('LoginSystemData.json', 'a') as f:      
                f.write("\n" + User + "," + PW)
                
    else:
        print("Registration failed! Please confirm your Password correctly.") 
