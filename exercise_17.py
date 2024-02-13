"""
Exercise 17 - Decode A Web Page

Note: this is a 4-chili exercise, not because it introduces a concept (although it introduces a new library), 
but because this exercise is more like a project. Feel free to skip this and come back when you're more ready!

Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
"""

# libraries
import requests                     # for looking up websites
from bs4 import BeautifulSoup       # for looking through html code

url = 'https://www.nytimes.com/'
r = requests.get(url)               # response object; can get all info from website using this
r_html = r.text

soup = BeautifulSoup(r_html, features="html.parser")

for link in soup.find_all('p'):
    #print("Name: ")
    print("Name: " + link.string)