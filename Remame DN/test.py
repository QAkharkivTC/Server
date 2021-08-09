import csv
with open("test_name_1.csv", encoding='cp1251') as r_file:
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(r_file, delimiter = ";")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    count = 0
    # Считывание данных из CSV файла
    print(file_reader.line_num)
    for row in file_reader:
        if count == 0:
            # Вывод строки, содержащей заголовки для столбцов
            print(f'Файл содержит столбцы: {", ".join(row)}')
        else:
            # Вывод строк
            print(f'    {row[0]}  {row[1]} и он родился в .')
            print(row)
            #pass
        count += 1
    print(f'Всего в файле {count} строк.')
    #print(file_reader.__next__())
    print(file_reader.line_num)
    print(file_reader.dialect)
    #print(file_reader.fieldnames)
    print(file_reader.line_num)
    print(file_reader.line_num)
    print(file_reader.line_num)
    print(file_reader.line_num)
    #print(file_reader.__next__())
    
