'''

modules
------
--> modules are the python code with which is saved in (.py) that contains functions variables classes

type
------
1. built-in
-------
--> the built-in modules that are already designed which comes with python when we are installing

eg
--
1. math
-------
--> math module used to work on mathematical functionality
floor
---
it will round-down to the near value
eg
---
import math
print(math.floor(3,78))

god
---
--> it will find the god value
eg
----
import math
print(math.god(24,36))

lcm
-----
--> it will find the lcm value
eg
-----
import math
print(math.lcm(*args:24,36))

square root value
--------
--> it will get square root value
eg
---
import math
print(math.sqrt(*args:24,36))


2. sys
3. os
4. random

2. user-defined
--------
--> the user-define modules are created by the programmer

alies name
-------
--> we can also import a module with different name
--> after importing  with the alias name, we have to use that alias name in the code....
eg
--
import first_module as am

importing only need function
-------------
--> when we are importing the few functions from the module can only access that function
syntax
--> from(keyword) module_name import(keyword) functions
eg
---
from first_module as am
print am.add(56,8)
print am.subtract(67,8)

importing all functionalities
-------------
--> use all function in that module we have to use (*) to get all of those..
syntax
--> from (keyword) module_name import(keyword) *)

from first_module import *
print(add(67,8))
print(subtract(56,8))
print(mul(22,45))
print(pow(2,3))


import first_module 

print(first_module.add(56,8))
print(first_module.subtract(67,8))


import first_module

first_module.display('vasavi')


import random
print(random.randint(1,2))


import math
print(math.sqrt(25))

import sys
print(sys.version)


details = {
    'name' : 'vasavi',
    'ATM PIN' : '1234'
}
import random
remain_ =3
while remain_>0:
    pin_ = input('Enter pin number: ')
    if pin_ == details['ATM PIN']:
        otp = random.radint(1000,9999)
        print(otp)
        user_otp = int(input('Enter user otp: '))
        if user_otp == otp:
            opt = int(input('enter option \n1.withdraw \n2. deposite'))
        else:
            remain_ == 1
            if remain_> 0:
                    print(f"incorrect pin enterd and you have{remain_}")
            else:
                    print(f"you have enterd 3 times incorrect pin card")
                          
factorial
---------
--> it will give factorial value
 eg
 -----
import math
print(math.factorial(5))

import math
print(math.log(2,3))
print(math.cos(math.pi))
print(math.pi)

random
-------
--> therandom module used to get the random number

import random
print(random.randint(1,100))

randint
-------
--> used to generate random nubers based on the range
eg
----

import random
color = ['red','green','blue','yellow']
print(random.choice(color))
random.shuffle(color)
print(color)

choice
-----
--> it will give the random value from the given data
eg
-----
import random
color =['red','blue','yellow']
print(random.choice(color))

shuffle
-----
--> it will shuufle the data randomly

import random
color = ['red','green','blue','yellow']
print(random.choice(color))
random.shuffle(color)
print(color)

uniform
-----
--> will give the decimal values in a range given
eg
----
import random
print(random.uniform(1,100))


sys
-----
--> sys module is used to ger details of python interperter
import sys
print(sys.version)
print(sys.path)



version
------
--> the version of python interpreter
eg
----
import sys
print(sys.version)
path
----
--> .py path will get by this function
eg
---
import sys
print(sys.platform)

exit
-------
--> this function will exit from the program
eg
-----

import sys
print(sys.exit())

platform
------
--> it will gives the python run platform
eg
----
impot sys
print(sys.platform)

argv
-----
--> it will give the current file run path
eg
----
import sys
print(sys.argv)

datetime
-------
--> used to work with date and time
eg
----
from datetime import datetime,date,time
print(datetime.now())
print(datetime.today)

now
----
--> it will give the today time+date
eg
---
from import datetime
print(datetime.now())

from datetime import datetime
now =datetime.now()
print(now.strftime('%y-%m'))
print(now.strftime("%A"))
print(now.strftime("%B"))
print(now.strftime("%H:%M:%S"))
print(now.strftime("%Y-%m-%d"))

%y ---> will get the year
%m ---> will get the month
%d ---> will get the dat
%h ---> will get the hour
%m --> will get the minute
%s ---> will get the second
%A ---> current day
%B ---> current month

collections
----------
--> the collections module will provide container type data which is more powerfull than buil-in data types(dict,list,tuple
eg
-----
import collections
data = ['apple','banana','orange','pineapple']
print(collections.counter(data))

deque
------
--> used to work with list
eg
------

from collections import deque
how = deque([1,2,3])
how.appendleft(7)
print(how)

extend
-------
from collections import deque
how = deque([1,2,3])
how.extend([4,5,6])
print(how)
pop
------
eg
----
from collections import deque
how = deque([1,2,3])
how.pop()
print(how)

named tuple
-----
eg
-----
from collections import namedtuple
data = namedtuple("stu",('name','age'))
print(data('john','18'))

import itertools
------

from itertools import count
c = count(100)
for j in range(5):
    print(next(c))

count
----

import itertools 
for j in itertools.repeat('python',10):
   print(j)

 permutations
 -----
 eg
 -----
from itertools import permutations

data = permutations ([1,2,3],2)
print(list(data))

combinations
-------
eg
----

from itertools import combinations

any_ = combinations([1,2,3],2)
print(list(any_))
plateforms
-------
eg
--
import platform
print(platform.python_version())
print(platform.python_compiler())
print(platform.machine())
print(platform.processor())


import random
import string

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

# asscii_letters--> this string module function that can give
# Upper and lower letters
# digits --> string module function that can give numbers(0-9)
# punctuation --> this string module function can give us
# punctuation (&$@)
eg
----
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

import random
import string

letters = string.ascii_letters
digits = string.digits
special_char = '&$@'

all_chars = letters + digits + special_char

password = ' '
for i in range(5):
    password += random.choice(all_chars)
    print(password)
    

bank_balance = 1000
from datetime import datetime
import sys
now = datetime,now()

while true:
    print("----welcome to SBI ATM----")
    user_opt = int(input("\n1.withdraw \n2.deposite \n3.check balance"))
    if user_opt == 1:
        with_m = int(input('enter the money you want to withdraw'))
        if with_m> bank_balance:
            bank_balance -= with_m
            print(f'remaining money {bank_balance} {now.strftime("%H:%m %y-%m-%d")}')
      else:
          print('insufficient money')
    elif user_opt == 2:
         deposite_m = int(input('enter the money you want to deposite: '))
         bank_balance += deposit_m
         print(f"money added successfully: {bank_balance} {now.stfrtime("%H:%m %y-%m-%d")}')
    elif user_opt == 3:
        print(f'available balance: bank balance) {now.sfrtime("%h:%m %y-%m-%d")}')
    elif user_opt == 4:
        sys.exit()
    else:
        print("incorrect choice")
        print('thanks for visiting the ATM')
        sys.exit()
                   
import random

num = random.randint(a:1,b:100)
user_opt = int(input("pick a number(1-100): "))
if user_opt == num:
    print(f'you have picked {user_opt} number')
else:
    print('better luck next time')

    
exception handling
-----------
--> an error can be handled by try and except

1.try:
-------
--> we can check the code here which may contain any error
eg
-----
try:
   print(n)
except:
   print('vasavi')

2.except:
---------
--> exception can handle any error that come in the try block
eg
-------
try:
    num = 0
    num_2 = 6
    print(num/num_2)
except:
    print('will get error')

num = 8
num_2 = 0
print(num/num_2)

eg2
--------
try:
    any_ = int(input('enter any number: '))
    print(any_+ 9)
except:
    print('error')
eg
------
try:
    print(9+'python')
except:
    print('error')


3.else:
--------
--> if no error in the code were raised,then the else block will execute..
eg
------
try:
    print(9+5)
except:
    print('error')
else:
    print('no error')
eg
------
try:
    print('python',+9)
    print(9/0)
    print(num)
except ZeroDivisionError:
    print('this will raise ZeroDivisionError')
except NameError:
    print('this will raise NameError')
else:
    print('no error')
        

4.finally
---------
--> the finally block will execute if error present in the try block or not
eg
-----
try:
    print('hello')
    
except ZeroDivisionError:
    print('this will raise ZeroDivisionError')
except NameError:
    print('this will raise NameError')
except TyperError:
    print('this will raise TypeError')
else:
    print('no error')
finally:
    print('end')
    

file handling
-------
--> an file handler is an object used to connect with that particular file....

1.with(keyword)
------
--> by using with keyword no need to close the file, it will close it by itself
syntax
-----
by file name
------
--> with open('file_name or path', 'mode') as name:
by file path
-------
w
eg

    
2.open()
--------
--> by using this open() we have to close the file by using close()
eg
----


modes
-------
1. 'r'
--------
the 'r' mode is used for functions read(),readline() and readlines
eg
----
with open('vasu.py','r') as file:
    file.write('python module take 2 hour per day')
  
2. 'w'
-------
--> the 'w' mode is used for write() function
eg
---
with open('vasu.py','w') as file:
    file.write('python module take 2 hour per day')
    
3. 'a'
--------
--> the 'a' mode is used for write() function and it will add the text at last position
eg
-----
with open('file.txt','a') as file:
    file.write('python module take 2 hour per day')
    
4. 'x'

function
---------
1.write()
2.read()
-------
--> the read() function will read the file chunk by chunk where we can specify the size
eg
-----
with open('vasu.py','r') as file:
    print(file.read(20))

3.readline()
----------
--> it will only read one line at a time with open
('dem.txt','r') as file: 
print(file.readline(20)

4.readlines
---------
---> the readlines() will read whole file and written it in a list, where each line is one index in the list
eg
-----

with open('vasu.py','r') as file:
    print(file.readlines())


    
smtplib module
------------
--> this module is used to send a mail without using mail or outlook by running the python code..
--> and here by using port(587)

how to send a mail by using python
------------
import smtplib

sender_email = 'vasavibantupalli@gmail.com'
sender_app_password = 'aauw cozv ksei vodv'
reciever_mail = 'ujeevana123@gmail.com'

message ="""
Hello,

this mail was sent using python

regards,
python team
"""


server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,sender_app_password)
server.sendmail(
    sender_email,
    reciever_mail,
    message
)

server.quit()
print('email sent successfully')



how to add a subject in sending mail program

import smtplib
from email.Message import Emailmessage

msg = EmailMessage()
sender_email = 'vasavibantupalli@gmail.com'
sender_app_password = 'aauw cozv ksei vodv'
reciever_mail = 'ujeevana123@gmail.com'

msg['from'] = sender_email
msg['to'] = reciever_email
msg['subject'] = 'python Mail'

msg.set_content("""
Hello,

this mail was sent using python

regards,
python team
""")


server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,sender_app_password)
server.send_message(msg)
server.quit()
print('Email sent successfully')






import smtplib
from email.message  import EmailMessage

msg = Emailmessage()
sender_email = 'vasavibantupalli@gmail.com'
sender_app_password = 'aauw cozv ksei vodv'
reciever_email = 'ujeevana123@gmail.com'

msg['from'] = sender_email
msg['to'] = reciever_email
msg['subject'] = 'python Mail'

msg.set_content("""
Hello,

this mail was sent using python

regards,
python team
""")

with open('practiseprograms.py','rb')as file:
    file_content = file.read()
    msg.add_attachment(
    file_content,
    maintype='application',
    subtype='pdf',
    filename='practiseprograms.py'
  )
    
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,sender_app_password)
server.send_message(msg)
server.quit()
print('Email sent successfully')



pip install pyttsx3
pip install speechRecgonition
pip install pyaudio

'''
import pyttx3
import speech_Recognition as sr
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    print('assistant:', text)
    engine.say(text)
    engine.runAndWait()

def take_command():

    recogniser = sr.Recognizer()
    with sr.Mcrophone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = take_command()
        print("you:", command)
        return command.lower()

    except sr.UnknownValueError:
        speak("sorry,i could not understand you.")
        return ""
    except sr.RequestError:
        speak('speech recognition service is unavilable.')
        return ""
    
def wish_user():
    hour = datetime.datetime.now().hour
    if hour<12:
        speak("good morning!")
    elif hour<18:
        speak("good afternoon!")
    else:
        speak("good evening!")
        speak("how can I help you?")
     
def run_assistant(): 
 wish_user()
 while true:
       command = take_command()

       if "hello" in command:
           speak("Hello how can i help you?")
       elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f" the current time is {current_time}")

       elif 'open youtube' in command:
            speak("opening youtube")
            webbrowser.open("https://WWW.youtube.com")
       elif "open google" in command:
            speak("opening google")
            webbrowser.open("https://WWW.google.com")
       elif "exit" in command or "stop" in command:
            speak("goodbye!")
            break
       else:
            speak("i don't know that command yet.")
run_assistant()



        
    








