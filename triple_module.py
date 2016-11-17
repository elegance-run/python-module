from PIL import Image

im=Image.open('test.jpg')
print(im.format,im.size,im.mode)
im.thumbnail((1024,728))
im.save('thun.jpg','JPEG')