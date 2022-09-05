import  bs4
import requests
import os
import pandas as pd

res = requests.get("http://www.arkanda.net/sumo/yokozuna-statistics.htm")
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
data = []
page = soup.find('center')
tables = page.find_all('table')
# print(tables)

# yokozunaTableFile = open("yokozuna.txt", "w")
# for table in tables:
#     yokozunaTableFile.write(table.text)
row_count = -1
data = []
for table in tables:
    table_array = None
    rows = table.find_all('tr')
    rows = [value for value in rows if value != '\n']
    number_of_yokuzunas_in_the_table = len(rows[0].find_all('td'))
    
    for row_count in range(1, number_of_yokuzunas_in_the_table):
        actual_row = []
        for row_i in range(1,4):
            cols = rows[row_i].find_all('td')
            col_val = cols[row_count].text
            actual_row.append(col_val)
            

        if actual_row[2] != "[?]":
            height_weight = actual_row[2].split('/')
            height = height_weight[0][:height_weight[0].index("cm")]
            weight = height_weight[1][:height_weight[1].index("kg")]
            actual_row.append(height)
            actual_row.append(weight)
            actual_row.append(3)
            data.append(actual_row)
    
df = pd.DataFrame(data)
cwd = os.getcwd()
filename = "yokozuna.csv"
filepath = (cwd + "\\regroup\\" + filename)

df.to_csv(filepath)

# print(data)




