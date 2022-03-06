import random
Cnumber=random.randrange(1,101)
userinput=int(input("Enter your number....."))
if userinput >  Cnumber:
    print("computer Number",Cnumber)
    print("your guess number is too high")
elif Cnumber>userinput :
     print("computer Number ",Cnumber)
     print("your number is too low")
else:
    print("computer Number",Cnumber)
    print("your guess number is equal")
