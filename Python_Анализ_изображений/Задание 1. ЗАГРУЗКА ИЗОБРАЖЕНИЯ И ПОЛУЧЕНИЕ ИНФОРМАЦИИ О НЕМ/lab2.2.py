from PIL import Image
img= Image.open("flowers.jpg")
print('Размер фото: ',img.size)
print('Расширение фото: ',img.format)
print('Цветовая модель фото: ',img.mode)
print('Информация фото: ',img.info)
print('Координаты прямоугольной области: ',img.getbbox())