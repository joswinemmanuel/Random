"""This is a addition operant guessing game"""

import random
import time
# import mysql.connector

f=open('score.txt','r')
h_score=int(f.readline())
nm=f.readline()
f.close()

def add():
    a=random.randint(1,100)
    b=random.randint(1,100)
    print(a,"+",b,"=","___",end='\n\n')
    return a+b
def sub():
    a=random.randint(1,100)
    b=random.randint(1,100)
    print(a,"-",b,"=","___",end='\n\n')
    return a-b
def mul():
    a=random.randint(1,10)
    b=random.randint(3,9)
    print(a,"x",b,"=","___",end='\n\n')
    return a*b
def div():
    a=random.randint(1,10)
    b=random.randint(1,10)
    a,b=max(a,b),min(a,b)
    a=a*b
    print(a,"/",b,"=","___",end='\n\n')
    return a/b

print("WELCOME TO THE GAME",end="\n\n")
time.sleep(2)
print("AN EXPRESSION WILL BE GIVEN, FIND THE RESULT ASAP",end="\n\n")
time.sleep(4)
print("INSTRUCTIONS")
print("5 points FOR answering within 5seconds")
print("4 points FOR answering within 10seconds")
print("3 points FOR answering within 15seconds")
print("2 points FOR answering in 1 chance")
print("1 point FOR just finding the answer")
print()
print("THE CURRENT HIGH SCORE IS:",h_score,"by",nm)
print()
time.sleep(5)
print("PRESS 0 TO QUIT and print final score")
input("press enter to begin")
print()

r=1
points=0
ini=True
while ini:
    print("ROUND:",r)
    print("YOUR POINTS:",points)
    start=time.time()
    chance=0
    c=random.choice([1,2,3,4])
    if c==1: c=add()
    elif c==2: c=sub()
    elif c==3: c=mul()
    elif c==4: c=div()
    while True:
        guess=int(input("The RESULT is:"))
        chance+=1
        if guess==c:
            stop=time.time()
            t=stop-start
            print()
            print(t,"seconds AND",chance,"chance were TAKEN")
            if t<5:
                print("LESS THAN 5seconds -->",5,"points")
                points+=5
            elif t<10:
                print("LESS THAN 10seconds -->",4,"points")
                points+=4
            elif t<15:
                print("LESS THAN 15seconds -->",3,"points")
                points+=3
            elif chance==1:
                print("IN THE FIRST TRY -->",2,"points")
                points+=2
            else:
                print("TRY FASTER NEXT TIME -->",1,"points")
                points+=1
            print()
            r+=1
            time.sleep(4)
            break
        elif guess==0:
            print()
            print("THANKS FOR PLAYING")
            print("YOU SURVIVED",r-1,"rounds")
            print("YOUR FINAL SCORE IS: ",points)
            ini=False
            break
        else:
            print("Nope, try again")
            continue
time.sleep(4)
print()
name=input('Enter your name: ')
print()
time.sleep(3)

if points<h_score:
    print("TRY TO BEAT THE HIGH SCORE NEXT TIME")
elif points==h_score:
    print("GREAT JOB, YOU TIED THE HIGH SCORE...WooooW")
else:
    print("YOU BROKE THE HIGH SCORE!!!!!")
    f=open('score.txt','w')
    f.write(str(points))
    f.write('\n')
    f.write(name)
    f.close()
time.sleep(2)
print()

# print('HALL OF FAME'.center(33))
# mydb=mysql.connector.connect(host='localhost',user='root'
#                              ,password='joswin',database='addition_king'
#                              ,auth_plugin='mysql_native_password')
# mycur=mydb.cursor()
# mycur.execute(f"insert into hiscore values('{name}',{points});")
# mydb.commit()
# mycur.execute('select player,max(score) from hiscore group by player order by score desc;')
# rec=mycur.fetchall()
# base='+'+'-'*31+'+'
# print(base)
# print('|'+'PLAYER'.center(20)+'|'+'SCORE'+' '*(10-len('score'))+'|')
# print(base)
# for i in rec:
#     print('|'+i[0].center(20)+
#           '|'+str(i[1])+' '*(10-len(str(i[1])))+'|')
# print(base)
# mycur.close()
# mydb.close()





    






























    






















         
