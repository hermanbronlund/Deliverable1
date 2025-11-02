import turtleplotlib as tpl
import matplotlib.pyplot as plt  # Importerer disse slik at hovedprogrammet virker med turtleplotlib og matplotlib.

# Omskrivningsregel for fraktalplanten i form av ordbok: F utvides til komplisert grenstruktur.
rule = {
    "F": "FF-[-F+F+F]+[+F-F-F]"
}

def rewrite_sequence(seq):
  
    new_seq = ""
    for char in seq:
        if char in rule:
            # Erstatt symbol fra input med omskrivningsregel
            new_seq += rule[char]
        else:
            # Symbol uten omskriving legges rett til ny sekvens
            new_seq += char
    return new_seq



def fractal_plant(turtle, depth, seq):
    """
    Tegner fraktalplanten basert på sekvens (seq).
    Hvis depth > 0: omskriver sekvensen for neste nivå og kaller seg selv rekursivt.
    Hvis depth == 0: tolker symboler i sekvensen og tegner fraktalen.
    """

    stack = []  # Stabel for lagring av turtle-posisjon og retning
    if depth == 0:
        # Tegnefasen: les hvert symbol, utfør passende tegneoperasjon.
        for char in seq:
            if char == "F":
                turtle.forward(10)  # Tegn fremover
            elif char == "-":
                turtle.left(25)     # Sving venstre 25 grader
            elif char == "+":
                turtle.right(25)    # Sving høyre 25 grader
            elif char == "[":
                # Lagre gjeldende posisjon og retning på stabel
                stack.append((turtle.position(), turtle.heading()))
            elif char == "]":
                pos, heading = stack.pop()
                x, y = pos
                turtle.goto(x, y)
                turtle.setheading(heading)
    else:
        # Omskriv hele sekvensen før tegning, for dybde-rekursjon
        new_seq = rewrite_sequence(seq)
        fractal_plant(t, depth, new_seq)

# Hovedprogram - oppsett og start på tegning
fig = plt.figure()
t = tpl.Turtle(fig, interactive=False)

start_seq = "F"  # Startsekvens
depth = 3        # Dybde: hvor mange ganger reglene omskrives og tegnes detaljert

fractal_plant(t, depth, start_seq)  # Start rekursiv tegning

plt.axis('equal')  # Sikre at tegningen vises proporsjonalt
plt.show()