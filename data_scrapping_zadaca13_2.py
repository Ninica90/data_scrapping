from BeautifulSoup import BeautifulSoup

from urllib2 import urlopen

import random

url = "https://quotes.yourdictionary.com/theme/marriage/"   #obavezno slash treba staviti na kraj

response = urlopen(url).read()

soup = BeautifulSoup(response)
quotes = []                               

for quote in soup.findAll("p", attrs={"class": "quoteContent"}):       #trazi quotove klase quoteContent
	quotes.append(quote.string)                                        # apendaj stringove iz quotova u listu quotes
#print len(quotes)

available_quotes = []                                                  
while len(available_quotes) < 5:                                        # treba ispisati samo 5 random quotova
	random_quote_index = random.randint(0, len(quotes) - 1)             # random_quote_index je int; 29 quotova, pocinje brojati od 0 pa je max range - 1
	random_quote = quotes[random_quote_index]                           # nova varijabla = trazimo quote na nekom random rednom broju u listi quotes
	if random_quote_index not in available_quotes:                      # kako ne duplicirati iste iteme iz liste!
		available_quotes.append(random_quote_index)                     # appenda samo distinct vrijednosti
		print "- " + random_quote
		


