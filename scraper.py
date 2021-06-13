# Scrapes Covid-19 data from "https://www.worldometers.info/"
# and prints out the data sorted(in descending order) according to the number of cases.
import requests
from bs4 import BeautifulSoup
import texttable as tt
table = tt.Texttable()

url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

result = []

result_iterator = iter(soup.find_all('td'))

while True:
	try:
		country = next(result_iterator).text
		cases = next(result_iterator).text
		deaths = next(result_iterator).text
		continent = next(result_iterator).text

		result.append((
			country,
			int(cases.replace(',', '')),
			int(deaths.replace(',', '')),
			continent
		))

    # Break when there's no more result
	except StopIteration:
		break

# Sort the result by the number of cases
result.sort(key = lambda row: row[1], reverse = True)

# Add an empty row at the beginning for the headers
table.add_rows([(None, None, None, None)] + result)
 
table.set_cols_align(('c', 'c', 'c', 'c')) 
table.header((' Country ', ' Cases ', ' Deaths ', ' Region '))

print("Data can be found on: https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/")
print()
print(table.draw())
