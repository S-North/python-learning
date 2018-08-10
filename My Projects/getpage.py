import requests
import bs4

pf = requests.get('https://www.marxists.org/archive/gramsci/1916/12/newspapers.htm')
soup = bs4.BeautifulSoup(pf.content, 'html.parser')

for div in soup.find_all('p'):
    print(div.text)

