########### Counter
## counter takes a list or string and returns count of appearance of each element or letter in a dictionary
from collections import Counter

myList = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
myString = 'aaabbbbccccc'
listCounter = Counter(myList)
stringCounter = Counter(myString)

print(listCounter) # Counter({3: 5, 2: 4, 1: 3})
print(stringCounter) # Counter({'c': 5, 'b': 4, 'a': 3})
print(listCounter.most_common()) # [(3, 5), (2, 4), (1, 3)]
print(stringCounter.most_common()) # [('c', 5), ('b', 4), ('a', 3)]
print(list(listCounter)) # [1, 2, 3]
print(list(stringCounter)) # ['a', 'b', 'c']