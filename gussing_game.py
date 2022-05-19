""" This is a number gussing game, to find the randomly generated number """

import random
h_score=100
def play_game():
    global h_score
    print("Welcome to the game")
    print("GUESS THE NUMBER BETWEEN 1 AND 100")
    num=random.randint(1,100)
    lst=[]
    while True:
        guess=int(input("GUESS THE NUMBER:"))
        lst.append(guess)
        if num==guess:
            print("You got the number, it was",num)
            break
        elif guess>num:
            print(guess,"is higher than the number")
        else:
            print(guess,"is lower than the number")
        print()
    print("You found the number in",len(lst),"guesses")
    print("Your gusses were:")
    for i in lst:
        print(i)
    if len(lst)<h_score:
        h_score=len(lst)
    print("The high score is",h_score)
    print()

while True:
    print("0)To to stop the game")
    print("1)To start the game")
    ch=int(input("Your choise:"))
    print()
    if ch==0:
        print("Thanks for playing!!!")
        break    
    elif ch==1:
        play_game()
    



















    






























    






















         
