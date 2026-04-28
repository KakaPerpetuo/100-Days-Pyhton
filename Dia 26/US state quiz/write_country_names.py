from turtle import Turtle

class Country_names(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
    
    def write_country(self, x, y, country):
        self.goto(x, y)
        self.write(arg= country, move= False, align= "center", font= ("Arial", 10, "normal"))


