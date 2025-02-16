# import re # regular expression

# text = 'The agent\'s phone number is 444-354-5000 call soon!, another phone text'
# print('phone' in text) # True


# pattern = 'phone'
# match = re.search(pattern, text)
# print(match.start(), match.end()) # index >>> if multiple matches, you will get the index of the first match only

# matches = re.findall('phone', text)
# print(matches) # ['phone', 'phone']
# for x in re.findall('phone', text):
#     print(x)



"""
#### REGULAR EXPRESSION PATTERNS

character           description                     example pattern                 example match

\d                  Digit                           file_\d\d                       file_25
\w                  Alphanumeric(letter/number)     \w-\w\w\w                       A-b_2
\s                  White Space                     a\sb\sc                         a b c
\D                  Non Digit                       \D\D\D                          XYZ
\W                  Non Alphanumeric                \W\W\W\W                        *-+=
\S                  Non White Space                 \S\S\S\S                        ashg

#### QUNATIFIERS

character           description                     example pattern                 example match

+                   Occurs one or many times        Version \w-\w+                  Version A-B_1
{3}                 Occurs exactly 3 times          \w{3}                           Gja
{2, 4}              Occurs 2 to 4 times             \d{2, 4}                        859
{3, }               Occurs 3 times or more          \w{3, }                         ad4522a
*                   Occurs zero or more             A*B*C*                          AAACC
?                   Occurs once or none             plurals?                        plural

"""
import re
myText = "My phone number is 444-652-7845"

phoneNumber = re.search(r"\d{3}-\d{3}-\d{4}", myText)
print(phoneNumber.group()) # 444-652-7845




## multiple pattern codes (separated by paranthesis () ) (to divide the pattern to group)
phonePattern = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
results = re.search(phonePattern, myText)
print(results.group()) # 444-652-7845
print(results.group(1)) # pattern starts with index 1 not 0 >>> 444
print(results.group(2)) # 652
print(results.group(3)) # 7845




## or
print(re.search(r'cat|dog', 'This is a cat').group()) # cat




## wild card >> the following '.' will act like a wild card, to match words that can replace '.' with any letter 
print(re.findall(r'.at', 'The cat in the hat sat there')) # ['cat', 'hat', 'sat']
print(re.findall(r'...at', 'The cat in the hat went splat')) # ['e cat', 'e hat', 'splat']




## start with, end with
print(re.findall(r'^\d', '1 is a number')) # ['1'] >>> search at the beginning of the text, if the number is in the middle, it won't match
print(re.findall(r'^\d', 'number: 2')) # []
print(re.findall(r'\d$', '1 is a number')) # []
print(re.findall(r'\d$', 'number: 2')) # ['2']




## exclude and include using []




## To exclude characters, we can use the ^ symbol in conjunction with a set of brackets []. Anything inside the brackets is excluded.
phrase = 'There is 3 main 35 inside 249 this why!'
pattern = r'[^\d]+' # '+' : occurs one or many times
print(re.findall(pattern, phrase)) # ['There is ', ' main ', ' inside ', ' this why!']

# remove punctuation
testPhrase = "This is a strin! but it has punctuation. How can we remove it?"
testPattern = r'[^!.?]+'
print(re.findall(testPattern, testPhrase)) # ['This is a strin', ' but it has punctuation', ' How can we remove it']




# we can use brackets to group together options
testPhrase2 = 'You find the hypen-words in this sentence, but you do not know how long-ish they are' 
# print words having dash in the middle
testPattern2 = r'[\w]+-[\w]+'
print(re.findall(testPattern2, testPhrase2)) # ['hypen-words', 'long-ish']




# Parenthesis for Multiple Options
# Find words that start with cat and end with one of these options: 'fish','nap', or 'claw'
text = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"

print(re.search(r'cat(fish|nap|claw)',text).group()) # catfish
print(re.search(r'cat(fish|nap|claw)',texttwo).group()) # catnap
print(re.search(r'cat(fish|nap|claw)',textthree).group()) # caterpillar