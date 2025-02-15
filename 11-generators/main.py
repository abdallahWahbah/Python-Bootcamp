def createCubes(n):
    result = []

    for i in range(n):
        result.append(i**3)
    return result

print(createCubes(10)) # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

# using generator (the same result but will not take much space in memory) (more memory efficient)

def createCubes2(n):
    for i in range(n):
        yield i **3

print(createCubes2(10)) # <generator object createCubes2 at 0x000001856B1A36B0>
print(list(createCubes2(10))) # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
for x in createCubes2(10):
    print(x)




def simpleGenerator():
    for i in range(3):
        yield i

g = simpleGenerator()
print(next(g)) # 0
print(next(g)) # 1
print(next(g)) # 2





######## EXERCICES

## Create a generator that generates the squares of numbers up to some number N.
def squaresGenerator(n):
    for i in range(n):
        yield i

for i in squaresGenerator(10):
    print(i)


## Use the iter() function to convert the string below into an iterator:
s = 'hello'
s = iter(s)
print(next(s)) # h
print(next(s)) # e
print(next(s)) # l
print(next(s)) # l
print(next(s)) # o


## Explain a use case for a generator using a yield statement where you would not want to use a normal function with a return statement.

# If the output has the potential of taking up a large amount of memory and you only intend to iterate through it, 
# you would want to use a generator.