"""
Exercise 19 - Decode a Web Page Two

Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on 
this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so 
that you can read the full article without having to click any buttons.
"""

# libraries
import requests                     # for looking up websites
from bs4 import BeautifulSoup       # for looking through html code

url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, features="html.parser")

print(soup.text)