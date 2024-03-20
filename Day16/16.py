#Day16 learning OOPs Concept in python

# a object has two things attributes, it is simply a variable holding some values and methods

from turtle import Turtle,Screen
from prettytable import PrettyTable
# timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('red','green')
# timmy.forward(150)
# # print(timmy)
# myScreen = Screen()
# # print(myScreen.canvheight)
# myScreen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon Name",['Pikachu','Squirtle','Charmandor'])
table.add_column("Type",['Electric','Water','Fire'])
table.align = 'l'
# table.sortby = "Pokemon Name"
table.reversesort = True
print(table)