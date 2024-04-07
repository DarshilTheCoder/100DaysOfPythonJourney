#Project Day18 hirst image creation
import turtle as t
import colorgram
import random as rd

tim_turtle = t.Turtle()
screen = t.Screen()
t.colormode(255)
colors_list = colorgram.extract('hirst.jpeg',10)
rgb_list = []
for color in colors_list:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_list.append(new_color)
print(rgb_list)
tim_turtle.speed('fastest')
tim_turtle.penup()
tim_turtle.hideturtle()
tim_turtle.setheading(225)
tim_turtle.forward(300)
tim_turtle.setheading(0)
nubmer_of_dots = 100
# for _ in range(10):
#     for _ in range(10):
#         tim_turtle.dot(20,rd.choice(rgb_list))
#         tim_turtle.penup()
#         tim_turtle.forward(50)
#         tim_turtle.pendown()
#     tim_turtle.penup()
#     tim_turtle.sety(counter)
#     counter+=50
#     tim_turtle.backward(500)
#     tim_turtle.setheading(0)  
for dot_counts in range(1,nubmer_of_dots+1):
    tim_turtle.dot(20,rd.choice(rgb_list))
    tim_turtle.forward(50)

    if dot_counts%10 ==0:
        tim_turtle.setheading(90)
        tim_turtle.forward(50)
        tim_turtle.setheading(180)
        tim_turtle.forward(500)
        tim_turtle.setheading(0)
screen.exitonclick()