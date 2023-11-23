from bs4 import BeautifulSoup
import requests

url = "http://www.ibm.com"
data = requests.get(url).text
soup = BeautifulSoup(data, "html5lib")  # create a soup object using the variable 'data'

for link in soup.find_all('a', href=True):  # in html anchor/link is represented by the tag <a>
    print(link.get('href'))

for link in soup.find_all('img'):  # in html image is represented by the tag <img>
    print(link)
    print(link.get('src'))

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
data = requests.get(url).text
soup = BeautifulSoup(data, "html5lib")
print(soup)
table = soup.find('table')  # in html table is represented by the tag <table>
# Get all rows from the table
for row in table.find_all('tr'):  # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td')  # in html a column is represented by the tag <td>
    color_name = cols[2].string  # store the value in column 3 as color_name
    color_code = cols[3].text  # store the value in column 4 as color_code
    print("{}--->{}".format(color_name, color_code))

# import pandas as pd
#
# tables = pd.read_html(
#     'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html')
#
# print(tables[0])
