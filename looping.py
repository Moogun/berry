import pandas as pd
from pyxing.session import *
from pyxing.query import *

f = open("account.txt", "rt")
lines = f.readlines()
id = lines[0].strip()
pwd = lines[1].strip()
cert = lines[2].strip()
f.close()

# Login
xasession = XASession()
xasession.login(id=id, password=pwd, cert=cert, block=True)
print("서버: ", xasession.get_server_name(), " connected - ", xasession.is_connected(), " accountList(0) - ",
      xasession.get_account_list(0))

df = pd.read_excel('candidate2.xlsx')
shcode = df['shcode']
price = df['price']

# Query
xaquery = XAQuery()

""" LOGIC  
    1. loop the candidate
    2. make a network request 
    3. get the current price 
    4. update the candidate table   
"""

def monitor_price(shcode) -> tuple[pd.DataFrame, str]:
    t1102 = xaquery.block_request('t1101', shcode=shcode)
    return t1102

# for index, row in df.iterrows():
#     print(row['shcode'])
#     comp_code = row['shcode']
comp_code = '042670'

p = monitor_price(comp_code)
table = p[0]
print('table', table)

newPrice = table['price']
print('newPrice', newPrice)

open = table['open']
high = table['high']
low = table['low']
diff = table['diff']

# df.loc[index, 'new_price'] = newPrice
# df.loc[index, 'open'] = open
# df.loc[index, 'high'] = high
# df.loc[index, 'low'] = low

df['new_price'] = newPrice
df['open'] = open
df['high'] = high
df['low'] = low

# if diff < 0:
#     # print('index', index)
#     print('diff', diff)
#     # df.loc[index, 'buying'] = 'no way'
#     df['buying'] = 'no way'
# else:
#     # print('index', index)
#     print('diff', diff)
#     # df.loc[index, 'buying'] = 'all in'
#     df['buying'] = 'all in'

df.to_excel('candidate2_update.xlsx')
# p = monitor_price('042670')
# table = p[0]

# value fetched from network

# for index, row in df.iterrows():
#     diff = float(row['diff'])
#     sh = row['shcode']


    # if diff < 0:
    #     print('index', index)
    #     print('diff', diff)
    #     df.loc[index, 'buying'] = 'cheap'
    # else:
    #     print('index', index)
    #     print('diff', diff)
    #     df.loc[index, 'buying'] = 'expensive'

# print('df', df[0])

# df.to_excel("candidate20.xlsx")






