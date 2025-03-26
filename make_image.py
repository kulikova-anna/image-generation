from make_database import congratulations_lists
import function
import input_data

excel_file = input_data.excel_file
Boss_ubiley, Boss_dr, Staff_ubiley = congratulations_lists(excel_file)

image1, size_img1 = function.img_size(input_data.img_one_person)
image2, size_img2 = function.img_size(input_data.img_two_person)
image3, size_img3 = function.img_size(input_data.img_three_person)
imageB, size_imgB = function.img_size(input_data.img_boss)
imageHB, size_imgHB = function.img_size(input_data.img_happy_boss)

image_parameters_staff = {
    'size': {1: size_img1, 2: size_img2, 3: size_img3}, #размер картинки
    'image': {1: image1, 2: image2, 3: image3}, #фон
    'left_margin': {1: 930, 2: 930, 3: 1210}, #отступ от левого края
    'start_name': {1: 540, 2: 500, 3: 400}, #отступ от верхнего края где начинается строка ФИО
    'indent': {1: 180, 2: 400, 3: 250}, #между строками
    'start_post': {1: 770, 2: 720, 3: 510}, #отступ от верхнего края где начинается строка должность
    'fill_name': {1: (0, 0, 0), 2: (0, 0, 0), 3: (255, 255, 255)}, #цвет текста ФИО
    'fill_post': {1: (7, 99, 155), 2: (7, 99, 155), 3: (255, 255, 255)}, #цвет текста должности
    'width': {1: 19, 2: 19, 3: 33} #размер шрифта
}

image_parameters_boss={
    'size': {'B': size_imgB, 'HB': size_imgHB},
    'image': {'B': imageB, 'HB': imageHB},
    'left_margin': {1: 1000, 2: 1000}, #отступ от левого края
    'start_name': {1: 580, 2: 540}, #отступ от верхнего края где начинается строка ФИО
    'indent': {1: 180, 2: 400}, #между строками
    'start_post': {1: 815, 2: 750}, #отступ от верхнего края где начинается строка должность
    'fill_name': {1: (0, 0, 0), 2: (0, 0, 0)}, #цвет текста ФИО
    'fill_post': {1: (7, 99, 155), 2: (7, 99, 155)}, #цвет текста должности
    'width': {1: 19, 2: 19} #размер шрифта
}

dict_list = {
    'B':{'data': Boss_dr, 'parameters': image_parameters_boss, 'dir_save':'Начальники'},
    'HB':{'data': Boss_ubiley, 'parameters': image_parameters_boss, 'dir_save':'Начальники_Юбилей'},
    'S':{'data': Staff_ubiley, 'parameters':image_parameters_staff, 'dir_save':'Сотрудники'}
}

def save_pic(list_abv):
    list = dict_list[list_abv]['data']
    dict_param = dict_list[list_abv]['parameters']
    dir_save = dict_list[list_abv]['dir_save']
    function.delete_files_in_folder(dir_save)
    for key in list:
        imgname = key
        quantity_staff = len(list[key])
        if quantity_staff >= 4:
            print(f'{imgname} - больше 3х человек')
        else:
            if list_abv=='S':
                key_params = quantity_staff
            else:
                key_params = list_abv
            size = dict_param['size'][key_params]
            image = dict_param['image'][key_params]
            left_margin = dict_param['left_margin'][quantity_staff]
            start_name = dict_param['start_name'][quantity_staff]
            indent = dict_param['indent'][quantity_staff]
            start_post = dict_param['start_post'][quantity_staff]
            fill_name = dict_param['fill_name'][quantity_staff]
            fill_post = dict_param['fill_post'][quantity_staff]
            width = dict_param['width'][quantity_staff]

            img, img_draw = function.creat_pic(size, image)

            function.make_HB_pic(img_draw, list[key], start_name, left_margin, fill_name, indent, start_post, fill_post, width)
            # img.show()
            img.save(r".\готово\{dir_save}\{imgname}.jpg".format(dir_save=dir_save, imgname=imgname))
            print(f'{imgname} - сохранено')

def all_save():
    save_pic('B')
    save_pic('HB')
    save_pic('S')

# save_pic('HB')

