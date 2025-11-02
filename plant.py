import turtleplotlib as tpl
import matplotlib.pyplot as plt

#Hovedprogram
fig = plt.figure()
t = tpl.Turtle(fig, interactive=False)

def fractal_plant(turtle, depth, color):
    # Funksjon for å tegne fraktal plante, implementerer omskrivningsregler
    if depth == 0:
        turtle.color(color)
        turtle.forward(10)