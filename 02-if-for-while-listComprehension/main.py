################ if statement
# id = 'School'

# if id == 'Bank':
#     print('Your balance is 1000')
# elif id == 'School':
#     print('Number of students: 5623')
# else:
#     print('Mismatch')






################ for loop
# # loop through an array
# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for item in myList:
#     # print even numbers
#     if item % 2 == 0:
#         if item == 4:
#             continue # break: will finish the loop
#         print(item)

# # loop through a tuple
# myTuple = ('a', 'b', 'c')
# for item in myTuple:
#     print(item)

# # loop through an array of tuples
# arrayTuples = [(1, 2), (3, 4), (5, 6)]
# for a, b in arrayTuples:    # for b in arrayTuples: # print the second item of the tuple only
#     print('arrayTuples', a, b)

# # loop through a dictionary
# dict ={'k1': 1, 'k2': 2, 'k3': 3}
# for key in dict: 
#     print(key, dict[key])


# # loop through items in a dictionary
# for item in dict.items():
#     print("items", item) # ('k1', 1)

# # loop through items in a dictionary
# for key,value in dict.items():
#     print("items2222", key, value)

# # loop through keys in a dictionary
# for key in dict.keys():
#     print('key: ', key)

# # loop through values in a dictionary
# for value in dict.values():
#     print('value: ', value)




# useful operators (functions)
# for num in range(3, 10, 2): # from 3 to 10(excluding) print numbers with step size of 2
#     print(num) # 3, 5, 7, 9

# for index, letter in enumerate('abcde'): # for item in enumerate('...') >> item will be a tuple >> (index, value)
#     print(f'At index: {index}, the letter is {letter}')

# # combining lists and looping through them 
# list1 = [1,2,3]
# # # print(max(list1), min(list1))
# list2 = ['a','b','c']
# list3 = [100,200,300]
# for item in zip(list1, list2, list3): # if (for example) the second list of length of 10, it will generate only 3 tuples (shortest list)
#     print(item) # (1, 'a', 100) (2, 'b', 200) (3, 'c', 300)
# # make a list of tuples
# print(list(zip(list1, list2, list3)))


# print('z' in ['a', 'b', 'c'], 'a' in 'a world!', 'key1' in {'key1': 45678}) # False, True, True


# import random
# list = [1,2,3]

# # shuffle: change indexes randomly of items in array
# random.shuffle(list) # doesn't return anything
# print(list)
# print(random.randint(1, 10)) # end (including)






################ while loop
# x = 0
# while x < 5:
#     # if x == 3:
#     #     break
#     print(f'The current value is {x}')
#     x += 1
# else:
#     print('X is now not less than 5') # will be printed one time when the condition is false







################ list comprehension (such as map and filter in js)
# myString = 'hello'
# myList = []

# for letter in myString:
#     myList.append(letter)
# print(myList) # ['h', 'e', 'l', 'l', 'o']

# # the same using list comprehension
# newList = [letter for letter in myString]
# print(newList) # ['h', 'e', 'l', 'l', 'o']


# numArray = [1, 2, 3, 4, 5]
# doubledNumArray = [num * 2 for num in numArray]
# print(doubledNumArray) # [2, 4, 6, 8, 10]
# doubleEvenArray = [num * 2 for num in numArray if num % 2 == 0]
# print(doubleEvenArray) # [4, 8]

# # using if-else in list comprehension
# print([x if x%2==0 else 'ODD' for x in numArray]) # ['ODD', 2, 'ODD', 4, 'ODD']

# # nested loops
# myList = []
# for x in [2, 4, 6]:
#     for y in [1, 10, 100]:
#         myList.append(x * y) # [2, 20, 200, 4, 40, 400, 6, 60, 600]
# print(myList)

# # nested loops in list comprehension
# print([x * y for x in [2, 4, 6] for y in [1, 10, 100]]) # [2, 20, 200, 4, 40, 400, 6, 60, 600]






################ exercises
##### print words that start with 's':
st = 'Sam Print only the words that start with s in this sentence'
for word in st.split(' '):
    if word.lower().startswith('s'):
        print(word)


##### Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
print([num for num in range(1, 51) if num % 3 == 0]) # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]


##### Write a program that prints the integers from 1 to 100. 
# But for multiples of three print "Fizz" instead of the number, 
# and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0 :
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)


##### Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
print([word[0] for word in st])
