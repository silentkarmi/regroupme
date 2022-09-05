import  bs4
import requests
import os
import pandas as pd

res = requests.get("https://www.nba.com/players")
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
# elems = soup.select("#__next > div.Layout_withSubNav__W2TRe.Layout_justNav__3CIEq > div.MaxWidthContainer_mwc__2OXc5 > section > div > div.flex.flex-wrap.PlayerList_content__Siz9D > div.PlayerList_playerTable__3SEob > div > div > div > table > tbody")

data = []
table = soup.find('table', attrs={'class':'players-list'})
table_body = table.find('tbody')

rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]


    #converting height from ft-inches to cm
    height = cols[4]
    feets_inches = height.split('-')
    height = float(feets_inches[0]) * 30.48 + float(feets_inches[1]) * 2.54
    cols[4] = height

    #converting pounds to kgs
    weight = cols[5].split()[0]
    cols[5] = float(weight) / 2.205
    cols.append(2)
    # data.append([ele for ele in cols if ele]) # Get rid of empty values
    data.append(cols)

# print(data)
df = pd.DataFrame(data)
cwd = os.getcwd()
filename = "nbaplayers.csv"
filepath = (cwd + "\\regroup\\" + filename)

df.to_csv(filepath)

