from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://t.me/+sAwQeJpRoakwYzFk'

wiki_url='https://en.wikipedia.org/wiki/List_of_most-followed_Instagram_accounts'

table_class='wikitable sortable jquery-tablesorter'
# it doesn't find it with table class don't know why yet
table_name = 'wikitable sortable'



response = requests.get(wiki_url)
soup = BeautifulSoup(response.text, 'html.parser')

soup_table = soup.find('table', {'class':table_name})
# print(soup_table)


pd.set_option('display.max_columns',3000)
pd.set_option('display.max_rows',500)
pd.set_option('display.min_rows',500)
df = pd.read_html(str(soup_table))

# pd.set_option('display.max_col_width',150)
# pd.set_option('display.width',120)
# pd.set_option('display.frame_repr',True)

print(type(df),len(df[0]),type(df[0]))
for pd in df:
        # print(i)
        pd.to_csv('out.csv',sep=',')
  
# print( requests.get(url).text )