# from PIL import Image

# img = Image.open("flowers.jpg")
# print(img.mode)
# img2 = img.convert("RGBA")
# print(img2.mode)
# img2.show()

# from PIL import Image

# img = Image.open("flowers.jpg")
# print(img.mode)
# img2 = img.convert("RGBA")
# print(img2.mode)
# img2.show()
# pil_im = Image.open('flowers.jpg').convert('L')

# from PIL import Image

# img = Image.open("flowers.jpg")
# print(img.mode)
# img2 = img.convert("P", None, Image.FLOYDSTEINBERG, Image.ADAPTIVE, 128)
# print(img2.mode)

# from PIL import Image
# img = Image.open("flowers.jpg")
# img.save("flowers.jpg")
# img.save("flowers.bmp", "BMP")
# f = open("flowers.bmp", "wb")
# img.save(f, "BMP")
# f.close()

from PIL import Image

img = Image.new("RGB", (100, 100)) 
img.show() # Черный квадрат
img = Image.new("RGB", (100, 100), (255, 0, 0)) 
img.show() # Красный квадрат
img = Image.new("RGB", (100, 100), "green") 
img.show() # Зеленый квадрат
img = Image.new("RGB", (100, 100), "#f00")
img.show() # тоже красный квадрат
img = Image.new("RGB", (100, 100), "white")
img.show() # Белый квадрат
img = Image.new("RGB", (320, 240), "silver") 
img.show() # Серый квадрат
img = Image.new("RGB", (320, 240), "rgb(205, 100,200)") 
img.show() # цветной прямоугольник
img = Image.new("RGB", (320, 240), "rgb(10%, 100%,40%)")
img.show() # цветной прямоугольник. Каналы в процентах

img = Image.new("RGB", (640, 480), "rgb(205, 100,200)")
img.show() # сиреневый прямоугольник
for x in range(640):
    for y in range(480):
        img.putpixel((x,y),(0,160,0))
img.save("okno.png", "PNG")
img.show() # зеленый прямоугольник
img = Image.new("RGB", (640, 480), "rgb(205,100,200)")
img.show() # сиреневый прямоугольник
for x in range(640):
    for y in range(480):
        img.putpixel((x,y),(x//3,(x+y)//6,y//3))
img.save("okno.png", "PNG")
img.show()