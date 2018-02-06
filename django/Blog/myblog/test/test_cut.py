from PIL import Image
import os
# http://www.jb51.net/article/116789.htm

def cut_img(img):
    img_size = img.size
    print("图片宽度和高度分别是{}".format(img_size))
    x = 125
    y = 499
    w = 593
    h = 858
    box = (x, y , w,  h)
    region = img.crop(box)
    region.save("bb.png")

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)
    path = os.path.join(r'D:\linyouwei\python\pycharm\django\Blog\media\upload\1234.png').replace('\\', '/')
    img = Image.open(path)
    cut_img(img)