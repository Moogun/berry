import pandas as pd
import file1
from pyxing.session import *
from pyxing.query import *

# Login
xasession = XASession()
xasession.login(id=file1.id, password=file1.pwd, cert=file1.cert, block=True)
print("서버: ", xasession.get_server_name()," connected - ", xasession.is_connected()," accountList(0) - ", xasession.get_account_list(0))

# Query
xaquery = XAQuery()

def check_acnt():
    dfs = xaquery.block_request("CSPAQ22200", RecCnt=1, AcntNo="20658614901", Pwd="1145", BalCreTp="1")
    print('dfs', dfs)

def handle_order():
    dfs = xaquery.block_request("CSPAT00600",
                                AcntNo="20658614901",
                                InptPwd="1145",
                                IsuNo="137400",
                                OrdQty=1, # long
                                OrdPrc=51000, # double
                                BnsTpCode="2",
                                OrdprcPtnCode="82",
                                # 00 지정가
                                # 03 시장가
                                # 81 시간외종가 82 시간외 단일가
                                MgntrnCode="000",
                                LoanDt="",
                                OrdCndiTpCode="0")
    print('dfs', dfs)

handle_order()
def check_stocks_holding():
    dfs = xaquery.block_request("t0424", accno="20658614901", passwd="1145")
    print('dfs', dfs)

# hold list of candidates
candidate = []
liveDataKey = ''

def e_search():
    dfs = xaquery.block_request("t1857",
                                sRealFlag="1", # 0: 조회, 1: 실시간
                                sSearchFlag="S",# F: file, S: Server
                                query_index="Taketheg0001",)
    global candidate
    global liveDataKey
    candidate = dfs[0] # dfs is [df], cts_time (a tuple) df is a list
    # print('candidate[0] type ---------- ', type(candidate[0]), '- len(candidate) - ', len(candidate),  len(candidate[0]))
    liveDataKey = candidate.loc[0]['AlertNum']
    print('liveDataKey', liveDataKey)
    pd.DataFrame(candidate[1]).to_excel("candidate2.xlsx")

e_search()
print('candiate[0] ', candidate[0])
# print('candiate[0][shcode] ', candidate[0][0])
# print('candiate[0][shcode][AlertNum] ', candidate[0][0]['AlertNum'])

#
# def handle_input(input_char: str) -> None:
#     print("You pressed", input_char)
#     match input_char:
#         case 'a':
#             check_acnt()
#         case 'o':
#             handle_order()
#         case 'q':
#             print("You pressed 'q' ")
#         case _:
#             print("invalid input")
#
# while True:
#     input_char = input("Press a key: ")
#     handle_input(input_char)