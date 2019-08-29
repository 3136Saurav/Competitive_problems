from bs4 import beautifulSoup
import requests
source = requests.get("http://coreyms.com").text
soup = beautifulSoup(source,'html.parser')
print(soup.prettify())
article = soup.find('article')
#print(article.prettify())
#headline = article.h2.a.text
#print(headline)
summary = article.find('div', class_ = 'entry-content').p.text
print(summary)