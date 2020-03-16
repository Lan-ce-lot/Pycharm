from PIL import Image
from PIL import ImageFilter

im = Image.open("img1.jpg")

om = im.filter(ImageFilter.BLUR) # 为图片使用模糊滤镜
om.save('img1_blur.jpg')
