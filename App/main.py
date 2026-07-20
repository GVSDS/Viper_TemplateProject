import w32.win32console as w32cmd
import t, c


pagecode: t.CDefine = 65001

@t.CExport
def main() -> int:
    w32cmd.SetConsoleOutputCP(pagecode)
    w32cmd.SetConsoleCP(pagecode)
    print("你好，世界")
    return 0
