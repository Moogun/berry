from pyxing.session import *
from pyxing.query import *
import pandas as pd

# Login
xasession = XASession()
xasession.login(id="Taketheg", password="bwii1145", cert="Bwiisi07@3", block=True)

xaquery = XAQuery()

# buy strength pnt = "137400"
# dfs = xaquery.block_request("t1475", shcode=pnt, vptype="0",
#                             datacnt=500,
#                             date="", # outblock date for next batch of data
#                             time="", #outblock date for next batch of data
#                             )
# print('buy_strength', dfs)
# df = dfs[1]
# df.to_excel("buy_strength.xlsx")

# buy volume spike compared to the same time yesterday
# dfs = xaquery.block_request("t1475", shcode=pnt, vptype="0",
#                             datacnt=500,
#                             date="", # outblock date for next batch of data
#                             time="", #outblock date for next batch of data
#                             )

# min/tick
# pnt = "137400"
# dfs = xaquery.block_request("t1310",
#                             daygb="0", # 0 today, 1 yesterday
#                             timegb="0", # 0 tick, 1 min
#                             shcode=pnt,
#                             )

print(dfs)