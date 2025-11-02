import turtleplotlib as tpl
import matplotlib.pyplot as plt

def snowflake_side(turtle, depth, lengde):  
    if depth == 0:
        turtle.forward(lengde)     # utfør F
    else:
        snowflake_side(turtle, depth-1, lengde/3)   # F ->
        turtle.left(60)            # +
        snowflake_side(turtle, depth-1, lengde/3)   # F
        turtle.right(120)          # -
        snowflake_side(turtle, depth-1, lengde/3)   # F
        turtle.left(60)            # +
        snowflake_side(turtle, depth-1, lengde/3)   # F

def snowflake(turtle, depth, lengde):
    for _ in range(3):
        snowflake_side(turtle, depth, lengde)
        turtle.right(120)

# Legger til en bit(lengde)-kode slik at snøfnugget så langt vises, for å være sikker på at koden stemmer før jeg begynner å legge til flere sider.
t = tpl.Turtle(interactive=False)

repetition_depth = 3     # 2 for enkel test, 3 for mer detaljert
snowflake(t, repetition_depth, 50)  # Endre til større eller mindre for å sjekke synlighet

plt.axis('equal')
plt.xlim(-90, 90)
plt.ylim(-70, 70)
plt.show()

