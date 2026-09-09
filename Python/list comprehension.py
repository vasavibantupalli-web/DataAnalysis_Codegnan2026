'''
list comprehension
-----
--> the comprehension is the short form of syntax used to generate a new list from the old list...
syntax--> [expression loop]


nums = [1,2,3,4]
new_l = [j if j% 2==0 else 'odd' for j in nums]
print(new_l)


nel_ = [i for i in nums if i%2 !=0]
print(nel_)

nested comprehension
---------------
--> nested comprehension means an comprehension inside the another comprehension is called nested comprehension...
syntax --> [expression loop_1 and loop_2]

match = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
any_ = [i for i in match]
all_ = [num for j in match for num in j]
print(any_)
print(all_)


new_ = [[i*j for j in range(1,6)] for i in range(1,6)]
ne = [i for i in range(1,6)]
print(ne)
print(new_)

generator
------
--> this generator will generate values one at a time and pause it on the same position when we are using yield keyword
--> here we will use yield to get the value
yield keyword
----------
--> this yield() use to get the value and will only gives one value and pauses there itself

next keyword
---------
-->the next() will retrieve the value
'''

def gen(n):
    for i in range (1,n+1):
        yield i*i
a = gen(5)
print(next(a))
print(next(a))
print(next(a))




        




