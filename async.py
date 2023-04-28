import asyncio
import time

async def count():
    print(0)
    await asyncio.sleep(2)
    print(1)

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    s = time.perf_counter()
    print('s - ', s)

    asyncio.run(main())
    elapsed = time.perf_counter() - s

    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
    # count()
    # main()

# import pandas as pd
#
# from pyxing.session import *
# from pyxing.query import *
#
# f = open("account.txt", "rt")
# lines = f.readlines()
# id = lines[0].strip()
# pwd = lines[1].strip()
# cert = lines[2].strip()
# f.close()
#
# # Login
# xasession = XASession()
# xasession.login(id=id, password=pwd, cert=cert, block=True)
# print("서버: ", xasession.get_server_name(), " connected - ", xasession.is_connected(), " accountList(0) - ",
#       xasession.get_account_list(0))
#
# xaquery = XAQuery()
# df = pd.DataFrame()
# async def monitor_price(shcode) -> pd.DataFrame:
#     loop = asyncio.get_running_loop()
#     t1102 = await loop.run_in_executor(None, xaquery.block_request, 't1101')
#     return t1102
#
# async def main():
#     # Create a list of symbols to monitor
#     symbols = ['042670', '137400', '316140', '000270']
#
#     # Create a list of tasks to run asynchronously
#     tasks = [monitor_price(symbol) for symbol in symbols]
#
#     # Wait for all tasks to complete
#     results = await asyncio.gather(*tasks)
#     print('results', results)
#
#     # Process the results
#     for table in results:
#         hname = table['hname']
#         newPrice = table['price']
#         open = table['open']
#         high = table['high']
#         low = table['low']
#         diff = table['diff']
#
#         df['new_price'] = newPrice
#         df['open'] = open
#         df['high'] = high
#         df['low'] = low
#
#         if diff < 0:
#             df['buying'] = 'no way'
#         else:
#             df['buying'] = 'all in'
#
#     # df.to_excel('candidate2_update.xlsx')
#     print('hname', hname, '----', df)
#
# # Run the main coroutine
# asyncio.run(main())