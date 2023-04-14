from PyQt5.QtWidgets import *
import sys
import win32com.client


ID = "Taketheg"
PASSWD = "bwii1145"
CERT = "Bwiisi07@3"

# 이벤트 처리용 클래스
class XASessionEvents:
    def OnLogin(self, code, msg):
        if code == "0000":
            print("로그인 성공")
        else:
            print("로그인 실패 ", msg)


# XASession 클래스
class XASession:
    def __init__(self):
        self.session = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionEvents)
        self.session.ConnectServer("hts.ebestsec.co.kr", 20001)

    def login(self, id, passwd, cert):
        self.session.Login(id, passwd, cert, 0, False)


# 메인 윈도우
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.session = XASession()
        self.session.login(ID, PASSWD, CERT)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
