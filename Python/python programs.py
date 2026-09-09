1 '''
2 -In the 1991 by russom
3 version 0.90
4 what is python?
6 high-level language
7 oops
8 interpretend language
9 -----------
10 -- the will be executed line by line that's the reason python interpretend language
11
12
13 dynamically typed language
14 --------
15 -- no need to mention the type of data pass to the variable..
16
17
18 why
19 ----
20 -easy to learn
21 -less syntax
22 -easy understand
23 -cross platform
24 -open-source
25 -large num of library
26
27 comments
28 -----
29 single-line
30 ------------
31 - this is used to explain line in the code
32
33 multi line
34 -------
35 -u used to comment multiple line using ''' ''', """ """
36
37 variables
38----------
39 this is used to store the datatypes
40
41 good way to define
42 ----------
43
44 -…
'''integer
to find datatype-- type(variable_name)
to find memory--id(variable_name)
------
number = 9

float
-----
num=89.5


num=89.45print(type(num))
---
--> string sequence of char that are inclosed in ('',"",'''  ''')
-->str immutable

method
------
replace()
------
to replace old str with anew str
syntax-- variable_name.replace('old_str','new_str','how many')
eg
--so = 'python is a language python python'
print(so.replace('python','java'))

join()
-----
so ='python is a language'
print('-'.join(So))
--> this method will add the new char after every sub-string
syntax -- 'new_string'.join(variable_name)
eg
--

split()
----
so = 'python is a language'
print(so.split('is'))
so ='python is a language'
print(so.split('is'))

index()
-----
so ='python is a lan…'''
to find datatype -- type(variable_name)
to find memory -- id(variable_name)

datatypes
---------

int
---
number=9
float
-----
num=15.17
print(type(num))

string
------
--> string scqunce of char that are inclosed in  ('', "")
--> string is immutable

method
------
replace()
--------
used to replace old str with new string
syntax-- variable_name.replace('old_str','new_str','how many')
eg--
so='python is a language'
print(so.replace('python', 'java'))
print(so)

join()
------
--> this method will add the new char after every sub-string 
syntax -- 'new_string'.join(variable_name)
eg--
so='python is a language'
print('-'.join(so))

split()
-------
eg--
so='python is a language'
print(so.split(' '))

index()
-------
--> tells character position, finds position
-->indexing means it tells the character in the given index position, finds items
eg--
so='python is a language'
print(so.index('a'))

count()
-------
so='python is a language'
print(so.count('a'))
print(so.count('n',10,16))
indexing:
so='python is a language'
print(so[10])

list
----
-->list is the collection of different datatypesthat are represented in [] and separated by ,
-->mutable datatype
eg--
any_=[1,'python',[2,4]]
print(any_[1][2])
any_=[1,'python',[2,['python',9],4],'java',['python',[56,78],'java',90]]
print(any_[4][0])

methods
------
append() --> this method is used to add new item into the list and it will add at last index position
eg--
any_=[1,2,3,4,5]
any_.append(10)
print(any_)
any_.append("python")
print(any_)

extend() --> it is used to add new item into the end of the list
eg--
any_=[1,2,3,4,5]
any_.extend("python")
print(any_)
any_.append("python")
print(any_)

remove() --> the remove will delete the item based on the value given...
if the value is not in the list will the error
eg--
any_=[1,2,3,4,5]
any_.remove(2)
print(any_)


pop() -->the pop will delete the item based on the index position given...
if the indexx position is out of range in the list will the error
eg--
any_=[1,2,3,4,5]
any_.pop(2)
print(any_)
print(any_.pop())



tuple
--> tuple is collection different datatype that are represented in () and separated by,
--> tuple is immutable
methods
----
index()
------
syntax --variable_name.index(item)
count()
---
syntax--variable_name.count(item)
go = (1,'java',[3,4],('python',78))
print(go.count(('python',78)))
print(go.count(('python',78))) ---o/p-->1
print(go.count('python'))---o/p-->0


go = (1,'java',[3,4],('python',78))
print(go.count(('python',78)))
print(go.count(('python',78))) ---o/p-->1
print(go.count('python'))---o/p-->0

dictionary
-------
--->dict is a key:value pair 
--->leys and values separated by :
--->dict is represented by {}
man={1:9,
'name':'sandy',
(6,7):90,2:90}
methods
-----
1.keys
2.values
3.items
4.update
-----
syntax--dict.update({key:value})



details={'name':'sandy',
         'AC': 123456,
         'aadhar':12346777,
         'Pan':12324359,
         'pin':11234}
details.update({'gender':'female'})
      details['name']='sandy'
print(details)

set
----
-set do not allows duplicate values inside it..
-set mutable..
- set is represented in {}

do = {1,2,3,2}
print(do)
#creating empty set
so = set()
print(type(so))

methods
------
1.update
------
use to add new value into set

syntax-- variable_name.update(itterable)
eg
---
2.add
-----
use to add new value into set

syntax ---variable name.update(value)
do = {1,2,3}
do.add(4)
print(do)

do={1,2,3}
do.update('python')
print(do)

3.remove()
------
used to del the value from the set, incase if the value is not present in the set will get the kayerror

syntax --variable_name.remove(value)
eg
--
do  {1,2,3,4}
do.remove(4)
print(do)

4.discard()
--------
used to del the value from the set, but never give any error incase value is not present inside the et...

syntax --variable_name.remove(value)
eg
--
d0 = {1,2,3}
do.discard(4)
print(do)
5.pop()
-----

used to delete the value but this pop() will take 0 arguments inside it

syntax -- variable_name.pop()

eg
--
do = {1,2,3}
do.pop()
print(do)

operations
------
1.union
--------
gives all sets value together but no duplicates

eg
--
do = {1,2,3}
so = {3,4,5}
print(do|so)
print(do.union(so))

2.intersection
-----
eg
--
do = {1,2,3}
so = {3,4,5}
print(do&so)
print(do.intersection(so))


3.difference
------------
eg
--
do = {1,2,3}
so = {3,4,5}
print(so - do)
print(do.difference(so))

TYPE CONVENTION
Int : string:Float
string -- str()
eg
--
num = 9
print(type(num))
so = str(num)
print(type(so))

Float
-----
 string --str()
 Integer
 eg
 ---
 print(type(so))
nums = 8.67
print(type(nums))
all_ = int(nums)
print(all_)
print(type(all_))


string
-------
eg
-- 
how = "67"
print(type(how))
who = int(how)
print(type(who))

list--list
eg
--
how ='2345'
print(type(how))
who = list(how)
print(who)
print(type(who))

tuple -- tuple()

eg
--
how ='2345'
print(type(how))
who = tuple(how)
print(who)
print(type(who))

list
------
eg
--
nums = [1,2,3,4]
print(type(nums))
all_n = list(nums)
print(type(all_n))


string -- str()
eg
--
nums = [1,2,3,4]
print(type(nums))
all_n = str(nums)
print(type(all_n))


tuple -- tuple()
eg
--
nums = [1,2,3,4]
print(type(nums))
all_n = tuple(nums)
print(type(all_n))

tuple
---
list -- list()
string -- str()
eg
--
nums = [1,2,3,4]
print(type(nums))
all_n = list(nums)
print (all_n)
print(type(all_n))

string -- str()
eg--
nums = [1,2,3,4]
print(type(nums))
all_n = str(nums)
print(type(all_n))

(+)concatination
s = [1,2,3,4]


'''
do = {1,2,3}
do.update([6,8])
print(do)
do={1,2,3}
do.update('python')
print(do)
do = {1,2,3}
do.add(4)
print(do)
do = {1,2,3,4}
do.remove(4)
print(do)
d0 = {1,2,3}
do.discard(4)
print(do)
do = {1,2,3}
do.pop()
print(do)
do = {1,2,3}
so = {3,4,5}
print(so - do)
print(do.difference(so))
num = 9
print(type(num))
so = str(num)
print(type(so))
nums = 8.67
print(type(nums))
all_ = int(nums)
print(all_)
print(type(all_))
how ='2345'
print(type(how))
who = tuple(how)
print(who)
print(type(who))
nums = [1,2,3,4]
print(type(nums))
all_n = str(nums)
print(type(all_n))
