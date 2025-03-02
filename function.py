from PIL import Image, ImageDraw, ImageFont
import textwrap
import os


nameFont = ImageFont.truetype(r"C:\Users\KULIK\AppData\Local\Microsoft\Windows\Fonts\RobotoMedium.ttf", 95)
workFont = ImageFont.truetype(r"C:\Users\KULIK\AppData\Local\Microsoft\Windows\Fonts\RobotoLightItalic.ttf", 50)

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

def text_in_pic (img_draw, list, part, start, fill, font, left_margin, indent, width, plus):
    for person in list:
        text_line = person.split('!')[part]
        if part==0:
            paragraphs = name_length(text_line, width)
        else:
            paragraphs = post_length(text_line)
        no = 0
        for line in paragraphs:
            wf = start + no
            img_draw.text((left_margin, wf), line, fill=fill, font=font)
            no += plus
        start += indent

def make_HB_pic(img_draw, list, start_name, left_margin, fill_name, indent, start_post, fill_post, width):
    text_in_pic(img_draw, list, 0, start_name, fill_name, nameFont, left_margin, indent, width, 100)
    text_in_pic(img_draw, list, 1, start_post, fill_post, workFont, left_margin, indent, width, 60)


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