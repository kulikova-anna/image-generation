from PIL import Image, ImageDraw, ImageFont
import textwrap
import pandas as pd
import os.path

nameFont = ImageFont.truetype(r"C:\Users\KULIK\AppData\Local\Microsoft\Windows\Fonts\RobotoMedium.ttf", 95)
workFont = ImageFont.truetype(r"C:\Users\KULIK\AppData\Local\Microsoft\Windows\Fonts\RobotoLightItalic.ttf", 50)

image1 = Image.open(r'D:\Python\HappyBirthday\фоны\фон1.jpg')
image2 = Image.open(r'D:\Python\HappyBirthday\фоны\фон2.jpg')
image3 = Image.open(r'D:\Python\HappyBirthday\фоны\фон3.jpg')
imageN = Image.open(r'D:\Python\HappyBirthday\фоны\фонНачальник.jpg')
imageHB = Image.open(r'D:\Python\HappyBirthday\фоны\фонНачальникЮбилей.jpg')

sizeimg1 = image1.size
sizeimg2 = image2.size
sizeimg3 = image3.size
sizeimgN = imageN.size
sizeimgHB = imageHB.size

def abzname (text,width):
    a = textwrap.wrap(text, width=width)
    return a
def abztext (text):
    b = textwrap.wrap(text, width=41)
    return b
def add_in_list(spisok):
    if day in spisok:
        spisok[day].append(alldata)
    else:
        spisok[day] = [alldata]

def creat_pic(size, image):
    img = Image.new('RGB', size, 'white')
    img.paste(image)
    new = ImageDraw.Draw(img)
    return img, new

def make_HB_pic(spisok, starttext,leftabz,fill_text,str_plus,startline,fill_line,width=19):
    for i in spisok[key]:
        name = i.split('!')[0]
        lines1 = abzname(name,width)
        no = 0
        for f in range(len(lines1)):
            wf = starttext + no
            new.text((leftabz, wf), lines1[f], fill=fill_text, font=nameFont)
            no += 100
        starttext += str_plus
        text = i.split('!')[1]
        lines2 = abztext(text)
        n1 = 0
        for k in lines2:
            w = startline + n1
            new.text((leftabz, w), k, fill=fill_line, font=workFont)
            n1 += 60
        startline += str_plus

my_file = r'D:\Python\HappyBirthday\Именинники.xls'
HB = pd.read_excel(my_file)

HB = HB.drop(HB.index[[0,1, 2, 3, 4, 5, 6,7]])

HB.columns = ['Сотрудник', '2', '3', 'Должность', '5', '6', '7', '8', '9', '10', 'Возраст', '12','Дата Рождения', 'Юбилей']
HB = HB.drop(columns=['2', '3','5', '6', '7', '8', '9', '10', '12'])

BigBoss_List = ['Начальник', 'Ведущий', 'Зам','зам','Заведующий', 'Руководитель', 'Главный', 'Директор' ]
bos_index = []
n = 0
for h in HB['Должность']:
    n+=1
    for i in BigBoss_List:
        if h.find(i) == 0:
            #print(h)
            bos_index.append(n-1)

Boss_frame = HB.iloc[bos_index]
Birthday_people = HB.dropna(axis=0)

Boss_name = []
Boss_ubiley = {}
Boss_dr={}
Staff_ubiley = {}
for index, row in Boss_frame.iterrows():
    imgname = row['Дата Рождения']
    day = imgname[0:2]
    fio = row['Сотрудник']
    working = row['Должность']
    alldata = '!'.join([fio, working])
    #print(imgname, fio, working)
    if type(row['Юбилей'])==int:
        #print('Юбилей')
        Boss_name.append(fio)
        add_in_list(Boss_ubiley)
    else:
        add_in_list(Boss_dr)


for index, row in Birthday_people.iterrows():
    imgname = row['Дата Рождения']
    day = imgname[0:2]
    fio = row['Сотрудник']
    working = row['Должность']
    alldata = '!'.join([fio, working])
    if fio not in Boss_name:
        #print(imgname[0:2], fio, working)
        add_in_list(Staff_ubiley)

#print(Boss_ubiley)
#print(Boss_dr)
#print(Staff_ubiley)

for key in Staff_ubiley:
    imgname = key
    colvo = len(Staff_ubiley[key])
    if colvo >= 4:
        print(f'{imgname} - больше 3х человек')
    else:
        if colvo == 1:
            size = sizeimg1
            image = image1
            leftabz = 930
            starttext = 540
            str_plus = 180
            startline = 780
            fill_text = (0, 0, 0)
            fill_line = (7, 99, 155)
            width = 19
        elif colvo == 2:
            size = sizeimg2
            image = image2
            leftabz = 930
            starttext = 500
            str_plus = 400
            startline = 720
            fill_text = (0, 0, 0)
            fill_line = (7, 99, 155)
            width = 19
        elif colvo == 3:
            size = sizeimg3
            image = image3
            leftabz = 1210
            starttext = 400
            str_plus = 250
            startline = 510
            fill_text = (255, 255, 255)
            fill_line = (255, 255, 255)
            width=33
        img, new = creat_pic(size, image)
        make_HB_pic(Staff_ubiley, starttext,leftabz,fill_text,str_plus,startline,fill_line,width)
        img.save(r"D:\Python\HappyBirthday\готово\Сотрудники\{imgname}.jpg".format(imgname=imgname))
        print(f'{imgname} - сохранено')

for key in Boss_dr:
    imgname = key
    colvo = len(Boss_dr[key])
    size = sizeimgN
    image = imageN
    fill_text = (0, 0, 0)
    fill_line = (7, 99, 155)
    if colvo == 1:
        leftabz = 1000
        starttext = 580
        str_plus = 180
        startline = 815
    elif colvo == 2:
        leftabz = 1000
        starttext = 540
        str_plus = 400
        startline = 750
    img, new = creat_pic(size, image)
    make_HB_pic(Boss_dr, starttext,leftabz,fill_text,str_plus,startline,fill_line)
    img.save(r"D:\Python\HappyBirthday\готово\Начальники\{imgname}.jpg".format(imgname=imgname))
    print(f'{imgname} - сохранено')

for key in Boss_ubiley:
    imgname = key
    colvo = len(Boss_ubiley[key])
    size = sizeimgHB
    image = imageHB
    fill_text = (0, 0, 0)
    fill_line = (7, 99, 155)
    if colvo == 1:
        leftabz = 1000
        starttext = 580
        str_plus = 180
        startline = 815
    elif colvo == 2:
        leftabz = 1000
        starttext = 540
        str_plus = 400
        startline = 750
    img, new = creat_pic(size, image)
    make_HB_pic(Boss_ubiley, starttext,leftabz,fill_text,str_plus,startline,fill_line)
    img.save(r"D:\Python\HappyBirthday\готово\Начальники_Юбилей\{imgname}.jpg".format(imgname=imgname))
    print(f'{imgname} - сохранено')
