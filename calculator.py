while(True):
    x=int(input("enter the first number:"))
    y=int(input("enter the second number:"))
    choice=int(input("""enter the chioice:
    1.addition
    2.subtraction
    3.multiplication
    4.division
    5.modulus
    6.exit()
    """))
    if choice==1:
        print("addition=",x+y)
    elif choice==2:
        print("subtraction=",x-y)
    elif choice==3:
        print("multiplication=",x*y)
    elif choice==4:
        print("division=",x/y) 
    elif choice==5:
        print("modulus=",x%y) 
    elif choice==6:
        exit()
    else:
        print("invalid choice")                 