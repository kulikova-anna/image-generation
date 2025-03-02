import pandas as pd
from function import birthday_information, add_in_list

def creating_database(excel_file):
    data_excel = excel_file
    database = pd.read_excel(data_excel)
    database.columns = ['Сотрудник', '2', '3', 'Должность', '5', '6', '7', '8', '9', '10', 'Возраст', '12','Дата Рождения', 'Юбилей']
    #удаляет лишние строки и столбцы
    database = database.drop(database.index[[0,1, 2, 3, 4, 5, 6,7]])
    database = database.drop(columns=['2', '3', '5', '6', '7', '8', '9', '10', '12'])
    return database

def find_boss(excel_file):
    database = creating_database(excel_file)
    boss_positions = ['Начальник', 'Ведущий', 'Зам', 'зам', 'Заведующий', 'Руководитель', 'Главный', 'Директор']
    bos_index = []
    n = 0
    for line in database['Должность']:
        n+=1
        for position in boss_positions:
            if line.find(position) == 0:
                bos_index.append(n-1)
    Boss_frame = database.iloc[bos_index] #фрейм, в котором только руководители
    Birthday_people = database.dropna(axis=0) #удаляем пустые строки
    return Boss_frame, Birthday_people

def congratulations_lists(excel_file):
    Boss_frame, Birthday_people = find_boss(excel_file)
    Boss_name = [] #начальники, у которых юбилей

    #итоговые списки, которые пойдут в работу
    Boss_ubiley = {} #начальники, у которых юбилей
    Boss_dr={} #начальники, у которых просто день рождения
    Staff_ubiley = {} #остальные работники, у которых юбилей

    for index, row in Boss_frame.iterrows():
        day, employee_information, fio = birthday_information(row)
        if type(row['Юбилей'])==int:
            Boss_name.append(fio)
            add_in_list(day, employee_information, Boss_ubiley)
        else:
            add_in_list(day, employee_information, Boss_dr)

    for index, row in Birthday_people.iterrows():
        day, employee_information, fio = birthday_information(row)
        if fio not in Boss_name:
            add_in_list(day, employee_information, Staff_ubiley)

    return Boss_ubiley, Boss_dr, Staff_ubiley

#Для наглядности как работает функция
#excel_file = r'D:\Python\HappyBirthday\Именинники.xls'
#Boss_ubiley, Boss_dr, Staff_ubiley = congratulations_lists(excel_file)
#print(Boss_ubiley)
#print(Boss_dr)
#print(Staff_ubiley)