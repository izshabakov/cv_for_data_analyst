import PIL
from PIL import Image
from pylab import *
# # Задание 1
# # 1. Закрасьте область изображения красным цветом.
# img = Image.open("flowers.jpg")
# img.paste( (255, 0, 0), (0, 0, 100, 100) )
# img.show()
# # 2. Залейте все изображение зеленым цветом.
# img = Image.open("flowers.jpg")
# img.paste( (0, 128, 0), img.getbbox() )
# img.show()

# # Задание 2. 
# # 1. Загрузите изображение, создайте его уменьшенную, а затем вставьте ее в исходное изображение, причем вокруг вставленного изображения отобразите рамку красного цвета.
# img = Image.open("flowers.jpg")
# img2 = img.resize((200, 150)) # Создаём миниатюру
# print(img2.size)
# img.paste((255, 0, 0), (9, 9, 211, 161)) # Рамка
# img.paste(img2, (10, 10)) # Вставляем миниатюру
# img.show()
# # 2. Выведите белую полупрозрачную горизонтальную полосу высотой 100 пикселов.
# img = Image.open("flowers.jpg")
# white = Image.new("RGB", (img.size[0], 100), (255, 255, 255))
# mask = Image.new("L", (img.size[0], 100), 64) #Маска
# img.paste(white, (0, 0), mask)
# img.show()
# # 3. Копируйте и вставьте повернутую часть изображения:
# img = Image.open("flowers.jpg")
# box = (100, 100, 400, 400)
# region = img.crop(box)
# region = region.transpose(Image.ROTATE_180)
# img.paste(region, box)
# img.show()

# # Задание 3. 
# im = array(Image.open("flowers.jpg"))
# imshow(im)
# print("Please click 3 points")
# x = ginput(3)
# print('you clicked:', x)

# Задание 4. Рисование на изображении
# запишем файл-изображение в массив
im = array(Image.open("flowers.jpg"))
imshow(im)
x = [100, 100, 400, 400]
y = [200, 500, 200, 500]
plot(x, y, 'r*')
plot(x[:2], y[:2])
title('Plotting: "flowers.jpg"')
axis('off') # убрать оси
plot(x, y) # синяя линия с круглыми маркерами
plot(x, y, 'go-') #зеленая линия с круглыми маркерами
plot(x, y, 'ks:') # черная пунктирная линия с квадратными маркерами
show()

