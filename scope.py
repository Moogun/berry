
cts = None
shcode = None

def getData(shcode, cts_input=None):
    global cts
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

print('1', cts)
cts = getData()
print('2', cts)

def getMoreData():
    while True:
        choice = input("Do you want to make the same request again? (y/n): ")
        if choice == "n":
            break
        elif choice == "y":
            getData(shcode='005930', cts_input=cts)
            print('3', cts)
            continue


def handle_transaction_made() -> None:
    value = input("enter a company code to see the transaction_made:\n")
    getData(value)
#
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