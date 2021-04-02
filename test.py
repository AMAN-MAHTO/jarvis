from bs4 import BeautifulSoup
import requests

url ='https://www.google.com/search?q=who+is+the+prime+minister+of+india'

response = requests.get(url)
result = BeautifulSoup(response.text,'html.parser')
# print(result)
# print(result.select('a'))
for link in result.select('a'):
   # print(link)
   x=link.get('href')
   if 'url' in x:
      print(x)
