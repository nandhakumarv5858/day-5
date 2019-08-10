import re
a =input("Enter your password")
c =True
while c:
    if (len(a)<6 or len(a)>13):
        break
    elif not re.search("[a-z]",c):
        break
    elif not re.search("[A-Z[",c):
        break
    elif not re.search("[0-9]",c):
        break
    elif not re.search("[$#@]",c):
        break
    else:
        print("Valid password")
        x=False
        break
if c:
    print("Invalid password")
