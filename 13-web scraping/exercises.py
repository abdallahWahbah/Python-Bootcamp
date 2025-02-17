"""
use the following website to practise scraping

https://toscrape.com/

"""

############ Exercise 1
### GOAL: get title of all books with a 2-star rating (item class is "star-rating Two" of the p that contains the stars)
### https://toscrape.com/

# import requests
# import bs4

# base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

# two_star_items = []

# # res = requests.get(base_url.format(2))
# # soup = bs4.BeautifulSoup(res.text, 'lxml')
# # book = soup.select('.product_pod')[0]
# # print(book.select('a')[1]['title']) # first item title in page number 2


# for n in range(1, 51):

#     scrap_url = base_url.format(n)
#     res = requests.get(scrap_url)

#     soup = bs4.BeautifulSoup(res.text, 'lxml')
#     books = soup.select('.product_pod') # product_pod: the article class name containing the item (image, stars, title...)
    
#     for book in books:
#         if len(book.select('.star-rating.Two')) != 0: # 'star-rating.Two': the p containing stars list
#         # if 'star-rating Two' in str(book): # the same condition
#             book_title = book.select('a')[1]['title']
#             two_star_items.append(book_title)

# print(two_star_items)






############ Exercise 2
### http://quotes.toscrape.com/
"""
TASK: Get the names of all the authors on the first page.
"""
import requests
import bs4

res = requests.get('http://quotes.toscrape.com/')
soup = bs4.BeautifulSoup(res.text, 'lxml')

authors = soup.select('.author')
# I used a set to not worry about repeat authors.
authorsArray = set()

for author in authors:
    authorsArray.add(author.text)

print(authorsArray)


"""
TASK: Create a list of all the quotes on the first page.
"""

quotes = []
for quote in soup.select(".text"):
    quotes.append(quote.text)

print(quotes)

"""
TASK: extract the top ten tags from the requests text shown on the top right from the home page (e.g Love,Inspirational,Life, etc...)
"""

tags = []
for tag in soup.select('.tag-item'):
    tags.append(tag.text)

print(tags)

"""
TASK: Notice how there is more than one page, and subsequent pages look like this http://quotes.toscrape.com/page/2/. 
### loop through all the pages and get all the unique authors on the website
For debugging purposes, I will let you know that there are only 10 pages, 
so the last page is http://quotes.toscrape.com/page/10/, 
but try to create a loop that is robust enough that it wouldn't matter to know the amount of pages beforehand, 
perhaps use try/except for this, its up to you!
"""


url = 'http://quotes.toscrape.com/page/'


#### Possible Solution #1 ( Assuming You Know Number of Pages)

authors = set()

for page in range(1,10):

    # Concatenate to get new page URL
    page_url = url+str(page)
    # Obtain Request
    res = requests.get(page_url)
    # Turn into Soup
    soup = bs4.BeautifulSoup(res.text,'lxml')
    # Add Authors to our set
    for name in soup.select(".author"):
        authors.add(name.text)

print(authors)




#### Possible Solution #2 ( Unknown Number of Pages, but knowledge of last page)
# Choose some huge page number we know doesn't exist
page_url = url+str(9999999)

# Obtain Request
res = requests.get(page_url)

# Turn into Soup
soup = bs4.BeautifulSoup(res.text,'lxml')

page_still_valid = True
authors = set()
page = 1

while page_still_valid:

    # Concatenate to get new page URL
    page_url = url+str(page)
    
    # Obtain Request
    res = requests.get(page_url)
    
    # Check to see if we're on the last page
    if "No quotes found!" in res.text: ## go to the website and request page num 999999999, "No quotes found!" will render on screen
        break
    
    # Turn into Soup
    soup = bs4.BeautifulSoup(res.text,'lxml')
    
    # Add Authors to our set
    for name in soup.select(".author"):
        authors.add(name.text)
        
    # Go to Next Page
    page += 1