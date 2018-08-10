import requests
import bs4 as soup


def scrape_page(article, link):
    page = requests.get(link)
    parsed = soup.BeautifulSoup(page.content, 'html.parser')
    text = ''                                       # variable to store the extracted page text
    file_path = 'scrapes/' + str(article) + '.txt'
    print(file_path)                                # DEBUG output the file names & paths

    for div in parsed.find_all('p'):                # find all the <p> tags
        text += (str(div.text) + '\n')               # add all <p> text to text variable and add a new line

    file = open(str(file_path), 'w')                # open/create a file with the link text as its name
    file.write(text)                                # write the extracted text to the file


index_page = requests.get('https://www.marxists.org/archive/gramsci/')
index_parsed = soup.BeautifulSoup(index_page.content, 'html.parser')

for div in index_parsed.select('a[href*=".htm"]'):  # gets all the anchors with ".htm"
    article = div.text
    link = 'https://www.marxists.org/archive/gramsci/' + div['href']    # change rel > abs paths
    invalid_strings = '..'                          # some links traverse folders e.g. ../../index.htm

    if invalid_strings not in (link.split('/')):    # find the invalid directories by splitting the string on /
        scrape_page(article, link)

#DEBUG_THE_FUNCTION scrape_page('Newspapers and the Workers', 'https://www.marxists.org/archive/gramsci/1916/12/newspapers.htm')
