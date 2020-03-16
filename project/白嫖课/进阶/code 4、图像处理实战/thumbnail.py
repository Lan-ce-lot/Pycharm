from PIL import Image

im = Image.open("img0.jpg")
im.thumbnail((128, 128))
im.save("img0TN.jpg", "JPEG")
