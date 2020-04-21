import requests
import bs4
ress=requests.get('https://loksabha.nic.in/')
soup=bs4.BeautifulSoup(ress.text,'html.parser')
s=soup.find_all('div',{'class':'update'})
for count in s:
	print(count.findChild('ul').text)