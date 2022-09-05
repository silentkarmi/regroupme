import  bs4
import requests
import os
import pandas as pd

res = requests.get("https://www.topendsports.com/events/summer/science/athletics-marathon.htm")
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
data = []
table = soup.find('table', attrs={'class':'list'})
rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    
    if not cols:
        continue

    #converting height from ft-inches to cm
    height = cols[3]
    weight = cols[4]
    if height.strip() == '-' or weight.strip() == '-':
       continue

    feets_inches = height.split(' ')
    # print(feets_inches)
    height = float(feets_inches[3]) * 30.48 + float(feets_inches[5]) * 2.54
    cols[3] = height

    #converting pounds to kgs
    weight = weight.split()[3]
    cols[4] = float(weight) / 2.205

    cols.append(1)

    # data.append([ele for ele in cols if ele]) # Get rid of empty values
    data.append(cols)

# print(data)
df = pd.DataFrame(data)
cwd = os.getcwd()
filename = "elitemarathoners.csv"
filepath = (cwd + "\\regroup\\" + filename)

df.to_csv(filepath)

