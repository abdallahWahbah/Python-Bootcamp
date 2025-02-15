try:
    # result = 10 + '10'
    # result = 10 / 0
    result = 10 + 10
except: # executed if there is error in try 
    print('You are not adding correctly')
else: # executed if try executed successfully 
    print('Add went well')
    print(result)
finally: # executed whether there is an error or not
    print('I always run, Bye')


# write try/except
try:
    with open('testfile', mode='w') as file:
        file.readlines() # error cause mode is w(write) and you try to read
except TypeError:
    print('There is a type error')
except OSError:
    print('You have an OS Error')
except:
    print('All other exceptions')
finally:
    print('I always run')


# number try/except
while True:
    try:
        inputValue = int(input('Please enter a number '))
    except:
        print('You need to enter a numeric value')
    else:
        print('Thanks')
        break
    finally:
        print('I always run, Bye')