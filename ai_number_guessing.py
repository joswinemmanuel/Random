import time
def ai_guess_algo(a,b,c):
    time.sleep(1)
    print("This is how AI finds the number")
    print()
    n=1
    while True:
        time.sleep(2)
        print('Test',n)
        ans=(a+b)//2
        if ans==c:
            print(ans,', Found it in',n,'steps')
            break
        else:
            print(ans,' is not the number')
            if ans>c:
                b=ans
            else:
                a=ans
        n+=1
        print()
        


print("This is a program to demonstrate how a computer find a RANDOM NUMBER")
print("between a STARTING NUMBER range and ENDING NUMBER range")
a=int(input("Enter starting number:"))
b=int(input("Enter ending nmber:"))
c=int(input("Choose the random number the computer needs to find:"))
print()
ai_guess_algo(a,b,c)
