from PIL import Image
import os
BASE_DIR  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(BASE_DIR,'test/aa.jpg').replace('\\', '/')
im = Image.open(path)
w, h = im.size
print('Original image size: %sx%s' % (w, h))
im.thumbnail((w//10, h//10))
im.save('thumbnail.jpg', 'jpeg')


