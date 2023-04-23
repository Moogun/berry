from pyxing.session import *
from pyxing.query import *
import pandas as pd
from typing import Tuple

# Login
xasession = XASession()
xasession.login(id="Taketheg", password="bwii1145", cert="Bwiisi07@3", block=True)

# TR 요청
xaquery = XAQuery()
outblock_sts_time =""

pnt = "137400"
hansolar ="009830"


def handle_status() -> None:
    print("You pressed s for 'status'")
    value = input("enter a company code to see the status:\n")
    df, cts_time_received = xaquery.block_request("t1301", shcode=value, cts_time=None)
    print(df)
    print('cts_time_received ---------->', cts_time_received)

def handle_code() -> None:
    print("You pressed 'handle_code'")

def handle_order() -> None:
    print("You pressed b for 'handle_order'")
    # AcntNo=String, InptPwd=String, IsuNo=String, OrdQty=long, OrdPrc=double, BnsTpCode=String,
    # 계좌,          비번,           ,종목        , 수량        ,주문가,      , 매도 1 /매수 2,
    account = "20658614901"
    test_account = "55501643701"
    pw = "1145"
    company = "011930" # string
    qty = 1 # quantity, long
    price = 2300 # order price, double
    buy =   "2"
    sell = "1"
    kindOfOrder = "00" # 00
    MgntrnCode = "000" #
    LoanDt = "0" #
    OrdCndiTpCode = "0" #

    df = xaquery.block_request(
        "CSPAT00600",
        AcntNo=test_account,
        InptPwd=pw,
        IsuNo=company,
        OrdQty=qty,
        OrdPrc=price,
        BnsTpCode=buy,
        OrdprcPtnCode=kindOfOrder, # 0, 1, 2 (x, 모의투자x)
            # 00 (o)
            # 000 (o)
        MgntrnCode=MgntrnCode,
            # 0,1,2, 00, 001, 002(x, 모의투자x)
            # 000 (o)
        LoanDt=LoanDt,
            # any number works
            #
        OrdCndiTpCode=OrdCndiTpCode)
            # any number works
            #
    print('df for order', df)


cts = None
shcode = None

def handle_transaction_made() -> None:
    company_code = input("enter a company code to see the transaction_made:\n")
    getData(company_input=company_code)

def getData(company_input, cts_input=None):
    global cts 
    global shcode

    if cts_input == None:
        df, cts_received1= xaquery.block_request("t1301", shcode=shcode)
        print(df)
        cts = cts_received1
        getMoreData()
    else:
        df, cts_received2= xaquery.block_request("t1301", shcode=shcode, cts_time=cts_input)
        print(df)
        cts = cts_received2
        getMoreData()

def getMoreData():
    while True:
        choice = input("Do you want to make the same request again? (y/n): ")
        if choice == "n":
            break
        elif choice == "y":
            getData(shcode='005930', cts_input=cts)
            print('3', cts)
            continue


def handle_invalid() -> None:
    print("Invalid input")

def handle_input(input_char: str) -> None:
    print("You pressed", input_char)
    match input_char:
        case 's':
            handle_status()
        case 'a':
            handle_code()
        case 't':
            handle_transaction_made()
        case 'b':
            handle_order()
        case 'q':
            print("You pressed 'q' to exit")
            xasession.disconnect_server()
        case _:
            handle_invalid()

while True:
    input_char = input("Press a key: ")
    handle_input(input_char)