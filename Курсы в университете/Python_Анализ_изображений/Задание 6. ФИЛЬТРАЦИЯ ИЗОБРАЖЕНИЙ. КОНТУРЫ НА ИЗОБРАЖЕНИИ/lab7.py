from PIL import ImageFilter
from PIL import Image
from pylab import *
# #Задание 1.
# img = Image.open("flowers.jpg")
# img2 = img.filter(ImageFilter.BLUR)
# img2.show()
# img3 = img.filter(ImageFilter.CONTOUR)
# img3.show()
# img4 = img.filter(ImageFilter.DETAIL)
# img4.show()
# img5 = img.filter(ImageFilter.EDGE_ENHANCE)
# img5.show()
# img6 = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
# img6.show()
# img7 = img.filter(ImageFilter.EMBOSS)
# img7.show().......................................................................................................
# img8 = img.filter(ImageFilter.FIND_EDGES)
# img8.show()
# img9 = img.filter(ImageFilter.SHARPEN)
# img9.show()
# img10 = img.filter(ImageFilter.SMOOTH)
# img10.show()
# img11 = img.filter(ImageFilter.SMOOTH_MORE)
# img11.show()

# Задание 2.
im = array(Image.open('flowers.jpg').convert('L'))
figure()
gray()
contour(im, origin='image')
axis('equal')
axis('off')
im.show()