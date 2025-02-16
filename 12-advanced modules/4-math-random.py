####### you can ignore this section

# ## math

# import math

# print(math.floor(5.9)) # remove decimal digits >> 5
# print(math.ceil(1.1)) # next number up >> 2
# print(round(2.2)) # 2
# print(round(2.7)) # 3
# print(math.pi) # 3.141592653589793
# print(math.inf) # inf
# print(math.e) # 2.718281828459045
# print(math.log(math.e)) # 1.0
# print(math.sin(90)) # 0.8939966636005579
# print(math.degrees(math.pi / 2)) # 90.0






## random
import random
print(random.randint(1, 12)) # start, end(including)

# if you want to get the same random number
random.seed(101) # any number (not important)
print(random.randint(1, 10))

myList = list(range(0, 10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(random.choice(myList)) # choose random int from the list


# choose some numbers from a list and construct a list (allow duplication)
print(random.choices(population=myList, k=10)) # [9, 5, 3, 0, 5, 6, 9, 4, 7, 3]
# choose some numbers from a list and construct a list (don't allow duplication)
print(random.sample(population=myList, k=10)) # [7, 1, 4, 8, 6, 0, 3, 2, 5, 9]

random.shuffle(myList) # happens in place (can't assign it to a variable)