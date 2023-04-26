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
                                OrdprcPtnCode="00",
                                # 00 지정가
                                # 03 시장가
                                # 81 시간외종가 82 시간외 단일가
                                MgntrnCode="000",
                                LoanDt="",
                                OrdCndiTpCode="0")
    print('dfs from order', dfs)

# handle_order()
def check_stocks_holding():
    dfs = xaquery.block_request("t0424", accno="20658614901", passwd="1145")
    print('check_stocks_holding', dfs)

# hold list of candidates
candidate = []
liveDataKey = ''

def e_search():
    dfs = xaquery.block_request("t1857",
                                sRealFlag="1", # 0: 조회, 1: 실시간
                                sSearchFlag="S",# F: file, S: Server
                                query_index="Taketheg0002",)
                                # query_index="C:\\Users\\moogun\\tech\\230413_xing\che1.2x vol400 volup1.5x.ACF"

    global candidate
    global liveDataKey
    # print('e_search dfs - ', dfs)
    # dfs is a tuple, ( [block 2], cts_time )

    if len(dfs[0]) == 0:
        print('No Outblock')
        return
    else:
        # oBlock_1 = pd.DataFrame(dfs[0])
        print('dfs[0]', dfs[0])

        # print('oBlock_1 - list', type(oBlock_1))
        # liveDataKey = oBlock_1[0][2]

        # print('oBlock_1 - df', oBlock_1.loc[0]['AlertNum'] )

        # pd.DataFrame(oBlock_1).loc[0]['AlertNum']
        # print('liveDataKey', liveDataKey)

        oBlock_2 = pd.DataFrame(dfs[0])
        oBlock_2.to_excel("candidate1.xlsx")

e_search()


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

if __name__ == "__main__":
    # 로그인 정보
    f = open("../account.txt", "rt")
    lines = f.readlines()
    id = lines[0].strip()
    password = lines[1].strip()
    cert = lines[2].strip()
    f.close()

    # 로그인
    from pyxing import session

    # Session
    xasession = session.XASession()
    xasession.login(id, password, cert, block=True)
