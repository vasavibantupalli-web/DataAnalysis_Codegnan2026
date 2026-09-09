'''
oops
-------
--> object oriented programming system
--> oops is used to maintain the code structure in object ans classes....

1.class
---------
--> class is an blueprint or template to an object
syntax
------
class(keyword) name:
#attribute
#methods
2.object
---------
--> object is instance of the class
syntax
-------
class(keyword) name:
#attribute
#methods

any_ = class_name
3.attribute
-----------
--> attribute is the data presentnin the class or pass to the class
eg
-------
take car
-----------
color
brand
seat
class vasavi:
    name = 'vasavi'
    age = 23
    back_g = 'b.tech'
    an = vasavi()
    print(an.name)

2.
    class car:
    def __init__(self):
        self.color = 'red'
        self.seat =6
        self.brand = 'BMW'

c1 = car()
print(c1.color)
print(c1.brand)        
              

4.methods
--------
--> method is a function that is created inside the class
syntax
------
class(keyword) name:
    #attribute
    def fun_name(self):
     #code

obj = class_name()
print(obj.fun_name())
class stu:
    name = 'vasavi'
    age = 23

s1 = stu()
print(s1.name)
print(s1.age)
    

class codegnan:
    city = 'hyd'
    tech = 'python'
    data = 'MY SQL'

code_ = codegnan()
print(code_.city)


class details:
    def __init__(self):
        self.name = 'vasavi'
        self.age = 23
        self.back_g = 'degree'
        self.role = 'student'

person_ = details()
print(person_.name)
print(person_.age)
print(person_.back_g)
print(person_.role)


class bank:
    def __init__(self):
        self.name = 'vasavi'
        self.aadhar = '234565473423'
        self.number = '99453222456'
        self.pan = 'hyrwr3y9hf'
per_d=bank()
print(per_d.name)
print(per_d.number)


class student:
    def __init__(self):
        self.name = 'vasavi'
        self.age = 23
        self.source = 'pfs'

    def st_name(self): 
       print(self.name)
       print(self.age)
       print(self.source)

    def all_data(self):
       print(self.name)
       print(self.age)

stu_ = student()
stu_.st_name()
stu_.all_data()



class car:
    def __init__(self):
        self.color = 'blue'
        self.seat = 6
        self.brand = 'BMW'

    def brake_(self):
        print(f'{self.brand} brake will apply at speed 250km')

    def accelater_(self):
        print(f'{self.brand} will take 2 sec to reach 180 speed')

    def clutch(self):
        print(f'{self.brand} with {self.seat} no automatic')

BMW = car()
BMW.brake_()
BMW.accelater_()
BMW.clutch()



class students:
    def __init__(self,name,age,batch):
        self.name = name
        self.age = 23
        self.batch = 5

    def all_data(self):
        print(self.name)
        print(self.age)
        print(self.batch)

stu_1 = students('vasu',23,5)
stu_1.all_data()

stu_2 = students('vasavi',22,5)
stu_2.all_data()

class register:
    def __init(self,name,age,number,mail):
        self.name = 'vasavi'
        self.age = 23
        self.number = 9673256987
        self.mail = 'vasavibantupalli@gmail.com'

    def all_data(self):
        print(self.name)
        print(self.number)
        print(self.mail)

register_1 :register('vasavi','23','9673256987')
register_1.all_data()



constructor
-----------
--> __init__
--> the constructor is a special method that only run when the object is created
--> mostly we will take data inside this method..
eg
------
class cls_data:
    def __init__(self):
        self.name = 'vasavi'
        self.course = 'python'

cls_ = cls_data()
print(cls_.name)
print(cls_.course)

self
-------
--> the self keyword refers to current object
eg
-------
class stu:
    def __init__(self):
        self.name = 'vasavi'

    def any_(self):
        print(self.name)

s1 = stu()
s1.any_()

class stu_data:
    def __init__(self,name,batch,age):
        self.name = 'vasavi'
        self.batch = 5
        self.age = 23
    def student(self):
        print(f'{self.name} from batch{self.batch} and age{self.age})

data1 = stu_data('sony',125,34)
data1.student()

encapsulation
-----
--> wrapping data and methods together is called as encapsulation and using or controlling the data in methods
eg
-----
class stu_data:
    def __init__(self,name,batch,age):
        self.name = 'vasavi'
        self.batch = 5
        self.age = 23
    def student(self):
        print(f'{self.name} from batch{self.batch} and age{self.age}')

data1 = stu_data('sony',125,34)
data1.student()

2.
class stu_data:
    def __init__(self,name,batch,age,fee):
        self.name = 'vasavi'
        self.batch = 5
        self.age = 23
        self.fee = 45000
    def student(self):
        print(f'{self.name} from batch{self.batch} and age{self.age} and paid{self.fee}')

data1 = stu_data('sony',125,34,45000)
data1.student()

access specifiers
-------------
1. public(name)
------
--> this can be access normally and can call it like a nrml variable
eg
----
self.name = name
print(self.name)

2.proctected  (_name)
--------
--> just adding single(_) before a variable it becomes proctected variableg
----
self.age = age
print(self._age)


class stu_data:
    def __init__(self,name,batch,age,fee):
        self.name = 'vasavi'
        self.batch = 5
        self.age = 23
        self.fee = 45000

    def only_name(self):
        print(f"{self._name}")
                  
    def only_batch(self):
        print(f"{self._batch}")

    def only_age(self):
        print(f'{self._fee}')

    def only_fee(self):
        print(f'{self._fee}')

data1 = stu_data('sony',125,34,45000)
data1.only_name()
data1.only_age()
data1.only_fee()


3. private (name)
----------
--> adding (__) before a variable it becomes private variable
eg
-----
self.__balance = balance
print(self.__balance)
2.
class bank_ac:
    def __init__(self):
        self.name = 'vasavi'
        self.Adr = '123456789'
        self.pan = 'jbugh4678t'
        self.__balance = 45000

    def details(self):
        print(self.name)
        print(self.Adr)
        print(self.pan)
        
    def bank_bal(self):
        print(self.balance)

AC = bank_ac()
AC.details()

class employee:
    def __init__(self):
        self.name = 'vasavi'
        self.role = 'python Developer'
        self.__salary = 82000
        self._experiance = 4.5
        self._emptype = 'full-time'

    def details(self):
        print(self.name)
        print(self.role)

    def income_(self):
        print(self.__salary)

    def type_(self):
        print(self._emptype)

emp = employee()
emp.details()
emp.income_()
emp.type_()


class college:
    def __init__(self):
        self.name = 'vasavi'
        self.course = 'data analytics'
        self.batch = 5
        self.number = 9121261949
        self.fee = 50000

    def details(self):
        print(self.name)
        print(self.course)
        print(self.batch)
        print(self.number)

    def fee(self):
        print(self._fee)

college = college()
college.details()

inheritance
-------------
--> inheriting is the process of inherite one class into another class
--> will general inherite from aclass is called parent class and using that class is called child class

class company: 
    def salary(self): 
      print('company salary')

class employee(company): 
    def mon_sal(self): 
      print('employee salary')

per_sal = employee()
per_sal.mon_sal()
per_sal.salary()

types
--------
1.single inheritence
--------------
--> if one child class inherite from one parent class this is called single inheritance
eg
---
class father:
    def land(self):
        print('5 acer land')

class me(father):
    def flat(self):
        print('6 flat')

all_ = me()
all_.flat()
all_.land()

2.multiple inheritance
---------------------
--> if one child inherite from more than one parent class this is called multiple inheritance
eg
-----
class father:
    def home(self):
        print('home at village')

class mother:
    def gold(self):
        print('50kg gold')

class son(father,mother):
    def flat(self):
        print('sons flat')

all_to = son()
all_to.home()
all_to.gold()

3.multi-level inheritance
---------------------
--> one child class become parent class to the another class is called multi-level inheritance
eg
----
class grandfather:
    def land(self):
        print('grandfather land')

class father(grandfather):
    def flat(self):
        print('father flat')

class son(father):
    def car(self):
        print('sons car')

fam = son()
fam.land()
fam.flat()
fam.car()

4.hirarchical inheritance
----------------------
--> if two child classes inherite from one parent class is called as hierarichal inheritance
eg
----
class father:
    def land(self):
        print('50 acer land')

class son_1(father):
    def flat(self):
        print('first son flat')

class son_2(father):
    def car(self):
        print('second son car')

s1 = son_1()
s1.land()
s1.flat()

s2 = son_2()
s2.land()
s2.car()

5.hybrid inheritance
-------------------
--> inherite from more than two types into one class is called as hybrid inheritance 
eg
-----
class person:
    def name(self):
        print('vasavi is her name')

class student(person):
    def study(self):
        print('degree final year')


class py_teacher:
    def teach(self):
        print('python')

class java_teacher:
    def teach(self):
        print('java')

class learner(py_teacher,java_teacher):
    def learn(self):
        print('learner')

class all_get(student,learner):
    def get_it(self):
        print('this person getting all data')

an = all_get()
an.name()
an.study()
an.teach()
an.learn()
        

single inheritance
--------
class teacher:
    def subject(self):
        print('python')

class me(teacher):
    def learner(self):
        print('learn')

all_ = me()
all_.subject()
all_.learner()
multiple inheritance
-----------
class father:
    def vehicle(self):
        print('scooty')

class mother:
    def gold(self):
        print('5kg gold')

class daughter(father,mother):
    def shop(self):
        print('shop')

all_ =daughter()
all_.vehicle()
all_.gold()
all_.shop()

3. multi-level inheritance
----------------
class Animal:
    def eat(self):
        print("Animal eats food")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


class Puppy(Dog):
    def play(self):
        print("Puppy plays")


p = Puppy()

p.eat()
p.bark()
p.play()

4.hirarichal inheritance
-------------------
class Vehicle:
    def start(self):
        print("Vehicle starts")


class Car(Vehicle):
    def drive(self):
        print("Car is driving")


class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")


c = Car()
b = Bike()

c.start()
c.drive()

b.start()
b.ride()

5. hybrid inheritance
-------------

class Person:
    def show(self):
        print("I am a person")


class Student(Person):
    def study(self):
        print("I am a student")


class Teacher(Person):
    def teach(self):
        print("I am a teacher")


class Assistant(Student, Teacher):
    def help(self):
        print("I help everyone")


a = Assistant()

a.show()
a.study()
a.teach()
a.help()

super-method
---------
--> the super-method is used to get the constructor from the parent class and use in the child class
--> and also can get any method from a parent class...
eg-1
-----
class person:
    def __init__(self,name,age,role):
        self.name = name
        self.age = age
        self.role = role

class employee(person):
    def __init(self,name,age,salary,role):
        super().__init__(name,age,role)
        self.salary = salary
        print('Employee Constructor called')

obj = employee('teja',67,100,'python developer')
print(obj.name)
print(obj.age)
print(obj.salary)

eg-2
--------
class all_:
    def job_(self):
        print("I'm looking for job")

class looking(all_):
     def job_(self):
         print('we are looking for candidate')

     def an_(self):
        super().job_()
        print('no jobs')

any_ = looking()
any_.an_()



class person:
    def __init__(self,name,age,role):
        self.name = name
        self.age = age
        self.role = role

class employee(person):
    def __init(self,name,age,salary,role):
        super().__init__(name,age,role)
        self.salary = salary
        print('Employee Constructor called')

obj = employee('teja',67,100,'python developer')
print(obj.name)
print(obj.age)
print(obj.salary)


polymorphism
------------
--> polymorphism means a same name but different forms...
1.method overloading
--------------
--> this method overloading happens in class a methods is created this same name,but the recent method will be activated and the before one will not the considered
eg
-----
class data_:

    def add_(self,a,b,c=0):
        return a+b+c

    def add_(self,a,b,c):
        return a+b+c

    def add_(self,a,b,c,d):
        return a+b+c+d
obj = data_()
print(obj.add_(2,3,9,7))

2.method overriding
-----------------
--> this method overriding happens when parent class and child class have same method and the child take its own implementation
eg
-----
class pay:
    def payment(self):
        print('payment called')

class UPI(pay):
    def payment(self):
        print('UPI payment called')

class paytm(pay):
    def payment(self):
        print('paytm payment called')

obj = UPI()
obj.payment()

go=paytm()
go.payment()

3.operation overloading
-----------------
--> operator overloading which gives special meaning to the operator when it called by object
1.__add__
---------------
class cal:
    def __init__(self,any_):
        self.any_ = any_
        
    def __add__(self,do):
        print(self.any_+ do.any_)

how = cal(78)
who = cal(67)
how.__add__(who)

2.__sub__
=--------
eg
------
class cal:
    def __init__(self,any_):
        self.any_ = any_
        
    def __sub__(self,do):
        print(self.any_- do.any_)

how = cal(78)
who = cal(67)

print(how-who)

3.__mul__
--------

class cal:
    def __init__(self,any_):
        self.any_ = any_
        
    def __mul__(self,do):
        print(self.any_* do.any_)

how = cal(78)
who = cal(67)

print(how*who)

4.__truediv__

class cal:
    def __init__(self,any_):
        self.any_ = any_
        
    def __truediv__(self,do):
        print(self.any_/ do.any_)

how = cal(78)
who = cal(67)

print(how/who)

abstraction
---------------
--> abstraction means hiding the implemented data and showing only need data to user
--> ABC-abstract base class
--> the abstract method is used to hide that particular information of a base class 
eg-1
------
from abc import ABC,abstractmethod
class gov_bank(ABC): 
   @abstractmethod
   def interest(self):
       print('government interest is 3.5')

class SBI_bank(gov_bank):
    def interest(self):
        print('SBI bank interest is 7.8')

class ICIC_bank(gov_bank):
    def interest(self):
        print('ICIC bank interest is 8.9')

obj = SBI_bank()
obj.interest()

obje = ICIC_bank()
obje.interest()

eg-2
--------

from abc import ABC,abstractmethod

class cls_fee(ABC):
    def fee_str(self):
        print('college fee 45000')

class manage(cls_fee):
    def fee_str(self):
        print('college fee 100000')

class EM(cls_fee):
    def fee_str(self):
        print('college fee 15000')



--> 1.create a code on caluculator to addgiven numbers 2or 3or 4inputs
-->2.create a class with the name vehicle 
    
 eg
 -------
class Vehicle:
    def start(self):
        print("Vehicle starts")


class Car(Vehicle):
    def drive(self):
        print("Car is driving")


class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")


obj = Car()
obje = Bike()

obj.start()
obj.drive()

obje.start()
obje.ride()    
eg
-----
class caluculator:

    def add(self,a,b,c=0,d=0):
        print(a+b+c+d)


obj = caluculator()
obj.add(2,3)
obj.add(2,3,4)
obj.add(2,3,4,5)

Regular EXpression(RegEX)
--------
-->  this RegEX is used form a search pattern to find out the string contain sequence char or not
--> to use this RegEX ,we need to import re module

functions
-----------
--> Findall
---------
--> the searching pattern is found then,it will gives the o]p in the list[]
eg
------
import re
some = 'python is a programming language'
print(re.findall('[a]',some))

--> Search
-------
--> this is also used to form a searching pattern but it will give only the first matched  object
--> where it will gives with the index position,where the matched object is found by the pattern
eg
----------
import re
do = 'i have 1000 rupees with me'
print(re.search('e',do))

meta characters
-------------
--> meta characters are the symbols used in the search pattern
1.[]
-------------
--> this [] symbol is used find a group char that present in the string, we can also specify the range
syntax --> re.findall(,[range]',variable_name)
--> by using this symbol we can search cap(A-Z), small(a-z) and digit(0-9)
eg
---
import re
some = 'we are iun theg class8'
print(re.findall('[aguo]',some))
print(re.findall('[a-z]',some))
print(re.findall('[0-9]',some))

2. . char
----------
--> this symbol will refer only one means can match only a single char in the pattern....
syntax --> re.searcgh('c....',variable_name)
eg
-----
import re
some = 'Hello! World'
print(re.findall('H...o',some))
print(re.search('H....',some))

3. ^
----------
--> this symbol is used where the pattern where string starting match or not
syntax
--> re.findall('^',variable_name)
eg
-----
import re
some = 'Hello! World'
print(re.search('^Hello',some))
print(re.findall('^Hello',some))

4. $
-------------
--> this symbol will find out if the string is ending with pattern or not
syntax
--> re.findall('sequence$',variable_name )
eg
-----
import re
any_ = 'Iamplaying for a trip'
print(re.findall('trip$',any_))
print(re.search('for a trip$',any_))

5.{}
--------
--> the symbol is used to find a group char that present in string
syntax
--> re.findall(('E.{size},variable _name))
eg
-----
import re
all_ = 'Ihave 1000 rupees with me'
print(re.findall('I.{2}',all_))

6.?
--------
--> the symbol will find max upto 1 match in the string
syntax
--> re.findall('.?'variable_name)
eg
-----
import re
some = 'Hello! World hello'
print(re.findall('Hel.?o',some))


7.*
--------
--> this symbol max number of sequence from the string
syntax
--> re.findall('.*,variable_name)
eg
----
import re
some = 'The symbol is used to find a group char that present'
print(re.findall('T.*r',some))

8.+
eg
--------
import re
some = 'The symbol is used to find a group char that present'
print(re.findall('T.+s',some))

eg 
import re
user_name = input("please enter your name: ")
pattern = re.search('^[A-Z,a-z]{3,}$',user_name)
if pattern:
    print('correct name')
else:
    print('incorrect name')

import re
num = input("please enter a number: ")
fnd = re.findall('^[6-9][0-9]{9}$',num)
if fnd:
    print('indian')
else:
    print('not indian')

Data analysis
------------
--> data analysis is a process of collecting,cleaning,transforming,organizine and analyzing data to convert into useful information and also used for making decisions to get better outcome

-->library used
-----------
numpy
pandas
maplotlib
seaborn

Numpy
-------
--> this refers to numerical python,
--> it is python library used for caluculations and operations
--> this python library is more faster than the list to perform operations
--> and also supports multi-dimensional arrays
eg
-----
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr.ndim)
'''
import numpy as np
arr_2 = np.array([1,2,3,4,5])
print(arr_2.ndian)
arr_3 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(arr_3.ndim)




















