from bs4 import BeautifulSoup
import  requests
import pandas as pd

url = "https://www.banki.ru/products/currency/cb/"
page = requests.get(url)
soup = BeautifulSoup(page.text,"lxml")
table = soup.find("table", class_="standard-table standard-table--row-highlight")
headers= []
for i in table.find_all("th"):
    title=i.text
    headers.append((title))

mydata = pd.DataFrame(columns = headers)

# Create a for loop to fill mydata
for j in table.find_all("tr")[1:]:
    row_data = j.find_all("td")
    row = [i.text for i in row_data]
    length = len(mydata)
    mydata.loc[length] = row

# Drop and clearing unnecessary rows
mydata.drop(mydata.index[1:40], inplace=True)
mydata.reset_index(inplace=True, drop=True)
print(headers)
print(type(mydata))