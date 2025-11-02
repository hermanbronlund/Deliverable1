import turtleplotlib as tpl
import matplotlib.pyplot as plt

def snowflake(turtle, depth, lengde):
    if depth == 0:
        turtle.forward(10)          # utfør F
    else:                          # F ->
        snowflake(turtle, depth-1, lengde/3)  #      F
        turtle.left(60)             #        +
        snowflake(turtle, depth-1, lengde/3)  #          F
        turtle.right(60)            #            -
        turtle.right(60)            #              -  
        snowflake(turtle, depth-1, lengde/3)  #                F
        turtle.left(60)             #                  +
        snowflake(turtle, depth-1, lengde/3)  #                    F
#kode hit er hentet/kopiert ihht instruks i oppgaven. 
#Legger til en bit(lengde) kode slik at snøfnugget sålangt vises, for å være sikker på at koden stemmer før jeg begynner å legge til kode. 
t = tpl.Turtle(interactive=False)

snoefnugg_start_lengde = 150    # Endre til større eller mindre for å sjekke synlighet
repetition_depth = 3            # 2 for enkel test, 3 for mer detaljert
snowflake(t, repetition_depth, snoefnugg_start_lengde)

plt.show()
