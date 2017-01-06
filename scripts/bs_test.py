from bs4 import BeautifulSoup
import urllib

r = urllib.urlopen('http://www.espn.com/nba/boxscore?gameId=400899961').read()
soup = BeautifulSoup(r, "lxml")
print type(soup.prettify())
