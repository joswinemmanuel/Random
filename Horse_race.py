import random
import time
# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',
#                              user='root',
#                              password='joswin',
#                              auth_plugin='mysql_native_password')
name=input('Your name:')
# mycur=mydb.cursor()
# mycur.execute('create database horse_game')
# mycur.execute('use horse_game')
# mycur.execute(f'create table score_sheet(Game_number char(10),{name} char(5),Computer char(5),Betting_in_dollar int);')
rounds=int(input('Number of game rounds you want to bet??:'))
money=0
for i in range(1,rounds+1):
    print()
    print(f'This is HORSE RACE BETTING Number {i}')
    bet=int(input(f'Betting for your {i}th game is($):'))
    print()
    print('Choose any horse from A to Z')
    p_cho=input('Your horse: ').upper()
    x=[chr(i) for i in range(65,91)]
    x.remove(p_cho)
    c_cho=random.choice(x)
    print("Computer's horse:",c_cho)
    print()
    p_trl=input('Choose your one character horse trail(-,=,+,etc): ')
    c_trl='_'
    print("Computer's horse trail:",c_trl)
    print()
    p_score=0
    c_score=0
    ps='YOU:|'
    cs='COM:|'
    print('Race track:')
    print('    |','_'*41,'|')
    print('PROGRESS AFTER EACH SECOND IS SHOWN LIVE')
    input('Click to start')
    while True:
        time.sleep(1)
        if p_score>40:
            print('    |','_'*41,'|')
            print()
            print(f"{name}'s horse was first and you won the game. Good Predction".upper())
            won=name
            money+=bet
            break
        elif c_score>40:
            print('    |','_'*41,'|')
            print()
            print("Computer's horse was first and won the game. Better luck next time".upper())
            won='Computer'
            money-=bet
            break        
        a,b=random.choice([1,2,3]),random.choice([1,2,3])
        ps+=p_trl*a+p_cho
        cs+=c_trl*b+c_cho
        print(cs)
        print(ps)
        ps=ps[:-1]
        cs=cs[:-1]
        p_score+=a
        c_score+=b
    # if won==name:
    #     mycur.execute(f"insert into score_sheet values('game {i}','win','lose',{bet})")
    #     mydb.commit()
    # else:
    #     mycur.execute(f"insert into score_sheet values('game {i}','lose','win',{bet})")
    #     mydb.commit()
print()

# input('CLICK TO SEE YOUR FINAL RESULT')
# print()
# print('FINAL RESULT IS')
# mycur.execute('select * from score_sheet')
# string=f"| Game number | {name} | Computer | Betting_in_dollar |"
# print('-'*len(string))
# print(string)
# print('-'*len(string))
# row=mycur.fetchall()
# for i in row:
#     print('|',i[0],' '*(10-len(i[0])),
#           '|',i[1],' '*(len(name)-1-len(i[1])),
#           '|',(i[2]),' '*(7-len(i[2])),
#           '|',str(i[3]),' '*(16-len(str(i[3]))),'|')
# print('-'*len(string))
# print()
if money>0:
    print(f'You EARNED a total of ${money} after {rounds} rounds.....WELL PLAYED')
elif money<0:
    print(f'You LOST a toltal of ${abs(money)} after {rounds} rounds.....BETTER LUCK NEXT TIME')
else:
    print(f'You earned no money after {rounds} rounds....Your profit is equal to loss')

    
    

    
