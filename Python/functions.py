'''funtions
---------
--> function is block that can  be executes when we call it..
--> to avoid the repeated lines of code..
def function_name(parameters):
-------
----
-----
function_name(arguements)


types of functions
--------
1. built-in
---------
eg
--
print()
len()
max()
min()
2. userdefine
----------
--> user-define are  the function that are develop by the user
num= 56
num_2 =89
def total_(num, num_2):
    
    print(num+num_2)
          
total_(num,num_2)
total_(1,2)
    
    
required arguements
---------------
--> we have to pass same number arguements that match the parameters
-->

num= 56
num_2 =89
def total_(num, num_2):
    
    print(num)
          
total_(num,num_2)
total_(1,2)

positional arguements
---------
--> it does not matter how we are passing the variable, if we assign the value to that variable in the calling.....

def name_(name_,name):
    print(name)
    print(name_)
name_(name ='vasavi', name_ ='bantupalli')

a = 0
b = 9
c = 8
d = 7
m = 6
def pos_(m,d,a,c,b):

    print(m)

pos_(a=0,b=8,c=4,d=1,m=7)


29/07

eg_1
-------
def any_(age,name,education):
    print(age)

any_('vasavi','23', 'degree')

eg_2
-------
def any_(name,age,edu):
    print(age)
    print(name)
any_(name='vasavi',age='23',edu='degree')

variable-length positional arguements
-------------
*args
-------
--> we can pass tuple of arguements and store in a single parameter by just adding *before theparameter..
--> and we can access the arguements using indexing

nums = (10,34,5,89)
eg1
---
def all_va(*nums):
    print(nums[3])
all_va(10,34,5,89)
eg_2
-----

def all_va(*sums):
    print(nums[1] +nums[3])
    all_va(10,34,5,89)

variable length key word arguements
--------
*kargs
------
--> by pass keyword arguements in the arguements, will get it as a dictionaryjust adding ** before the parameter..
--> and can access by using dictionary methods..
eg
----
def dct(**all_in):
    for key, val in all_in.items():
        print(key,':',val)
dct(name = 'vasavi',age= '23',role= 'student')
eg_2
----
def dct_nums(*args,**kargs):
    print(args)
    print(kargs)
dct_nums(12,56,7,name='vasavi',age=78,edu='degree')


eg-1
-----
def nums():
    num = 90
    print(num)
nums()

eg-2
----

num_2 = 89
def nums(num_2):
    num = 90
    print(num)
    print(num_2)
nums(num_2)
print(num_2)


num_2 = 20
def nums(num_2):
    num_1 = 38
    num = 52
    print(num)
    print(num_1)
    print(num_2)
nums(num_2)
print(num_2)
    

num_2 = 20
def nums(num_2):
    num =90
    print(num)
    print(num_2)
nums(num_2)
print(num_2)
limit = int(input('enter a limit: '))
a,b =2,34
print(a,b,'end: ')

eg
----
limit_ = int(input('enter the limit:10,34,60 '))
num = 0
num_2 = 1
def fibonacci(limit_,num,num_2):
    print(num,num_2, end =' ')
    for j in range(1,limit_+1):
        num_3 = num+num_2
        num = num_2
        num_2 = n-um_3
        print(num_3, end=' ')
fibonacci(limit_,num,num_2)


passing by values
------------
def any_(num,num_2):
    print(num)
    print(num_2)
any_(num = 8, num_2 = 9)

anonymous function
--------
--> anonymous function is a function that don't any name
--> this also called as lamda function
--> lamda function will take n number of arguements but only one expression

syntax --> lamda arguements :expression
1.
so = lambda a,b,c : a+b+c
print(so(2,45,6))


eg
------
def num(n):
    if n == 1:
        return 1
    return n* num(n-1)
print(num (5))

map()
--> the map function will be applied on the given function of each and every element of an iterable
eg
---
nums = [1,2,3,4,5]
so = list(map(lambda x: x*x,nums))
print(so)

filter()
--> filter() function will only consider if the condition is true, then it will keep that values
eg
------
nums =[1,2,3,4,5]
so = list(filter(lambda x: x%2==0,nums))
print(so)

'''
from functools import reduce

nums = [1,2,3,4,5]

so = reduce(lambda x,y :x+y,nums)
print(so)





            


































    
    
