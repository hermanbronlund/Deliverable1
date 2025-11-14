class Complex:
    def __init__(self, re=0, im=0):
        # Denne funksjonen kjører hver gang jeg lager et Complex objekt.
        # 'self.re' lagrer den reelle (vanlige) delen av tallet.
        # 'self.im' lagrer den imaginære delen.
        self.re = re
        self.im = im

    def __str__(self):
        # Denne funksjonen bestemmer hvordan objektet vises når man bruker print().
        # F.eks. Complex(2,3) gir '2+3i' på skjermen.
        return f"{self.re}+{self.im}i"

    def __repr__(self):
        # Gir en mer detaljert tekst om objektet - for lister, feilsøking osv.
        return f"Complex({self.re}, {self.im})"

    def __add__(self, other):
        # Denne funksjonen gjør at jeg kan bruke + mellom Complex-objekter (eller med tall).
        # Den legger sammen den reelle og den imaginære delen hver for seg.
        if isinstance(other, Complex):
            return Complex(self.re + other.re, self.im + other.im)
        else:
            # Hvis 'other' bare er et tall, legges det til realdelen
            return Complex(self.re + other, self.im)
    
    def __radd__(self, other):
        # Gjør at '3 + z' også funker, ikke bare 'z + 3'.
        return self.__add__(other)

    def __sub__(self, other):
        # Trekker fra på samme måte som addisjon, men minus istedenfor pluss.
        if isinstance(other, Complex):
            return Complex(self.re - other.re, self.im - other.im)
        else:
            return Complex(self.re - other, self.im)
    
    def __rsub__(self, other):
        # Gjør at '3 - z' funker. Merk at vi snur rekkefølgen.
        if isinstance(other, Complex):
            return Complex(other.re - self.re, other.im - self.im)
        else:
            return Complex(other - self.re, -self.im)
        
    def __mul__(self, other):
        # Multipliserer to komplekse tall:
        # (a+bi)*(c+di) = (ac-bd)+(ad+bc)i
        if isinstance(other, Complex):
            a, b = self.re, self.im
            c, d = other.re, other.im
            return Complex(a*c - b*d, a*d + b*c)
        else:
            # Hvis 'other' er et tall, ganger det med begge deler.
            return Complex(self.re * other, self.im * other)
    
    def __rmul__(self, other):
        # Sørger for at '3 * z' også virker.
        return self.__mul__(other)
    
    def __eq__(self, other):
        # Sjekker om to komplekse tall er like.
        if isinstance(other, Complex):
            return self.re == other.re and self.im == other.im
        else:
            return False

    
z = Complex(1, 2)
y = Complex(3, 4)


