from PIL import Image
import io
img = Image.open("smile.png")
img.show()
#Картинка в бинарном режиме
img = Image.open("smile.png")
img = img.convert("L")
img.show()
#Передача файлового объекта
f = open("smile.png", "rb") 
img = Image.open(f)
img.show()
f.close()
#Загрузка изображения из строки. Модуль io
f = open("smile.png", "rb")
i = f.read() 
f.close()
img = Image.open(io.BytesIO(i))
img.show()
