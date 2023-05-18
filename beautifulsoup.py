from bs4 import BeautifulSoup
import requests

url = 'https://eservices.dor.nc.gov/sau/e536_2022_10_01.jsp'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
tr = soup.find(attrs={'id':'students_name_row'})
td = tr.find(attrs={'class':'w2p_fw'}) 
name = td.text 
print(name)