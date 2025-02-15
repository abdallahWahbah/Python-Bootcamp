########### constructor, methods, public variables
# class Circle:

#     pi = 3.14

#     def __init__(self, radius=1):
#         self.radius = radius

#     def getCircleArea(self):
#         return self.pi * (self.radius ** 2)
    
# circle1 = Circle()
# print(circle1.getCircleArea())

# circle2 = Circle(3)
# print(circle2.getCircleArea())
# print(circle1.pi)




########### Inheritance
# class Animal: # base(parent) class

#     def __init__(self):
#         print('Animal created')

#     def whoAmI(self):
#         print('I am an animal')

#     def eat(self):
#         print('I am eating')

# class Dog(Animal): # derived(child) class
#     def __init__(self):
#         Animal.__init__(self)
#         print('Dog created')

#     # overriding
#     def whoAmI(self):
#         print('I am a dog')

#     def bark(self):
#         print('WOOF!')

# dog1 = Dog()
# dog1.eat()
# dog1.bark()
# dog1.whoAmI()




########### Abstract
# class Animal: # abstract class is a class that can't be implement(can't take an object from it), only acts like a base class (inheritance only)
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         raise NotImplementedError('Subclass must implement this absract method')
    
# class Dog(Animal):

#     # No need to implement __init__
#     def speak(self):
#         print('WOOF!')

# dog1 = Dog('ISSO')
# dog1.speak()




########### Special methods(Magic/Dunder), delete object
# class Book:

#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def __str__(self): # to give a string representation about the class >>> you can print the object directly >> print(str(book1))
#         return f'{self.title} by {self.author}'
    
#     def __len__(self):
#         return self.pages
    
#     def __del__(self):
#         print('An object is deleted')

# book1 = Book('Python rocks', 'Jose', 200)
# print(str(book1))
# print(len(book1))

# del book1 # delete the object from the memory of the computer




########### EXERCISES
class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def getDistance(self):
        x1, y1 = self.coor1 # tuple unpacking
        x2, y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    def getSlope(self):
        x1, y1 = self.coor1 # tuple unpacking
        x2, y2 = self.coor2
        return (y2-y1) / (x2-x1)


coordinate1 = (3,2)
coordinate2 = (8,10)
li = Line(coordinate1,coordinate2)
print(li.getDistance())
print(li.getSlope())