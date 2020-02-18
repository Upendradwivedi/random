print("\t\t\t***************DICE GAME*****************")
print("do you want to continue-:")
ch=input("write Y for yes and N for no-:")
while(ch=='Y'):
    i=0
    COUNT=0
    count=0
    while(i<5):
        import random
        import time
        player=random.randint(1,6)
        ai=random.randint(1,6)
        print("IT'S YOUR CHANCE.....\n YOU ROLLED........")
        time.sleep(2)
        print("YOU ROLLED",player)
        print("IT'S COMPUTER CHANCE.....\n COMPUTER ROLLED.......")
        time.sleep(2)
        print("computer rolled",ai)
        if(player>ai):
            print("you win")
            COUNT=COUNT+1
        if(player<ai):
            print("computer win")
            count=count+1
        while(player==ai):
            print("its tie")
            print("game again")
            import random
            import time
            player=random.randint(1,6)
            ai=random.randint(1,6)
            print("IT'S YOUR CHANCE.....\n YOU ROLLED........")
            time.sleep(2)
            print("YOU ROLLED",player)
            print("IT'S COMPUTER CHANCE.....\n COMPUTER ROLLED.......")
            time.sleep(2)
            print("computer rolled",ai)
            if(player>ai):
                print("you win")
                COUNT=COUNT+1
            if(player<ai):
                print("computer win")
                count=count+1
        i=i+1
    print("your score is",COUNT)
    print("computer score is",count)
    if(COUNT>count):
        time.sleep(2)
        print("you win")
    if(COUNT<count):
        time.sleep(2)
        print("you loose computer win\nbetter luck next time")
       
    print("do you want to continue")
    ch=input("write Y for yes and N for no-:")
   
if(ch=='N'):
    print("see you next time")
    exit()
