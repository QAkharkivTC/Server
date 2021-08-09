import csv

def get_random_name_surname(random_number, path):
    if path == 'name':
        row_num = 0
    elif path == 'surname':
        row_num = 1
    else:
        row_num = 0
        
    with open("test_name_1.csv", encoding='cp1251') as r_file:
        file_reader = csv.reader(r_file, delimiter = ";")   # Создаем объект reader, указываем символ-разделитель ","
        count = 0                                           # Счетчик для подсчета количества строк и вывода заголовков столбцов

        #if random_number > file_reader.line_num:
         #   random_number = file_reader.line_num

        for row in file_reader:
            if count == 0:
                pass
            elif count == random_number:
                print(row[row_num])
            else:
                pass
            count += 1
        


get_random_name_surname(0, 'surname')    
get_random_name_surname(3, 'name')
get_random_name_surname(300, 'surname')
get_random_name_surname(30, 'surname')
