import colorgram
import random
from turtle import Turtle, Screen, colormode

TOTAL_COLORS = 30
POSICAO_INICIAL = -360

#colors = colorgram.extract('dotImage.jpg', TOTAL_COLORS)

#list_of_colors = []

#for n in range(TOTAL_COLORS):
#    color = colors[n]
#    rgb = color.rgb
#    r = rgb.r
#    g = rgb.g
#    b = rgb.b
#    cor = (r, g, b)
#    list_of_colors.append(cor)

#for _ in range(4):
#    del list_of_colors[0]

#print(list_of_colors)
color_list = [(142, 77, 52), (188, 165, 118), (165, 152, 38), (16, 46, 83), (46, 110, 135), (144, 57, 83), 
              (61, 120, 100), (143, 184, 174), (141, 170, 176), (86, 36, 30), (65, 152, 168), (219, 209, 96),
              (109, 38, 32), (102, 145, 110), (166, 98, 130), (95, 122, 169), (161, 140, 160), (176, 104, 84),
              (52, 52, 87), (206, 182, 195), (67, 47, 63), (75, 51, 67), (174, 200, 193), (171, 200, 203), 
              (217, 180, 172), (182, 191, 206)]

tim = Turtle()
colormode(255)
tim.speed("fastest")
tim.hideturtle()

posicao_inicial = -360

for _ in range(10):
    tim.penup()
    tim.setposition(POSICAO_INICIAL, posicao_inicial)
    tim.pendown()

    for _ in range(10):
        ball_color = random.choice(color_list)
        #tim.color(ball_color)
        #tim.begin_fill()
        #tim.circle(20)
        #tim.end_fill()
        # Duas formas diferentes de fazer
        tim.dot(20, ball_color)
        tim.penup()
        tim.forward(50)
        tim.pendown()

    posicao_inicial += 50

screen = Screen()
screen.exitonclick()