from pyxing.session import *
from pyxing.query import *

# Login
xasession = XASession()
xasession.login(id="Taketheg", password="bwii1145", cert="Bwiisi07@3", block=True)

print("서버이름: ", xasession.get_server_name())
print("연결상태: ", xasession.is_connected())
print("계좌    : ", xasession.get_account_list(0))

# block request 메서드로 요청하기 (blocking 방식)
# dfs = xaquery.block_request("t8430", gubun=0)
# print(dfs[0])

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

def e_search():
    dfs = xaquery.block_request("t1857",
                                sRealFlag="1", # 0: 조회, 1: 실시간
                                sSearchFlag="S",# F: file, S: Server
                                query_index="Taketheg00",)
    print('dfs', dfs)

e_search()

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