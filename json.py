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

#if myRL == "Login":
 #   User = input("Username:") 
  #  PW = input("Password:")
   # with open('LoginSystemData.json', 'r') as f: 
    #    readable = f.read() # --> you need to readable:str your file
     #   lines = readable.splitlines() # --> ['name,pw','name,pw','name,pw']
      #  user = list(filter(lambda l:l.split(',')[0] == User and l.split(',')[1] == PW,lines))
       # if user:
        #       print("Login successful")
        #else:
         #      print("Login failed. Wrong Username or Password.")     
        #f.close()