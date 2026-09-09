'''
name ='sony'
age =45
print('welcome',name,'your age is',age)
2.F-string (doc-string)
-----------------
eg
-- 
name ='sony'
age =45
print(f'welcome {name} your age is {age}')

%s =-> all
name ='sony'
print('name :%s' % name)

%d =--> digit
eg
--
price = 89
print('name :%d' %price)

%f -->float
eg
--
price = 89
print('name : %f' % price)

name ='sony'
price =89.67
print('name :%f' % price)
(dot).format ()
age =89
print('name :{} \nage :{} '.format(name,age))

if condition
----
--> the if condition is used to check it is true or false 
age = 18
if age >=18 :
   print(f" your age is {age} and eligible to vote")

if-else
------

age= int(input("enter your age : "))
if age >= 18:
    print("your age is {age} and eligible to vote")
else :
    print(f"your age is {age}, you have to wait {18-age} years")

  
num =int(input("enter a number :"))
if num % 2 ==0:
   print(f'{num} is a even number')
else :
    print(f"{num} is a odd number")
    

vol_ = input('enter single letter:')
if vol_ in 'AEIOUaeiou':
   print(f'{vol_} is vol')
else :
   print(f'{vol_} is con')

so ='pythin'
do =so[::-1]
print(do)
if so [::-1] == so:
    print(f'{so} is a pali')
else:
    print(f'{so} is not a pali')


 leap year
 ------

year_ =int(input("enter a year: "))
if year_ % 4==0 and year_ %100 !=0 or year_ % 400== 0:
      print(f'{year_} is a leap')
else :
     print(f'{year_} not a leap')

elif
--------

marks_ =78
if marks_> 35:
      print('pass')
else:
      print('fail')

2.
marks_ = int(input("enter your marks:80"))
if marks_>=90:
      print('A+')
 
 elif marks_>= 80:
      print('A')
elif marks_>= 70:
      print('B+')
elif marks_>= 60:
      print('B')
elif marks_>= 50:
      print('C+')
elif marks_>= 40:
      print('C')
else:
      print('fail')
      

3.
num =89
num_2 =102
num_3 =5
if num> num_2 and num> num_3:
    print(f'{num} is greater value')
elif num_2> num and num_2 > num_3:
    print(f'{num_2} is greater value')
else:
    print(f'{num_3} is greater value')

control statements
------
1. break
2. continue

 break
 ----
 num =[34,67,90,107,56]
 for i in num:
  print(i)
  if i == 90:
  else:
  print('end')


 continue
 ------
num =[34,67,90,107,56]
 for i in num:
 if i == 90:
   continue
     print(i)
 else:
    print('end')

    
nested if
-------

detail_ ={'ATMPIN': '9870'}

atm_ = input('enter tour 4 digit atm pin: ')
if len(atm_) ==4 : 
    if atm_ == detail_ ['ATMPIN']:
       op_ = int(input("enter\nl. withdraw \n2. deposite \n3.pinchange"))
     ifop_ ==1 :
          money_w = int(input('enter money to withdraw: '))
     elif op_ ==2 :
          money_D = int(input('enter money to deposite: '))
     
   else:
     print('incorrect pin entered')
 else:
     print('pls enter only 4 digit pin')
    

 loops
 -------
 1. forloop 
 ------
 for loop is used to itterate over sequence such as str, list, tuple
 -- else in for loop it will execute when whole ittereates are completed..
 -- incase if condition becomes true, then else will never execute..

 num ='python is a language'
for i in num:
    print(i)
range()
----
-- range() function is used to generate number upto a limit...
syntax -- range(start, end, step)
eg
--
for j in range(1,10,3):
    print (j)


 2. while loop
 -----------

num = 1
while num<10:
 print(num)
 num += 1
 
assert keyword
----
-- the keyboard is used to check the cndition
eg
--
1.
age = 35
assert age>= 18, 'not eligible'
print('eligible')
 
2.
marks_ = 75
assert marks_ >= 35, 'fail'
print('pass')


    
