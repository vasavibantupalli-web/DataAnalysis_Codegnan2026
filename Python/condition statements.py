'''
1.Generate even and odd numbers for a certain range

eg--
limit_=int(input('Enter the limit: '))
for j in range(1,limit_+1):
    if j%2==0:
        print(f'{j} is a even')
    else:
        print(f'{j} is an odd')

2. check whether the number is a prime or not
num=int(input('Enter a number: '))
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print(f'{num} is prime')
else:
    print(f'{num} is not a prime')


3. Generate prime numbers for a certain limit

limit_=int(input('Enter the limit: '))
for i in range(2,limit_):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(f'{i} is prime')


4. Reverse a string and check if it is palindrom or not

eg--
s=input('Enter: ')
rev_=''
for i in s:
    rev_=i+rev_
if rev_==s:
    print(f'{s} is Palindrom')
else:
    print(f'{s} not a palindrom')

5. draw rightangle triangle using * for a limit
o/p--
*
**
***
****

eg-- 
n=int(input('Enter a num: '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end='') --> end is used to print the starts side by side
    print()  --> print() is used to go to the next line


0/p--
1
12
123
1234
12345


eg--
n=int(input('Enter a num: '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print()

o/p--
1
23
456
78910

eg--
n=int(input('Enter a num: '))
count=0
for i in range(1,n+1):
    for j in range(1,i+1):
        count+=1
        print(count,end='')
    print()

6. reverse tringle
o/p--
*****
****
***
**
*

eg--
n=int(input('Enter a num: '))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print('*',end='')
    print()
    
0/p--
10
98
765
4321

eg--
n=int(input('Enter a num: '))
count=0
for i in range(n,0,-1):
    for j in range(1,i+1):
        count+=1
        print(count,end='')
    print()
    
o/p--
1234
123
12
1

eg--
n=int(input('Enter a num: '))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end='')
    print()

7.  to print piramid
o/p--
    *
   * *
  * * *
 * * * *
* * * * *

eg--
n=int(input('Enter a num: '))
for i in range(n):
    print(' '*(n-i-1),end='') --> to give spaces before  starts
    print('* '*(i+1)) --> to print starts

8. reverse piramid
o/p--
* * * *
 * * *
  * *
   *

eg--
n=int(input('Enter a num: '))
for i in range(n,0,-1):
    print(' '*(n-i),end='')
    print('* '*(i))

-- remove doublicates from the list
eg--

nums=[1,2,2,5,5]
emp_=[]
for j in nums:
    if j not in emp_:
        emp_.append(j)
print(emp_)

9. check whether the given number is a perfect number or not
eg--
num=int(input('Enter a num: '))
per_num=0
for j in range(1, num):
        if num%j==0:
            per_num+=j
if per_num==num:
    print(f'{num} is perfect number')
else:
    print(f'{num} is not a perfect number')


'''
n = int(input('Enter a number:'))
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end='')
    print()
