from PIL import Image, ImageDraw, ImageFont
import textwrap
import os


font_name = ImageFont.truetype(r"C:\Users\KULIK\AppData\Local\Microsoft\Windows\Fonts\RobotoMedium.ttf", 95)
font_post = ImageFont.truetype(r"C:\Users\KULIK\AppData\Local\Microsoft\Windows\Fonts\RobotoLightItalic.ttf", 50)

# make_image
def name_length (text, width):
    length = textwrap.wrap(text, width=width)
    return length
def post_length (text):
    length = textwrap.wrap(text, width=41)
    return length

def img_size(img):
    image = Image.open(img)
    size_img = image.size
    return image, size_img

def creat_pic(size, image):
    img = Image.new('RGB', size, 'white')
    img.paste(image)
    img_draw = ImageDraw.Draw(img)
    return img, img_draw

# def text_in_pic (img_draw, list, type_text, start, fill, font, left_margin, indent, width, plus):
#     for person in list:
#         text_line = person.split('!')[type_text]
#         if type_text==0:
#             paragraphs = name_length(text_line, width)
#         else:
#             paragraphs = post_length(text_line)
#         no = 0
#         for line in paragraphs:
#             wf = start + no
#             img_draw.text((left_margin, wf), line, fill=fill, font=font)
#             no += plus
#         start += indent

def text_in_pic (img_draw, list, type_text, class_img):
    for person in list:
        text_line = person.split('!')[type_text]
        if type_text == 'name':
            paragraphs = name_length(text_line, class_img.width)
            start = class_img.start_name
            fill = class_img.fill_name
            font = font_name
            plus = 100
        elif type_text == 'post':
            paragraphs = post_length(text_line)
            start = class_img.start_post
            fill = class_img.fill_post
            font = font_post
            plus = 60
        else:
            print('Error - type_text может принимать значение name или post')
            break
        no = 0
        for line in paragraphs:
            wf = start + no
            img_draw.text((class_img.left_margin, wf), line, fill=fill, font=font)
            no += plus
        start += class_img.indent

def make_HB_pic(img_draw, list, class_img):
    text_in_pic(img_draw, list, 'name', class_img)
    text_in_pic(img_draw, list, 'post', class_img)


# make_database
def birthday_information(row):
    birthday_date = row['Дата Рождения']
    day = birthday_date[0:2]
    fio = row['Сотрудник']
    post = row['Должность']
    employee_information = '!'.join([fio, post])
    return day, employee_information, fio

def add_in_list(day, employee_information, list):
    if day in list:
        list[day].append(employee_information)
    else:
        list[day] = [employee_information]

def delete_files_in_folder(folder):
    folder_path = (r'.\готово\{save}'.format(save=folder))
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f'Ошибка при удалении файла {file_path}. {e}')

#delete_files_in_folder('Начальники_Юбилей')