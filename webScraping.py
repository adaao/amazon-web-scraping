import urllib.request
from bs4 import BeautifulSoup

url = "https://www.amazon.com.br/s?k=iphone&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2"
response = urllib.request.urlopen(url)
'''print(response.read())'''
soup = BeautifulSoup(response)

print(soup.prettify())
