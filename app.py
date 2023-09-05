"""
from math import *

print(sqrt(100))

""
name = input('Input your name: ')
age = int(input('input your age: '))

print('welcome' , name , 'you are' , age, 'old')

"""
# word replacement exercise
"""
sentence = input('Enter your sentence: ')
print('your sentence is:' ,sentence)
word1 = input('enter the word to replace: ')
word2= input('enter the word to replace it with: ')
print(sentence.replace(word1, word2))
"""

#lists
"""
countries=['uk', 'usa', 'canada']
print(countries[2][0])
print(countries[1:2])
countries[0]='nig'
print(countries)
print(type(countries))
"""

#list constructor
"""
countries2= list(('nigeria', 34, False))
print(countries2)
"""

#list functions
"""
list1 = [1,2,3,4,5]
list2 = ['banana', 'apple','mango']
list2.append('cherry')
list2.insert(1, 'figs')
list2.remove('banana')
print(list2.index('mango'))
list1.extend(list2)
print(list1)
"""

#functions
"""
user = input('Enter your name: ') 

def welcomeMessage(n):
    print('welcome', n)

welcomeMessage(user)

def add_number(a,b):
    return a + b

num1 = int(input('enter a number: '))
num2 = int(input('enter another number: '))

print(add_number(num1, num2))
"""

#if statements
"""
value = input('Input a value: ')

if type(value) == str:
    print(value, 'is a string')
else:
    print(value, 'is not a string')
"""

