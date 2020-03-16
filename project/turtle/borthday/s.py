
# # Layer Cake Challenge - www.101computing.net/layer-cake/
# from turtle import *
# from shapes import *
# from PIL import Image, ImageSequence
# import cv2
# import numpy
# myPen = Turtle()
# myPen.shape("turtle")
# myPen.speed(10)
# myPen.hideturtle()
# window = turtle.Screen()
# window.bgcolor("#69D9FF")
# y = -140

# #Inititalise the dictionary

# ingredients = {}
# #Add items to the dictionary
# ingredients["strawberry"]="pink"
# ingredients["milk chocolate"]="#BF671F"
# ingredients["matcha"]="#93c572"
# ingredients["icing sugar"]="#FFFFFF"

# ### Now let's preview the layer cake

# #let's draw the plate
# draw_rectangle(turtle, "white", -150, y-10, +300, 10)

# #Iterate through each layer of the list
# draw_rectangle(myPen, ingredients["milk chocolate"], -120, y, 240, 30)
# y+=30
# draw_rectangle(myPen, ingredients["strawberry"], -120, y, 240, 35)
# y+=35
# addIcing(myPen, ingredients["icing sugar"],120,y)
# y+=10
# draw_rectangle(myPen, ingredients["milk chocolate"], -100, y, 200, 20)
# y+=20
# draw_rectangle(myPen, ingredients["strawberry"], -100, y, 200, 40)
# y+=40
# addIcing(myPen, ingredients["icing sugar"],100,y)
# y+=10
# draw_rectangle(myPen, ingredients["milk chocolate"], -70, y, 140, 24)
# y+=24
# draw_rectangle(myPen, ingredients["strawberry"], -70, y, 140, 36)
# y+=36
# addIcing(myPen, ingredients["icing sugar"],70,y)
# y+=10
# draw_rectangle(myPen, ingredients["matcha"], -4, y, 8, 60)
# y+=65
# draw_star(myPen, "white", 2, y, 10)

# turtle.penup()
# turtle.goto(-110, 180)
# turtle.pendown()
# turtle.color("blue")
# turtle.write("小刘，生日快乐！",  font = ("Times", 18,"bold"))


# pic_name = ")1VVKP_V3O[A(_RM_ZAUIYG.gif"
# im = Image.open(pic_name)
# while 1:
#     for frame in ImageSequence.Iterator(im):    #使用迭代器
#         frame = frame.convert('RGB')
#         cv2_frame = numpy.array(frame)
#         show_frame = cv2.cvtColor(cv2_frame, cv2.COLOR_RGB2BGR)
#         cv2.imshow(pic_name, show_frame)
#         cv2.waitKey(100)
# turtle.end_fill()

# turtle.hideturtle()

# turtle.done()

def check(board, row, col):
    i = 0
         while i < row:
                 if abs(col-board[i]) in (0, abs(row-i)):
                         return False
                i += 1
         return True


def EightQueen(board, row):
        blen = len(board)
        if row == blen:
                    # 来到不存在的第九行了
                 print (board)
                 return True
        col = 0
         while col < blen:
                 if check(board, row, col):
                        board[row] = col
                        if EightQueen(board, row+1):
                                 return True
                col += 1
         return False


def printBoard(board):
        '''为了更友好地展示结果 方便观察'''
         import sys
        for i, col in enumerate(board):
                sys.stdout.write('□ ' * col + '■ ' + '□ ' * (len(board) - 1 - col))
                 print ('')
b = [0] * 10
EightQueen(b, 0)
printBoard(b)
