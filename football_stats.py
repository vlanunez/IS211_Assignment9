import urllib.request as urllib2
from bs4 import BeautifulSoup
html = urllib2.urlopen('https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/?sortcol=td&sortdir=descending')
soup = BeautifulSoup(html, 'html.parser')

def main():
    t_rows = soup.findAll('tr', class_="TableBase-bodyTr")
    counter = 0
    print("Here are the 20 players currently with the most touchdowns:")
    for row in t_rows:
        td = row.find_all("td")
        name = td[0].find('a').text.strip()
        position = td[0].find("span", attrs={'class': "CellPlayerName-position"}).text.strip()
        team = td[0].find("span", attrs={'class': "CellPlayerName-team"}).text.strip()
        touchdown = td[8].text.strip()
        counter += 1
        print(f"Name = {name} | position = {position} | team {team} | TDs = {touchdown}")
        if counter >= 20:
            break


if __name__ == '__main__':
    main()
