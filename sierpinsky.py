import turtleplotlib as tpl
import matplotlib.pyplot as plt  #importerer disse slik at hovedprogrammet virker med turtleplotlib og matplotlib. 


def dragon(turtle, depth):
    turtle.forward(10)             # F
    dragonX(turtle, depth-1)       # X
    
def dragonX(turtle, depth, color):
    if depth > 0:                  # X ->
        dragonX(turtle, depth-1, color)   #       X         
        turtle.left(90)            #         +
        dragonY(turtle, depth-1)   #           Y
        turtle.forward(10)         #             F
        turtle.color(color) #legger til denne linjen for å velge farger.
        
def dragonY(turtle, depth, color):
    if depth > 0:                  # Y ->
        turtle.forward(10)         #       F
        turtle.color(color)  #Legger til denne linjen for å kunne velge farger. 
        dragonX(turtle, depth-1, color)   #         X
        turtle.right(90)           #           -
        dragonY(turtle, depth-1, color)   #             Y

        #Kode over er hentet fra canvas, ihht instruksjoner i oppgaven. 

#Hovedprogram
fig = plt.figure()
t = tpl.Turtle(fig, interactive=False)

depth = 5
fargeA = "blue"  #Disse tre linjene lar oss velge farge. 
fargeB = "red" 

dragonX(t, depth, fargeA) # Start med klasse A (dragonX)

plt.axis('equal') #Legger til kommando slik at vinduet vises med tegningen. 
plt.show()