import win32com.client

instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
codeList = instCpCodeMgr.GetStockListByMarket(1)


def get_kospi():
    kospi = {}
    for code in codeList:
        name = instCpCodeMgr.CodeToName(code)
        kospi[code] = name
    return kospi
