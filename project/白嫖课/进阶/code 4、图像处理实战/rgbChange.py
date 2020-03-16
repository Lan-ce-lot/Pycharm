from PIL import Image

im = Image.open(img1.jpg')
r,g,b = im.split()   # 获得RGB通道数据
newr = g.point(lambda i: i*0.9
newg = g.point(lambda i: i<200)    # 选择g通道值低于200的像素点
newb = b.point(lambda i: i)
om = Image.merge(im.mode, (newr, newg, b))   # 将3个通道合成新图像
om.save('img1Merge.jpg')
