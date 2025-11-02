import turtleplotlib as tpl
import matplotlib.pyplot as plt

rule = "FF-[-F+F+F]+[+F-F-F]" #regel for planten. 

def fractal_plant(turtle, depth, seq):
    stack = []  # Stub for lagring av turtle-posisjoner ved [ og ]

    for char in seq:
        if depth == 0:
            if char == "F":
                turtle.forward(10)  # Tegner en linje
        else:
            if char == "F":
                # Kaller funksjonen rekursivt med ny sekvens (her enklere med samme regel)
                fractal_plant(turtle, depth-1, rule)
            elif char == "-":
                turtle.left(25)  # Venstresving på 25 grader
            elif char == "+":
                turtle.right(25)  # Høyresving på 25 grader
            elif char == "[":
                # Lagre turtle-posisjon og retning på stack
                stack.append((turtle.position(), turtle.heading()))
            elif char == "]":
                # Hent turtle-posisjon og retning fra stack
                pos, heading = stack.pop()
                turtle.setposition(pos)
                turtle.setheading(heading)

#Hovedprogram
fig = plt.figure()
t = tpl.Turtle(fig, interactive=False)

depth = 3 #Starter med lav dybde for å teste. 

fractal_plant(t, depth, seq=) #Kaller på funksjonen.


plt.show()



