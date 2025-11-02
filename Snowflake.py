import turtleplotlib as tpl
import matplotlib.pyplot as plt

def snowflake_side(turtle, depth, lengde):  
    # Tegner én side av snøfnugget.
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

def complete_flake(turtle, depth, lengde, color='blue', linewidth=2):
    # Funksjon for å tegne et komplett snøfnugg, ikke bare én side.
    turtle.color(color)       # Sett farge
    turtle.width(linewidth)      # Sett linjetykkelse
    for _ in range(3):
        snowflake_side(turtle, depth, lengde)
        turtle.right(120)
        
# Legger til kode slik at snøfnugget vises, og dette kan brukes for å teste at det fungerer før man legger til utvidelser.
fig = plt.figure()
t = tpl.Turtle(fig, interactive=False)

# Justerbare parametere – endre for å teste ulike snøfnugg
repetition_depth = 3      # 2 for enkel test, 3 for mer detaljert
flake_size = 100           # Endre til større eller mindre for å sjekke synlighet
flake_color = 'deepskyblue' # Linjefarge, f.eks. 'blue', 'red', 'green'
flake_linewidth = 2       # Linjetykkelse

complete_flake(
    t,
    repetition_depth,
    flake_size,
    color=flake_color,
    linewidth=flake_linewidth
)

plt.axis('equal')
plt.xlim(-90, 90)
plt.ylim(-70, 70)
plt.show()

