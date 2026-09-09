'''

'
num = int(input("enter a number: "))
if num % 2 == 0:
         print("even number")
else:
         print("odd number")

        
num = int(input("number: "))
if num>0:
      print("positive number")
if num<0:
      print("negative number")



1. solve 5&3, 6&9


a = 5
b = 3
sum = a&b
print("5&3 = ", sum)

a = 6
b = 9
sum = a&b
print("6&9 = ",sum)


2. print your name 1515 times

name = "vasavi"
for i in range(1515):
   print(name)



3. take string input change it to float


num = int(input("enter a number: "))
num = float(num)
print("value: ",num)
print("datatype:", type(num))


x = int(input("integer: "))
y = float(x)
print("integer: ",x)
print("float: ",y)


 
length = 3
width = 2
area = length*width
print(area)


5.create a python function to check if a given string is a palindrome.
name = "vasavi welcome"
age = "22"
print(name,age)


3. even or odd
------
number = int(input("Enter an integer: "))
if number % 2 == 0:
    print(f"{number} is an Even number:")
else:
    print(f"{number} is an odd number:")
    

    

4. maximum and minimum
------
list = [1,2,3,4,5]
if max(list)>min(list):
    print("Maximum value:",max(list))
else:
    print("Minimum value:",min(list))

    
5.  palindrome
---------
def palindrome(text):
    if text == text[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")
word = "level"
palindrome(word)


6. principle, amount,rate and time period
--------
p = float(input("Enter the pricipal: "))
r = float(input("Enter the rate: "))
t = float(input("Enter the time: "))
A = p*(1+r/100)**t
CI = A-p
print("Amount=",A)
print("Compound Interest=",CI)


2.
name = 'vasavi'
age = '22'
average = 55

name = "vasavi"
age = "22"
average_test_score = "8.66"
print( "Name:",name)
print("Age:",age)
print("Average Test Score:",average_test_score)
2. greeting message
-----
name = input("enter your name")
age = int(input("enter your age"))

print("Hello," ,name + "!")
print("you are", age,"years old,")
print("welcome! have a great day,")
          
 1.length and width
 ------
num = int(input('enter a width: '))
length = 3
width = 2
area = length*width
print(area)

7. number of days
-----

num = int(input('enter a number of days: '))
years = num/365
weeks = num/7
days =  num%7
print("year: ",years)
print("weeks: ", weeks)
print("days: ",days)
 
8. sum of all positive numbers
----------

num = int(input('enter a integer: '))
sum = 100
for i in range(1,num+1):
    sum = sum+i
    print("sum=",sum)

9.count the numbers of words
---------

sentence =input("enter a sentence:")
words = sentence.split()
print("sentence= ",len(words))

output:
    enter a sentence:  iam going to village
    sentence=  4

 10.
 
num = input("enter a number= ")
a = 10
b = 20
print("a= ",b)
print("b= ",a)

11.name age avg score

name = input('enter your name: ')
age = input('enter your age: ')
avgtestscore = float(input('enter your avgtestscore: '))
print("name: ",name)
print("age:",age)
print("avg test score: ",avgtestscore)

12. create two strings

string1 = input('enter a strng: ')
string2 = input('enter a string: ')
print("string1: ",string1)
print("string2: ",string2)
 
class caluculator:
    def __init__(add,sub,mult,div):
          self.add = add
          self.subtract = sub
          self.multiply = mult
          self.divide = div

    def all_data(self):
        print(self.add)
        print(self.subtract)
        print(self.multiply)
        print(self.divide)

caluculator_1 = caluculator('add','sub','mul','div')
caluculator_1.all_data()

'''
age = int(input())
if age<18:
    raise ageerror
print(":eligible")























          
          
          
