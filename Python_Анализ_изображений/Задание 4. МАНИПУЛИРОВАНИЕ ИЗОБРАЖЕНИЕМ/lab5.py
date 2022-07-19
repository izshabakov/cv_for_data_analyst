from PIL import Image
# # Задание 1. 
# # Открываем файл:
# img = Image.open("flowers.jpg")
# # Создаем копию:
# img2 = img.copy()
# # Просматриваем копию:
# img2.show()

# img=Image.open("flowers.jpg")
# print(img.size) # Исходные размеры изображения
# img.thumbnail((400, 300), Image.BILINEAR)
# print(img.size) # Изменяется само изображение
# img = Image.open("flowers.jpg")
# img.thumbnail((400, 100), Image.BILINEAR)
# print(img.size) # Вывод размера изображения

# #Создайте версию изображения указанного размера
# img = Image.open("flowers.jpg")
# print(img.size) # Исходные размеры изображения
# img.show()
# newsize = (400, 400)
# imgnr = img.resize(newsize)
# imgnr.show()# Изменяется само изображение

# # Вырежьте прямоугольный фрагмент из исходного изображения.
# # Задание 2. Вырезка куска изображения и изменение его размеров
# img = Image.open("flowers.jpg")
# img2 = img.crop([0, 0, 100, 100]) # помечаем фрагмент
# img2.load() # Считываем фрагмент
# print(img2.size)
# # Измените размеры куска изображения
# img = Image.open("flowers.jpg")
# print(img.size) # вывод размеров изображения
# img.show()
# box = (100,100,300,300)#берем кусок изображения:
# img2 = img.crop(box)
# newsize = (400, 400)
# img2nr = img2.resize(newsize)
# img2nr.show() # Изменяется само изображение

# Задание 3. 
img = Image.open("flowers.jpg")
img.size # Исходные размеры изображения
img2 = img.rotate(90)# Поворот на 90 градусов
print(img2.size)
img3 = img.rotate(45, Image.NEAREST)
print(img3.size) # Размеры сохранены, изображение обрезано
img4 = img.rotate(45, expand=True)
print(img4.size) # Размеры увеличены, изображение полное
# Получение горизонтального и зеркального образа изображения:
img2 = img.transpose(Image.FLIP_LEFT_RIGHT)
img2.show() # горизонтальный зеркальный образ
img3 = img.transpose(Image.FLIP_TOP_BOTTOM)
img3.show() # Вертикальный зеркальный образ
img4 = img.transpose(Image.ROTATE_90)
img4.show() # Поворот на 90 против часовой стрелки
img5 = img.transpose(Image.ROTATE_180)
img5.show() # Поворот на 180
