# Dynamic typing

ourVariable = 2
print(2)
ourVariable = "This is dynamic typing"
print(ourVariable, len(ourVariable))
print(ourVariable[-2]) # n
print(ourVariable[2:]) # from index 2 to the end >> is is dynamic typing
print(ourVariable[:3]) # from beginning to index 3 (excluding) >>> Thi
print(ourVariable[::2]) # from beginning to end with step of 2 >> Ti sdnmctpn
print(ourVariable[::-1]) # reverse the string >> gnipyt cimanyd si sihT
nameSam = 'Sam' # convert it to Pam
print('P' + nameSam[1:].upper()) # PAM

splitOldVar = "Hello World"
print(splitOldVar.split(" ")) # ['Hello', 'World']
# Strings are not mutable! (meaning you can't use indexing to change individual elements of a string)

# # type
# print(type("Hello")) # <class 'str'>
# print(type(123)) # <class 'int'>
# print(type(5.56)) # <class 'float'>
# print(type(True)) # <class 'bool'>

# to remove item at a certain index in an array, pass the index to pop()
import random
numberArray = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five']
print('rrrrrrrrrrandom', random.choice(numberArray))
numberArray.pop(2)
print(numberArray)
letterArray = ['z', 'y', 'a', 'c', 'b']
letterArray.sort() # works well with numbers also,  doesn't return anything, sort in place
print(letterArray)
letterArray.reverse()
print(letterArray)


myTuple = ('a', 'a', 'b')
print(myTuple.count('a'))

# sets are unordered collection of unique elements
mySet = set()
mySet.add(1)
mySet.add(2)
mySet.add(2)
print(mySet) # {1, 2}
repeatedItemsArray = [1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 4, 4]
print(set(repeatedItemsArray)) # {1, 2, 3, 4}



# files
# if you have a file that contains list of lines)
# data = []
# with open('file.txt') as data_file:
#     lines = data_file.readlines()
#     for line in lines:
#         data.append(line.strip())

# print(data)

# # write to file
# # if file doesn't exist, it will create a file for you
# with open('new_file.txt', mode='a') as file: # mode='r': read only(default), w: wrie(override everything), a: append(add to existing)
#     file.write('\nNew Line')


# comparison
print(1 < 3 > 2) # True >>> just read the following conditions to learn how to write a condition
# 1<3 and 3>2
# 1==2 or 2<3
# not 400 > 500