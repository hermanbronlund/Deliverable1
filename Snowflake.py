import turtleplotlib as tpl

def snowflake(turtle, depth):
    if depth == 0:
        turtle.forward(10)          # utfør F
    else:                          # F ->
        snowflake(turtle, depth-1)  #      F
        turtle.left(60)             #        +
        snowflake(turtle, depth-1)  #          F
        turtle.right(60)            #            -
        turtle.right(60)            #              -  
        snowflake(turtle, depth-1)  #                F
        turtle.left(60)             #                  +
        snowflake(turtle, depth-1)  #                    F

t = tpl.Turtle(interactive=False)
snowflake(t, 3)
#kode hit er hentet/kopiert ihht instruks i oppgaven. 
#Legger til en bit kode slik at snøfnugget sålangt vises, for å være sikker på at koden stemmer før jeg begynner å legge til kode. 
tpl.show()