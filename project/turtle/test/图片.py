from PIL import Image, ImageSequence
import cv2
import numpy
 
pic_name = ")1VVKP_V3O[A(_RM_ZAUIYG.gif"
im = Image.open(pic_name)
while 1:
    for frame in ImageSequence.Iterator(im):    #使用迭代器
        frame = frame.convert('RGB')
        cv2_frame = numpy.array(frame)
        show_frame = cv2.cvtColor(cv2_frame, cv2.COLOR_RGB2BGR)
        cv2.imshow(pic_name, show_frame)
        cv2.waitKey(100)
