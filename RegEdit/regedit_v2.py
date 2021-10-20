import winreg


Path_web = 'SOFTWARE\\TrueConf\\Server\\WebManager'
Path_config = 'SOFTWARE\\TrueConf\\Server\\Configuration'

def off_zopim():
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, Path_web, 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(key, 'zopim_url', None, winreg.REG_SZ, " ")
    winreg.CloseKey(key)
    

def add_web_logs():
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, Path_web, 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(key, 'log_level', None, winreg.REG_SZ, "debug")
    winreg.SetValueEx(key, 'debug', None, winreg.REG_SZ, "1")
    winreg.CloseKey(key)

def smtp():
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, Path_config, 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(key, 'SMTP Admin Email', None, winreg.REG_SZ, "apukhtin+121@trueconf.ru")
    winreg.SetValueEx(key, 'SMTP Authentication Type', None, winreg.REG_DWORD, 1)
    winreg.SetValueEx(key, 'SMTP Login', None, winreg.REG_SZ, "apukhtin")
    winreg.SetValueEx(key, 'SMTP Password', None, winreg.REG_SZ, "v2*1631271188*iiUySUteqtY+LuFWMVABtw==")
    winreg.SetValueEx(key, 'SMTP Port', None, winreg.REG_DWORD, 465)
    winreg.SetValueEx(key, 'SMTP Sender Email', None, winreg.REG_SZ, "apukhtin+12@trueconf.ru")
    winreg.SetValueEx(key, 'SMTP Sender Name', None, winreg.REG_SZ, "SAA")
    winreg.SetValueEx(key, 'SMTP Server', None, winreg.REG_SZ, "mail.trueconf.com")
    winreg.SetValueEx(key, 'SMTP Use SSL', None, winreg.REG_DWORD, 1)
    winreg.CloseKey(key)

def meeting_room():
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, Path_config, 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(key, 'Meeting Room Filter', None, winreg.REG_SZ, "(msDS-PhoneticLastName=ResourceType:Room)")
    winreg.SetValueEx(key, 'Meeting Room Search Filter Attr', None, winreg.REG_SZ, "displayName")
    winreg.SetValueEx(key, 'Meeting Room BaseDN', None, winreg.REG_SZ, "DC=trust1,DC=loc")
    winreg.CloseKey(key)

def debug():
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, Path_config, 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(key, 'Debug Level', None, winreg.REG_DWORD, 4)
    winreg.SetValueEx(key, 'Debug Modules', None, winreg.REG_SZ, "4294967295")
    winreg.SetValueEx(key, 'Debug Transcoders', None, winreg.REG_DWORD, 1)
    winreg.CloseKey(key)

    

add_web_logs()  #включить подробное логирование веб
#off_zopim()     #отключить чат-поддержки на страницах конфигуратора
smtp()          #включить smtp - (apukhtin)
#debug()         #включение подробного логирования
meeting_room()  #включить комнаты встреч для ldap
