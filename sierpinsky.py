import turtleplotlib as tpl
import matplotlib.pyplot as plt  #importerer disse slik at hovedprogrammet virker med turtleplotlib og matplotlib. 

# Kode over er hentet fra canvas, ihht instruksjoner i oppgaven – MODIFISERT for at A og B bruker hver sin farge.

def sierpinskyA(turtle, depth, colorA, colorB):
    # A → B−A−B
    if depth > 0:  # X -> (her: A → B−A−B)
        sierpinskyB(turtle, depth-1, colorA, colorB)  #      X  (her: B)
        turtle.color(colorA)  #Legger til denne linjen for å kunne velge farger (A).
        turtle.right(60)  #         + (venstresving for fraktal-trekant)
        sierpinskyA(turtle, depth-1, colorA, colorB)  #          Y  (her: A)
        turtle.right(60)  #         + (venstresving for fraktal-trekant)
        sierpinskyB(turtle, depth-1, colorA, colorB)  #              F (her: B)
    else:
        turtle.color(colorA)  #Legger til denne linjen for å kunne velge farger (A).
        turtle.forward(10)  #Grunnstrek

def sierpinskyB(turtle, depth, colorA, colorB):
    # B → A+B+A
    if depth > 0:  # Y -> (her: B → A+B+A)
        turtle.color(colorB)  #Legger til denne linjen for å kunne velge farger (B).
        sierpinskyA(turtle, depth-1, colorA, colorB)  #      F (her: A)
        turtle.left(60)  #        - (høyresving trekant)
        sierpinskyB(turtle, depth-1, colorA, colorB)  #         X (her: B)
        turtle.left(60)  #        - (høyresving trekant)
        sierpinskyA(turtle, depth-1, colorA, colorB)  #           Y (her: A)
    else:
        turtle.color(colorB)  #Legger til denne linjen for å kunne velge farger (B).
        turtle.forward(10)

#Hovedprogram
fig = plt.figure()
t = tpl.Turtle(fig, interactive=False)

depth = 5
fargeA = "blue"  #Disse tre linjene lar oss velge farge.
fargeB = "red"

sierpinskyA(t, depth, fargeA, fargeB)  # Start med klasse A (her: sierpinskyA)

plt.axis('equal')  #Legger til kommando slik at vinduet vises med tegningen. 
plt.show()