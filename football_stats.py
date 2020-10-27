import urllib.request as urllib2
from bs4 import BeautifulSoup
html = urllib2.urlopen('https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/?sortcol=td&sortdir=descending')
soup = BeautifulSoup(html, 'html.parser')


t_rows = soup.findAll('tr', class_="TableBase-bodyTr")
def main():
    counter = 0
    for row in t_rows:
        td = row.find_all("td")
        name = td[0].find('a').text.strip()
        position = td[1].find('b')
        team = td[2].find('c')
        touchdown = td[8].text.strip()
        counter += 1
        print(f"Name = {name} | position = {position} | team {team} | TDs = {touchdown}")
        if counter >= 20:
            break





if __name__ == '__main__':
    main()
