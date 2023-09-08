from PIL import Image, ImageFilter

try:
    orig = Image.open('Image_1.bmp')
except FileNotFoundError:
    print('be')

# blur = orig.filter(ImageFilter.BLUR)
# boxblur = orig.filter(ImageFilter.BoxBlur(34))
# gaussblur = orig.filter(ImageFilter.GaussianBlur(21))
# blur.save('py_bl.bmp')
# boxblur.save('py_blb.bmp')
# gaussblur.save('py_blg.bmp')

# cropped = orig.crop((0, 0, 1440 // 2, 900 // 2))
# cropped.save('cr.bmp')

# contour = orig.filter(ImageFilter.CONTOUR)
# contour.save('cou.bmp')

# pixs = orig.load()
# w, h = orig.size
#
# for x in range(w):
#     for y in range(h):
#         r, g, b = pixs[x, y]
#         pixs[x, y] = g, b, r
# orig.save('invert.bmp')

w, h = orig.size
resize = orig.resize((w // 2, h // 2))
resize.save('resize.bmp')

print('params img:')
print('format:', orig.format)
print('size:', orig.size)
print('color\'s shem:', orig.mode)
