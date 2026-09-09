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




     




    






    
