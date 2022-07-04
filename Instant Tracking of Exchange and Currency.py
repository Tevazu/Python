import requests
from bs4 import BeautifulSoup

url = "https://www.doviz.com/" # Type the site's URL
response = requests.get(url) # Take the website using reqeuests.get()

html_content = response.content # Take the content of website using response.content
soup = BeautifulSoup(html_content, "html.parser") # We use "html.parser" with BeautifulSoup to tear the website

# Now we need to find which tag and class or key word is including our data. To do this we examine the website
# In this website, our data is in "span" tag and "data-socket-key" key word
# Take data and key word in text format for all monetary unit

GRAM_GOLD = soup.find("span", {"data-socket-key":"gram-altin"}).text # Take data and key word in text format
DOLAR = soup.find("span", {"data-socket-key":"USD"}).text # Take data and key word in text format
EURO = soup.find("span", {"data-socket-key":"EUR"}).text # Take data and key word in text format
STERLİN = soup.find("span", {"data-socket-key":"GBP"}).text # Take data and key word in text format
BIST_100 = soup.find("span", {"data-socket-key":"XU100"}).text # Take data and key word in text format
bitcoin = soup.find("span", {"data-socket-key":"bitcoin"}).text # Take data and key word in text format

print("Gram Gold:", GRAM_GOLD) # Print all objects
print("Dolar:", DOLAR)
print("Euro:", EURO)
print("Sterlin:", STERLİN)
print("Borsa İstanbul:", BIST_100)
print("Bitcoin:", bitcoin)






