# в скобках передаем три аргумента:
#путь к файлу
# режим открытия : r - чтение, w - полная перезапись(удалит существующие данные), a - добавление новой информации
# encoding(кодировка текста) = utf-8 
with open(f'{эта_папка}\\last_msg', 'w', encoding='utf-8') as file: # после as идет название временной переменной 
    file.write("текст") 

    текст_файла = file.read()  # чтение из файла 