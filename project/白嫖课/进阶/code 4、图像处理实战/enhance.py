from PIL import Image
from PIL import ImageEnhance

im = Image.open("img1.jpg")

# 调整图像对比度
om = ImageEnhance.Contrast(im) 
# 图像对比度增强3倍    
om.enhance(3).save('img1_EnContrast.jpg')
