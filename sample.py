import requests
from bs4 import BeautifulSoup

#PART ONE BASICS

# # Making a GET request
# r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# # check status code for response received
# # success code - 200
# print(r)

# # Parsing the HTML
# soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())
# print(soup.title)



#PART TWO EXTRACT ALL PRESIDENTS FROM THE FOLLOWING URL

url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

# Lets use the requests get method to fetch the data from url

response = requests.get(url)
# lets check the status
status = response.status_code
print(status)

content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
print(soup.title) # 
#print(soup.prettify()) # gives the whole content of the website
# print(soup.title.get_text()) # gives the text of the title
#print(soup.body) # gives the whole page on the website
# print(soup.body.get_text()) # gives the text of the body
# print(soup.body.find_all('p')) # gives all the paragraph tags in the body
# print(soup.body.find_all('h1')) # gives all the h1 tags in the body
# print(soup.body.find_all('h2')) # gives all the h2 tags in the body
print(soup.body.find_all('table')) # gives all the td tags in the body




## Lets get the tables of all the from the website

tables = soup.find_all('table')

tables = soup.find_all('table', {'cellpadding':'3'})
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
table = tables[0] # the result is a list, we are taking out data from it
for td in table.find('tr').find_all('td'):
    print(td.text)