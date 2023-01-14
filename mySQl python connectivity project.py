import mysql.connector as ms

mydb= ms.connect(host='localhost',user='root',passwd='Xvds9@zcsuX#123',database='project')
cursor= mydb.cursor()


print(" __       __    __       __         _____    ____________    _____________ ")
print("|  |     |  |  |  \     /  |       /   __|  |   _______  |  |             |")
print("|  |     |  |  |   \   /   |      /   /     |  |       | |  |_____   _____|")
print("|  |     |  |  |    \-/    |     /    \     |  |_______| |        | |")
print("|  |     |  |  |  \     /  |    /  /\  \    |   __   ____|        | |")
print("|  |_____|  |  |  |\   /|  |   /  /  \  \   |  |  \  \           _| |_")
print("\___________/  |__| \_/ |__|  /__/    \__\  |__|   \__\         |_____|")


while True:
    print("\n|----------Welcome to Grossery Tracker----------|")
    print("|\t\t\t\t\t\t|")    
    print("|\t\tHow Can I Help You !\t\t|") 
    print("|\t\t\t\t\t\t|")
    

    print('|\t1.account details\t\t\t|') #1

    print("|\t2.balance\t\t\t\t|") #2

    print("|\t3.total expenditure\t\t\t|") #3

    print("|\t4.total loan\t\t\t\t|") #4

    print("|\t5.coupuns details\t\t\t|") #5

    print('|\t6.offers\t\t\t\t|') #6

    print("|\t7.sales detail\t\t\t\t|") #7
    
    print("|\t8.show list\t\t\t\t|") #8 '''5 wala nai hua '''

    print('|\t9.rate\t\t\t\t\t|') #9 '''logic '''
    
    print("|\t10.show purchased item\t\t\t|") #10

    print("|\t11.calories tracker\t\t\t|") #11 '''compare and suggest'''

    print("|\t12.due dates\t\t\t\t|") #12

    print("|\t13.edit loans\t\t\t\t|") #13
    
    print("|\t14.moving cart\t\t\t\t|") #14 '''logic'''

    print('|\t15.mannage account\t\t\t|') #15
    
    
    
    

    
    print("|\t\t\t\t\t\t|")
    print("|-----------------------------------------------|")
    ch=int(input("\t   PLEASE ENTER YOUR CHOICE: "))
    print("|-----------------------------------------------|\n")



    if ch==1:
        cursor.execute('select * from account')
        for x in cursor:
            print(x)



    if ch==2:
        cursor.execute(' select min(balance) from account')
        for x in cursor:
            print('\nyour balance is ',list(x))



    if ch==3:
        cursor.execute(' select expenditure from account order by date desc limit 0,1')
        for x in cursor:
            print('your expenditure is:',list(x))



    if ch==4:
        cursor.execute('select loan from account order by date desc limit 0,1')
        for x in cursor:
            print('\nyour loan is ',list(x))



    if ch==5:
        print('\t    |----------------------|')
        print("\t    |SELECT YOUR CATEGORIES|")
        print('\t    |----------------------|')
        print('\t    |1.total coupuns\t   |')
        print('\t    |2.coupun details\t   |')
        print('\t    |3.expiring coupuns\t   |')
        print('\t    |----------------------|')
        choice=int(input("\t   |PLEASE ENTER YOUR CHOICE: "))

        
        if choice==1:
            cursor.execute("select count(coupuns) from account where coupuns='yes'")
            for x in cursor:
                print('\ntotal coupuns',x)
        if choice==2:
            cursor.execute('select * from coupuns')
            for x in cursor:
                print('\ncoupuns detail',x)
        if choice==3:
            cursor.execute('select exp from coupuns order by exp asc')
            for x in cursor:
                print('\nexpiring copuns list',x)


    if ch==6:
        cursor.execute('select * from offers')
        for x in cursor:
            print('\n',x)

    if ch==7:
        cursor.execute('select * from sales;')
        for x in cursor:
            print(x)


            
    
    if ch==8:
        print('\t    |----------------------|')
        print("\t    |SELECT YOUR CATEGORIES|")
        print('\t    |----------------------|')
        print('\t    |1.cerials\t\t   |')
        print('\t    |2.fruits\t\t   |')
        print('\t    |3.packed foods\t   |')
        print('\t    |4.vegitables\t   |')
        print('\t    |5.all list\t\t   |')
        print('\t    |----------------------|')
        choice=int(input("\t   |PLEASE ENTER YOUR CHOICE: "))
        if choice==1:
            cursor.execute('select items from cerials')
            for x in cursor:
                print(x)
        if choice==2:
            cursor.execute('select items from fruits')
            for x in cursor:
                print(x)
        if choice==3:
            cursor.execute('select items from packed_food')
            for x in cursor:
                print(x)
        if choice==4:
            cursor.execute('select items from vegitables')
            for x in cursor:
                print(x)
        if choice==5:
            cursor.execute('null')
            for x in cursor:
                print(x)

    if ch==9:
        condition =True
        a=True
        while condition == a:
            dict1={'potato':20,'tomato':15,'onion':40,'garlic':10,'mushroom':250,
               'apple':100,'banana':50,'grapes':60,'casew':160,'nuts':110,
               'rice':1400,'wheat':700,'flour':95,'cornflour':105,'besan':85,
               'potato chips':20,'mixture':95,'salted nuts':105,'fries':35,'candies':100}
            choice=input("PLEASE ENTER FOOD ITEMS TO KNOW RATE: ")
            if choice in dict1.keys():
                print(dict1[choice])
            if choice not in dict1.keys():
                a=False
                print('choose from this list\n')
                print(list(dict1.keys()))
        else:
            print("\n|-----------------------------------------------|")
            print('|\t     DO YOU WANT TO CONTINUE\t\t|')
            print("|-----------------------------------------------|")
            ch=input('|\t\tPress yes/no to respond: ')
            print("|-----------------------------------------------|\n")
            if ch in ('yes','y','YES','Y'):
                print('\n')
            
            if ch in ('no','n','NO','N'):
                break
        

            
        

    if ch==10:
        cursor.execute('select * from purchased')
        for x in cursor:
            print('\n',x)


    if ch==11:
        weight=float(input('please enter your weight in kg: '))
        height=float(input('please enter your height m: '))
        age=float(input('please enter your age in year: '))
        gender=input('please enter your gender: ')
        
        if gender in ('girl','lady','woman','g','l','w','female'):
            cal=(65+(4.3 * (weight*0.45))+(4.7*(height*0.025))-(4.8*age))
            print('your required calory is',cal)
            cursor.execute('select sum(calories) from purchased')
            for x in cursor:
                print(x)
                total=list(x)
            cal=list(cal)
            if cal>total:
                print('your required calories is',cal,'you only took',total/10,'please add more')
            
            
        if gender in ('boy','man','b','m','male'):
            cal=(66+(6.3 * (weight*0.45))+(12.9*(height*0.025))-(6.2*age))
            print('your required calory is',cal)
            cursor.execute('select sum(calories) from purchased')
            for x in cursor:
                total=list(x)
            cal=list(cal)
            if cal>total:
                print('your required calories is',cal,'you only took',total/10,'please add more')



    if ch==12:
        cursor.execute('select date,loan from account order by date desc limit 0,1;')
        for x in cursor:
            print('\nyour net payable',list(x))



    if ch==13:
        cursor.execute(' select * from loan group by due_date having min(due_date)')
        for x in cursor:
            print('\nyour shop list is ',x)



    if ch==14:
        while True:
            print('Do you Want To Reset/Insert/remove')
            print('1.reset')
            print('2.insert')
            print('3.remove')
            print('4.to leave')
            choice=int(input("PLEASE ENTER YOUR CHOICE: "))
            if choice==1:
                cursor.execute('delete from purchased_list')
                mydb.commit()
                print('deleted items:',cursor.rowcount,' your list got reset')

            if choice==2:
                a=input('PLEASE ENTER ITEM: ')
                cursor.execute('insert into purchased_list values(',a,')')

                if choice==1:
                    cursor.execute('delete from purchased_list where items=')
                    mydb.commit()
                    print('deleted items:',cursor.rowcount,' your list got reset')

            if choice==4:
                break

            else:
                print('PLEASE ENTER CORRECT CHOICE')




    if ch==15:
        cursor.execute(' select * from loan')
        for x in cursor:
            print('\nyour shoping data is ',x)


            
    else:
        print("\n|-----------------------------------------------|")
        print('|\t     DO YOU WANT TO CONTINUE\t\t|')
        print("|-----------------------------------------------|")
        ch=input('|\t\tPress yes/no to respond: ')
        print("|-----------------------------------------------|\n")
        if ch in ('yes','y','YES','Y'):
            print('\n')
            
        if ch in ('no','n','NO','N'):
            break
        
##        else:
##            print('please enter correct choice')
##        
        
        
cursor.close()
mydb.close()




