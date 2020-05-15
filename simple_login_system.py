#login system without gui
import getpass as gp
logic=True
fd=open("login_info.txt","a")
while logic is True:
    email=input("Please enter email address:")
    if email.find('@')==-1 or  email.find(".com")==-1:
        print("Please enter proper email address:")
        continue
    else:
        logic=False
        break
logic = True
while logic is True:   
    password = gp.getpass("Please enter a password:")
    if len(password) < 6:
        print("Please enter a password of length 6 char or more:")
        continue
    else:
        logic = False
        break
fd.write(email)
fd.write('\n')
fd.write(password)
