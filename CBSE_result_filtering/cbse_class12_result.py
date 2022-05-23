def all_stud_mark():
    f=open('75612.TXT','r')
    x=f.readlines()
    co=1
    for i in range(0,len(x),2):
        n=x[i].split()[2]+' '+x[i].split()[3]
        print(co,n,(' '*(20-len(n))),':',end='')
        co+=1
        for j in range(0,len(x[i+1].split()),2):
            print(x[i+1].split()[j][1:],end=' ')
        print()
            

def best_mark():        
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='plus2marks_all'
                                 ,auth_plugin='mysql_native_password')
    mycur=mydb.cursor()
    mycur.execute('select name,m1+m2+m3+m4+m5 as total,m1,m2,m3,m4,m5,m1+m2+m3+m4+m5 from bio_math union select name,m1+m2+m3+m4+m5 as total,m1,m2,m3,m4,m5,m1+m2+m3+m4+m5 from cs order by total desc')
    c=1
    for i in mycur.fetchall():
        print(str(c)+')',i[0],' '*(20-len(i[0])),':',i[1],'       ',[i[2],i[3],i[4],i[5],i[6]],'    ',str((i[7]/500)*100)[0:5]+'%')
        c+=1

def any_sub_write():
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='plus2marks_all'
                                 ,auth_plugin='mysql_native_password')
    mycur=mydb.cursor()
    f=open('75612.TXT','r')
    x=f.readlines()
    for i in range(0,len(x),2):
        xx=x[i].split()
        if [xx[-9],xx[-8],xx[-7],xx[-6],xx[-5]] in (['301','030','054','055','065'],['301','030','041','054','055']):
            n=x[i].split()[2]+' '+x[i].split()[3]
            m=[]
            for j in range(0,len(x[i+1].split()),2):
                m.append(int(x[i+1].split()[j][1:]))
            mycur.execute(f'insert into comm values("{n}",{m[0]},{m[1]},{m[2]},{m[3]},{m[4]});')
            mydb.commit()
    
            
            
best_mark()

