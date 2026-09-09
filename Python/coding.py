'''
7*1 =7
7*2 =14

tab = int(input('enter a num: '))
for j in range(1,11):
print(f'{tab_} x{j}
={tab_*j}')

153 =1**3 +5**3 +3**3

num int(input('enter a number: '))
length_ =len(str(num))
am_ = 0
for j in str(num):
    am_ = int(j) ** length_ +am_
    if am_ == num:
        print(f'{num} is amstrong')
        else:
            print(f'{num} is not')

 
limit_ = int(input('enter limit: ')
num = 0
num_2 =1
print(num,num_2,end =' ')
for j in range(1,limit_ +1):
    all_ad = num + num_2
    num = num_2
    num_2 = all_ad
    print(all_ad,end =' ')

    
calculator

num_1 = int(input('enter a num: '))
num_2 =int(input('enter a num: '))
opt_ = int(input('enter \n1.div \n2.mult: '))
if opt_ == 1:
    print(num_1 / num_2)
elif opt_ == 2:
        print(num_1 * num_2)

ICIC_teja = {'name' : 'teja',
             'ADr':"2345678",
             'pan': 'hfg676afgh9',
             'ATM PIN' : '7700',
             'Balance':45678}
remain_A = 3
while remain_A>0:
    pin_ = input(" enter your 4 digit pin: ")
    if len(pin_) == 4:
        if pin_ in ICIC_teja['ATM PIN']:
            pass
        else:
            remain_A -= 1
            if remain_A> 0:
                print(f' Incorrect pin nad you have only {remain_A}')
            else:
                print('card is block')
                break
    else:
        print('pls enter only 4 digit atm pin')




        


ICIC_teja = {'name' : 'teja',
             'ADr':"2345678",
             'pan': 'hfg676afgh9',
             'ATM PIN' : '7700',
             'Balance':45678}
remain_A = 3
while remain_A>0:
    pin_ = input(" enter your 4 digit pin: ")
    if len(pin_) == 4:
        if pin_ in ICIC_teja['ATM PIN']:
            pass
        else:
            remain_A -= 1
            if remain_A> 0:
                print(f' Incorrect pin nad you have only {remain_A}')
            else:
                print('card is block')
                break
    else:
        print('pls enter only 4 digit atm pin')
'''
ICIC_teja = {'name' : 'teja',
             'ADr':"2345678",
             'pan': 'hfg676afgh9',
             'ATM PIN' : '7700',
             'Balance':'45678',
            'Trasaction History':[] }
remain_A = 3
withdraw=0
deposite=0
while remain_A>0:
    pin_ = input(" enter your 4 digit pin: ")
    if len(pin_) == 4:
        if pin_ in ICIC_teja['ATM PIN']:
            opt_ = int(input('enter \n1.withdraw \n2.Deposite \n3.Blance /n4.Trasaction History /n5.Pin Change: /n '))
            if opt_ ==1:
               Withdraw_m = int(input('enter amount you want to Withdraw: '))
               if Withdraw_m <= ICIC_teja['Balance'] and Withdraw_m % 100 == 0:
                   ICIC_teja['Balance'] -= withdraw_m
                   print(f'you have withdraw [Withdraw_m] and the total Balance ICIC_teja')
                   user_ =int(input('enter /n1.Homepage /n2.Exit:/n'))
                   if user_ ==1:
                       print('Thank you for visiting')
                   break
               else:
                    print('can not provide change or no balance')
                    break
            elif opt_ ==2:
                deposite_m = int(input('enter the money you want to deposite: '))
                if deposite_m % 100 == 0:
                    ICIC_teja['Balance'] += deposite_m
                    print(f'you have deposited {deposite_m} and the total Balance')
                    user_ = int(input('enter \n1.Home page \n2. Exit: '))
                    if user_ == 1:
                        print('home page')
                    else:
                        print('Thanks for visiting')
                        break
                    
                        
                else:
                    print('change can not be deposite')
    
            elif opt_ ==3:
                print(f'Balance is{ICIC_teja['Balance']}')
                user_=int(input('Enter /n1.Homepage /n2.Exit: /n'))
                if user_==1:
                    print('Homepage')
                else:
                    print('Thanku for visiting')
                    break
            elif opt_==4:
                        print(f'Transaction History withdraw amount:{withdraw} deposite amount:{deposite}')
                        if user_==1:
                            print('home page')
                        else:
                            print('Thanku for visiting')
                            break
                
            elif opt_== 5:
                      pass
                                
            
                 else:
                    remain_A -= 1
                    if remain_A> 0:
                          print(f' Incorrect pin nad you have only {remain_A}')
                 else:
                     print('card is block')
                     break
                 else:
                     print('pls enter only 4 digit atm pin')

        
