import random
i=0
n=int(input("how many games"))
guess=['stone','paper','scissor']
while i<n:
    myguess=input("enter your guess :")
    p=random.randint(0,2)

    if myguess=="stone" or myguess=="scissor" or myguess=="paper":
        print("computer's guess :", guess[p])

        if myguess=="stone":
            if guess[p]=="scissor":
                print("you win")
            elif guess[p]=="paper":
                print("you lose")
            else:
                print("draw")
        if myguess == "paper":
            if guess[p] == "stone":
                print("you win")
            elif guess[p] == "scissor":
                print("you lose")
            else:
                print("draw")
        if myguess == "scissor":
            if guess[p] == "paper":
                print("you win")
            elif guess[p] == "stone":
                print("you lose")
            else:
                print("draw")
    else:
        print("enter correct options ")
    i+=1
