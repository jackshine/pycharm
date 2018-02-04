from PIL import Image
import os
BASE_DIR  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(BASE_DIR,'test/aa.jpg').replace('\\', '/')
im = Image.open(path)
w, h = im.size
print('Original image size: %sx%s' % (w, h))
im.thumbnail((w//10, h//10))
im.save('thumbnail.jpg', 'jpeg')
# http://www.jb51.net/article/116789.htm

def cut_img(img):
    img_size = img.size
    print("图片宽度和高度分别是{}".format(img_size))
    x = 100
    y = 250
    w = 250
    h = 250
    box = (x, y , x+w, y+h)
    region = img.crop(box)
    region.save("bb.jpg")

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)
    path = os.path.join(BASE_DIR, 'test/aa.jpg').replace('\\', '/')
    img = Image.open(path)
    cut_img(img)