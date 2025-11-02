import turtleplotlib as tpl
import matplotlib.pyplot as plt

def fractal_plant(turtle, depth, color):
    # Funksjon for å tegne fraktal plante, implementerer omskrivningsregler
    if depth == 0:
        turtle.color(color)
        turtle.forward(10)
    else:
        pass

#Hovedprogram
fig = plt.figure()
t = tpl.Turtle(fig, interactive=False)

depth = 3 #Starter med lav dybde for å teste. 

fractal_plant(t, depth, color='red') #Kaller på funksjonen.


plt.show()



