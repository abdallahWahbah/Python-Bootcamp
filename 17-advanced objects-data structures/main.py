########### numbers: hex, bin, pow, abs, round

# print(hex(12)) # heaxadecimal: >> 0xc
# print(bin(12)) # 0b1100
# print(2 ** 4, pow(2, 4))# 16 16 
# print(abs(-2)) # 2
# print(round(3.1)) # 3
# print(round(3.9)) # 4
# print(round(3.15635, 2)) # 3.16






########### string: capitalize(first letter), upper(all letter), lower, count(how many letter exists), find(index)....
# text = "hello world"
# print(text.capitalize()) # Hello world
# print(text.upper()) # HELLO WORLD
# print(text.lower()) # hello world
# print(text.count('l')) # 3
# print(text.find('w')) # index of w: 6
# print(text.title()) # Hello World (upper first letter of each word)
# print(text.islower()) # will return True if all cased characters are lowercase
# print(text.isspace()) # return True if all characters are whitespace.
# print(text.istitle()) # return True if text is a title cased string and there is at least one character
# print(text.isupper()) # 
# print(text.endswith('d'))
# print(text.split(' ')) # ['hello', 'world']
# # use partition() to return a tuple including the first occurrence of the separator between the first half and the end half.
# print(text.partition('l')) # ('he', 'l', 'lo world')






########### sets

# mySet = set()
# mySet.add(1)
# mySet.add(1)
# mySet.add(2)
# print(mySet) # {1, 2}
# a, b = mySet
# print(a, b)
# # mySet.clear()
# # print(mySet) 
# setCopy = mySet.copy()
# setCopy.add(6)
# print(setCopy) # {1, 2, 6}
# print(setCopy.difference(mySet)) # {6}
# mySet.discard(2) # delete item


# s1 = {1, 2, 3}
# s2 = {1, 4, 5}
# # s1.difference_update(s2) # removes the common items from s1
# # print(s1) # {2, 3}
# print(s1.intersection(s2)) # {1}

# # intersection_update will update a set with the intersection of itself and another.
# # s1.intersection_update(s2)


# # isdisjoint: return True if two sets have a null intersection.
# # issubset: reports whether another set contains this set.
# # issuperset: report whether this set contains another set.
# # symmetric_difference: Return the symmetric difference of two sets as a new set
# # union: Returns the union of two sets
# print(s1.isdisjoint(s2))
# print(s1.issubset(s2))
# print(s1.issuperset(s2))
# print(s1.union(s2))
# s3 = {1, 2}
# s4 = {1, 2, 4}
# print(s3.symmetric_difference(s4)) # {4}






########### dictionary conprehension

# newDict = {x:x**2 for x in range(10)}
# print(newDict) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# for k in newDict.keys():
#     # print(k)
#     pass

# for k in newDict.values():
#     # print(k)
#     pass

# for key, value in newDict.items():
#     # print(key, value)
#     pass






########### list
myList = [1, 2, 3]
myList.append(4) # [1, 2, 3, 4]
print(myList.count(4)) # 1: how many times the item(param) exsists

# myList.append([5, 6]) # [1, 2, 3, 4, [5, 6]]
myList.extend([5, 6]) # [1, 2, 3, 4, 5, 6]

myList.index(4) # 3 >>> will get error not -1 if item doesn't exist

myList.insert(2, 'inserted item') # at index 2 insert item >>> [1, 2, 'inserted item', 3, 4, 5, 6]
 
myList.pop() # [1, 2, 'inserted item', 3, 4, 5]
myList.pop(2) # [1, 2, 3, 4, 5]

myList.remove(1) # removes the first occurence of a value >>> [2, 3, 4, 5]

myList.reverse() # [5, 4, 3, 2]

myList.sort() # [2, 3, 4, 5]

myList.sort(reverse=True) # [5, 4, 3, 2]


print(myList)