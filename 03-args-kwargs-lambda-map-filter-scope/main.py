################ default and simple example
# def say_hello(name='Abdallah'):
#     print(f'Hello Mr {name}')

# def checkEven(number):
#     return number % 2 ==0

# def checkEvenNumberList(list):
#     for num in list:
#         if num % 2 == 0:
#             return True
#     return False
# say_hello()
# say_hello('Wahbah')
# isEven = checkEven(21)
# print(isEven)
# print(checkEvenNumberList([1, 3, 5, 7]))
# print(checkEvenNumberList([2, 4, 6]))




################ Tuple unpacking

# employs = [('Abdallah', 20), ('Mahmoud', 10), ('Wahbah', 100)]

# def whoWorksMost(employees):
#     max_hours = 0
#     employee_name = ''

#     for name, hours in employees:
#         if hours > max_hours:
#             max_hours = hours
#             employee_name = name
#         else: # not important
#             pass
        
#     return (employee_name, max_hours) # tuple

# employeeNameOfTheMonth, numerOfHours = whoWorksMost(employs)
# print(employeeNameOfTheMonth, numerOfHours)




################ *args: arguments(rest in js), **kwargs: keyword arguments
## conclusion: *args constrcuts a tuple, **kwargs constructs a dictionary 
## *args is like rest in js, but constructs a tuple not array
## you can change args to any name and use it (the important in ths * as indicator)
# def my_func_args(*args):
#     print(args) # tuple not array
#     # you can loop through it using for

# my_func_args(1, 2, 3, 4, 5, 6)

# ## **kwargs create a dictionary of key-value pairs
# ## you can change kwargs to any name and use it (the important in ths ** as indicator)
# def my_func_keyword_args(**kwargs):
#     print(kwargs) # {'fruit': 'Apple', 'price': 100}
#     for key, value in kwargs.items():
#         print(f'the key is {key}, and its value is {value}')

#     if 'fruit' in kwargs:
#         print('Hellooooooooooo')

# my_func_keyword_args(fruit='Apple', price=100)

# ## use of *args and **kwargs together
# ## all #args should all of them behind each other (not at beginning and after **kwargs)
# def food(*args, **kwargs):
#     print(f'I would like {args[0]} pieces of {kwargs['food']}')

# food(10, 20, 30, fruit='Apple', food='Egg', animal='dog')




################ Exercises

## OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# def old_macdonald(name):
#     return name[0].upper() + name[1:3] + name[3].upper() + name[4:]
#     # firstWord = name[:3]
#     # secondWord = name[3:]
#     # return firstWord.capitalize() + secondWord.capitalize()

# result = old_macdonald('macdonald') # MacDonald
# print(result)


# ## Given a sentence, return a sentence with the words reversed
# def master_yoda(word):
#     wordList = word.split()
#     reversedList = wordList[::-1]
#     return '-'.join(reversedList)

# print(master_yoda('Hello I am Abdallah')) # Abdallah-am-I-Hello


# ## Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# def check3Occurence(nums):
#     for i in range(0, len(nums) - 1):
#         if nums[i] == 3 and nums[i + 1] == 3:
#             return True
#     return False
# print(check3Occurence([1, 3, 4])) # False
# print(check3Occurence([1, 3, 3])) # True


# ## duplicate each char 3 time
# def duplicateChar(name):
#     result = ''
#     for char in name:
#         result += char * 3 # char + char + char

#     return result


## to check if item exists in array >>>> if 11 in [1, 11, 23]


# ## SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
# ## spy_game([1,2,4,0,0,7,5]) --> True
# ## spy_game([1,0,2,4,0,5,7]) --> True
# ## spy_game([1,7,2,0,4,5,0]) --> False
# def spy_game(list):
#     code = [0, 0, 7, 'X']
#     for num in list:
#         if num == code[0]:
#             code.pop(0)
#     print(len(code) == 1)
#     # for i in range(0, len(list) - 2):
#     #     if list[i] == 0 and list[i+1] == 0 and list[i+2] == 7:
#     #         print('True')
#     #         return True
#     # print(False)
#     # return False
# spy_game([1,2,4,0,0,7,5])
# spy_game([1,0,2,4,0,5,7])
# spy_game([1,7,2,0,4,5,0])




################ Lambda expressions, Map, Filter

# ## map
# def square(number):
#     return number ** 2
# numbers = [1, 2, 3, 4]

# for item in map(square, numbers):
#     print(item)
# mySquareNumbers = list(map(square, numbers)) # [1, 4, 9, 16]
# print(mySquareNumbers)

# def splicer(myString):
#     if len(myString) % 2 == 0:
#         return 'EVEN'
#     else:
#         return myString[0]
# names = ["ANDI", 'EVE', "SALLY"]
# mySplicedNames = list(map(splicer, names)) # ['EVEN', 'E', 'S']
# print(mySplicedNames)

# ## filter
# def checkEven(number):
#     return number % 2 ==0
# myNumbers = [1, 2, 3, 4, 5, 6]
# myEvenList = list(filter(checkEven, myNumbers))
# print(myEvenList) # [2, 4, 6]

# ## lambda expression in an anonymous function and we don't use them usually
# def double(number):
#     return number * 2

# doubleLambda = lambda num: num * 2
# print(doubleLambda(16))

# ## use of lambda with map or filter
# oldNumbers = [1, 2, 3, 4]
# lambdaSquaredListWithMap = list(map(lambda num: num * 2, oldNumbers))
# print(lambdaSquaredListWithMap) # [2, 4, 6, 8]
# lambdaCheckEvenListWithFilter = list(filter(lambda num: num % 2 == 0, oldNumbers))
# print(lambdaCheckEvenListWithFilter) # [2, 4]




################ Nested statements and Scope

# x = 25 
# def printer():
#     x = 50
#     return x

# print(x) # 25
# print(printer()) # 50

# ## explanation: the function will try to take the value from inner(local) to outer(enclosing: explained belowe) to outer(global)

# name = 'GLOBAL string scope'

# def greet():
#     name = 'ENCLOSING string scope'

#     def hello():
#         name = 'LOCAL string scope'
#         print('Hello ' + name)
#     hello()
# greet() # Hello LOCAL >> if you commented the 'LOCAL' name, it will print the outer with is enclosing (ENCLOSING) 
# # and if there is no 'ENCLOSING', it will take the outer with is the 'GLOBAL'

# ## changing global variables

# y = 50
# def myFunction(y):
#     print(f'Y is {y}')

#     # LOCAL REASSIGNMENT
#     y = 200 # this change will affect the local y only not the global ont
#     print(f'Changed y to be {y}')

# print(myFunction(y)) # 50, Changed y to be 200
# print(y) # 50

# ## when declaring a variable inside a function, it has scope only local to that function

# ## if you want to change y global not the local one only, put (global y) and remove y from param
# print('----------------')

# newY = 90
# def myFunctionGlobalChange():
#     global newY

#     newY = 120
#     print(f'newY chnaged globally to {newY}')

# print(newY) # 90
# print(myFunctionGlobalChange()) # newY chnaged globally to 120
# print(newY) # 120




################ Exercises

## Write a function that checks whether a number is in a given range (inclusive of high and low)
# def checkNumberExist(num, low, high):
#     return num in range(low, high+1)

## Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
# def countUpperLowerCase(string):
#     lowerCount = 0
#     upperCount = 0
#     # dict = {'lower': 0, 'upper': 0}

#     for letter in string:
#         if letter.islower():
#             lowerCount += 1
#             # dict['lower'] + 1
#         else: 
#             upperCount + 1
#             # dict['upper'] + 1
#     return (lowerCount, upperCount)


## Write a Python function that takes a list and returns a new list with unique elements of the first list.
## Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
## Unique List : [1, 2, 3, 4, 5]

# def uniqueItems(listParam):
#     return list(set(listParam)) # you can loop through the listParam with condition  >>>> if x not in listParam, and add it to a new list
# print(uniqueItems([1,1,1,1,2,2,3,3,3,3,4,5])) # [1, 2, 3, 4, 5]


## palindrome

# def checkPalindrome(s):
#     s = s.replace(' ', '')
#     return s == s[::-1]


## pangram: words or sentences containing every letter of the alphabet at least once 
import string
def pangram(sentence, alphabet = string.ascii_lowercase):
    sentence = sentence.replace(' ', '')
    sentence = sentence.lower()
    sentence = set(sentence)
    alphabet = set(alphabet)
    return alphabet == sentence