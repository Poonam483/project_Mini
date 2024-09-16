import random
list=["rock","paper","scissors"]
while("True"):
    ucount=0
    ccount=0
    user=int(input('''
        Game start....
        1.YES
        2.NO | Exit                    
        '''))
    if user==1:
        n=int(input("Enter the number of rounds you play:"))
        for i in range(n):
            user=int(input('''enter a userchoice:
                1.rock
                2.paper
                3.scissors
                4.exit()    
                '''))
            comp=random.randint(1,3) 
            print("userchoice:",user)
            print("computerchoice:",comp)
            if user==comp:
                print("It's Tie")
            elif (user==2 and comp==1) or (user==3 and comp==2) or (user==1 and comp==3):
                print("You Won")
                ucount=ucount+1
                print("Your score:",ucount)
            elif (comp==2 and user==1) or (comp==3 and user==2) or (comp==1 and user==3):
                print("You Loose")
                ccount=ccount+1
                print("Comp score:",ccount)
            else:
                exit()
        if ucount> ccount:
            print("YOU ARE WINNER OF THE GAME")
        elif ucount<ccount:
            print("YOU DON'T WIN THE GAME") 
        else:
            print("NOBODY WIN THE GAME")           
    else:
        break





