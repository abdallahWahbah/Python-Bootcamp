"""
#### installing libraries
# pip install requests
# pip install lxml
# pip install bs4
"""

import requests
import bs4       # beautiful soup

pageSource = requests.get('https://en.wikipedia.org/wiki/Ahmed_Zewail')
soup = bs4.BeautifulSoup(pageSource.text, 'lxml')
# print(soup) # will print the source page as it is not as a simple text


# scraping page title, and first paragraph
pageTitle = soup.select('title')[0].getText() # Ahmed Zewail - Wikipedia
firstParagraph = soup.select('p')[0].getText()
print(pageTitle, firstParagraph)


# scraping a random list
list = soup.select('.external')
print(list)
for item in list:
    print(item.text)


# scraping image and downloading it in my computer
zewailImage = soup.select('.mw-file-element')[1]['src']
# if you want to see the full link, just add "https:" before zewailImage result (cause i selected egypt flag not zewail)
imageLink = requests.get("https:" + zewailImage)

f = open('zewait_image.JPG', mode="wb") # image new name with the same extension (JPG), mode = write binary
f.write(imageLink.content)
f.close()