создаем тестовые файлы для проверки файлтрансфера в чате 

перечни расширений файлов указаны в файлах

конструкция:
#f = open(name,"wb")
#f.truncate(451824)
##f.write('\0')
#f.close()

используется для указания файлам определенного размера (оп дефолту не используется, но можно раскоментировать)