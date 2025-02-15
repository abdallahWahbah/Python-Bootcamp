## Decorator allows you to add extra functionality to existing function




# function accepting and returning function

def helloFromTheOtherSide():
    print('helloFromTheOtherSide')

def hello(someFunction):
    print("hello() function has been executed!")
    someFunction()

    def greet():
        return '\t this is a greet() function inside hello()'
    
    def welcome():
        return '\t this is a welcome() function inside hello()'
    
    
    # print(greet())
    # print(welcome())
    # print('This is internal calling of greet() and welcome() functions')

    print('returning function(s)')
    return (greet, welcome) # of course you can return greet only on welcome only

# hello(helloFromTheOtherSide)
print('-------------------------')
greetingVariable, welcomeVariable = hello(helloFromTheOtherSide)
print(greetingVariable())
print(welcomeVariable())




## Decorator allows you to add extra functionality to existing function
print('-------------------------')
def my_decorator(original_function):
    def wrapper_function():
        print('Some extra code before executing the original function')
        original_function()
        print('Some extra code after executing the original function')
    return wrapper_function

# def func_needs_to_be_decorated():
#     print('AHHHHHHHHHHHHHHHHHHHHHHH')

# my_variable = my_decorator(func_needs_to_be_decorated)
# my_variable()


# the same code as above but using @decorator
@my_decorator
def func_needs_to_be_decorated():
    print('AHHHHHHHHHHHHHHHHHHHHHHH')
func_needs_to_be_decorated()