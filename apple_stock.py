import urllib.request as urllib2
from bs4 import BeautifulSoup
html = urllib2.urlopen('https://finance.yahoo.com/quote/AAPL/history?period1=1571703179&period2=1603325579&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true')
soup = BeautifulSoup(html, 'html.parser')

def main():
    t_rows = soup.findAll("tr", class_="BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)")
    for row in t_rows:
        tds = row.find_all("td")
        try:
            dt = tds[0].text
            open = tds[1].text
            adj_close = tds[5].text
            volume = tds[6].text
            print(f"Date = {dt} | Open = {open} | Adj_close = {adj_close} | Volume = {volume}")
        except IndexError:
            pass


if __name__ == "__main__":
    main()
