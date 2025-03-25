from function import img_size
import input_data
class image_parameters:
    left_margin = 930  # отступ от левого края
    start_name =  540 # отступ от верхнего края где начинается строка ФИО
    indent = 180 # между строками
    start_post = 770 # отступ от верхнего края где начинается строка должность
    fill_name = (0, 0, 0) # цвет текста ФИО
    fill_post = (7, 99, 155) # цвет текста должности
    width = 19 # размер шрифта

class image_one_person (image_parameters):
    image, size_img = img_size(input_data.img_one_person)

class image_two_person (image_parameters):
    image, size_img = img_size(input_data.img_two_person)
    start_name = 500
    indent = 400
    start_post = 720

class image_three_person (image_parameters):
    image, size_img = img_size(input_data.img_three_person)
    left_margin = 1210
    start_name = 400
    indent = 250
    start_post = 510
    fill_name = (255, 255, 255)
    fill_post = (255, 255, 255)
    width = 33

class image_boss(image_parameters):
    left_margin = 1000

    def select_img(arg):
        if arg == 'B' :
            image, size_img = img_size(input_data.img_boss)
        elif arg == 'HB' :
            image, size_img = img_size(input_data.img_happy_boss)
        else:
            pass
        return image, size_img


class image_one_boss(image_boss):
    start_name = 580
    start_post = 815

class image_two_boss(image_boss):
    indent = 400
    start_post = 750



# image_parameters_staff = {
#     'size': {1: size_img1, 2: size_img2, 3: size_img3}, #размер картинки
#     'image': {1: image1, 2: image2, 3: image3}, #фон
#     'left_margin': {, }, #отступ от левого края
#     'start_name': {1: , 2: , 3: }, #отступ от верхнего края где начинается строка ФИО
#     'indent': {1: , 2: , 3: }, #между строками
#     'start_post': {1: 770, 2: 720, 3: 510}, #отступ от верхнего края где начинается строка должность
#     'fill_name': { }, #цвет текста ФИО
#     'fill_post': { }, #цвет текста должности
#     'width': { } #длина строки
# }
#
# image_parameters_boss={
#     'size': {'B': size_imgB, 'HB': size_imgHB},
#     'image': {'B': imageB, 'HB': imageHB},
#     'left_margin': {}, #отступ от левого края
#     'start_name': {1: , 2: }, #отступ от верхнего края где начинается строка ФИО
#     'indent': {1: , 2: }, #между строками
#     'start_post': {1: 815, 2: 750}, #отступ от верхнего края где начинается строка должность
#     'fill_name': {}, #цвет текста ФИО
#     'fill_post': {}, #цвет текста должности
#     'width': {} #длина строки
# }