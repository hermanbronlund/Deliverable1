import turtleplotlib as tpl
import matplotlib.pyplot as plt  #importerer disse slik at hovedprogrammet virker med turtleplotlib og matplotlib. 

    
def sierpinskyX(turtle, depth, color):
    if depth > 0:                  # X ->
        sierpinskyX(turtle, depth-1, color)   #       X  
        turtle.color(color)  #Legger til denne linjen for å kunne velge farger.        
        turtle.left(90)            #         +
        sierpinskyY(turtle, depth-1, color)   #           Y
        turtle.forward(10)         #             F
        
        
def sierpinskyY(turtle, depth, color):
    if depth > 0:                  # Y ->
        turtle.color(color)  #Legger til denne linjen for å kunne velge farger. 
        turtle.forward(10)         #       F
        sierpinskyX(turtle, depth-1, color)   #         X
        turtle.right(90)           #           -
        sierpinskyY(turtle, depth-1, color)   #             Y

        #Kode over er hentet fra canvas, ihht instruksjoner i oppgaven. 

#Hovedprogram
fig = plt.figure()
t = tpl.Turtle(fig, interactive=False)

depth = 5
fargeA = "blue"  #Disse tre linjene lar oss velge farge. 
fargeB = "red" 

sierpinskyX(t, depth, fargeA) # Start med klasse A (dragonX)

plt.axis('equal') #Legger til kommando slik at vinduet vises med tegningen. 
plt.show()