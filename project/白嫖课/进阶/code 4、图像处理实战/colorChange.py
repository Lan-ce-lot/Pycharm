from PIL import Image

im = Image.open('img1.jpg')
r,g,b = im.split()
om = Image.merge("RGB", (b, g, r))
om.save('img1BGR.jpg')
