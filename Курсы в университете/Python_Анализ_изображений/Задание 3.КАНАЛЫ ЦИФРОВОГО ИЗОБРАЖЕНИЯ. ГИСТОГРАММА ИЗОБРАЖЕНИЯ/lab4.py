from PIL import Image
import matplotlib.pyplot as plt
import cv2


# img = Image.open("flowers.jpg")

# for x in range(img.size[0]):
#     for y in range(img.size[1]):
#         r,g,b = img.getpixel((x,y))
#         img.putpixel((x,y),(b, r,g))
# img.show()

# img= Image.open("flowers.jpg")
# R,G,B= img.split()
# img2=Image.merge("RGB",(R,G,B))
# print(img2.mode)
# img2.show()

im = cv2.imread("flowers.jpg") 
a = plt.hist(im.ravel(), 256) 
plt.show()
