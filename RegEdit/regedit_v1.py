import winreg


Path_web = 'SOFTWARE\\TrueConf\\Server\\WebManager'

def off_zopim():
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, Path_web, 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(key, 'zopim_url', None, winreg.REG_SZ, " ")
    winreg.CloseKey(key)
    

def add_web_logs():
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, Path_web, 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(key, 'log_level', None, winreg.REG_SZ, "debug")
    winreg.SetValueEx(key, 'debug', None, winreg.REG_SZ, "1")
    winreg.CloseKey(key)


add_web_logs()  #включить подробное логирование веб
off_zopim()     #отключить чат-поддержки на страницах конфигуратора
