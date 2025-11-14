from complex import Complex

def test_complex():
    print("Test 1: Lage komplekse tall")
    z = Complex(1, 2)
    assert z.re == 1
    assert z.im == 2
    print("Test 1: z =", z)
    print("  Reell del:", z.re)
    print("  Imaginær del:", z.im)

    print("Test 2: __str__ og __repr__")
    assert str(z) == "1+2i"
    assert repr(z) == "Complex(1, 2)"
    print("Test 2: str(z) =", str(z))
    print("Test 2: repr(z) =", repr(z))


    print("Test 3: Addisjon og subtraksjon")
    a = Complex(3, 4)
    b = Complex(-1, 1)
    sum_ab = a + b
    diff_ab = a - b
    assert (a + b).re == 2 and (a + b).im == 5
    assert (a - b).re == 4 and (a - b).im == 3
    print("Test 3: a =", a, ", b =", b)
    print("  a + b =", sum_ab)
    print("  a - b =", diff_ab)
    print("  (re, im) sum:", sum_ab.re, sum_ab.im)
    print("  (re, im) diff:", diff_ab.re, diff_ab.im)

    print("Test 4: Multiplikasjon")
    x = Complex(1, 2)
    y = Complex(3, 4)
    prod = x * y
    assert prod.re == -5 and prod.im == 10  # (1+2i)*(3+4i) = -5+10i
    print("Test 4: x =", x, ", y =", y)
    print("  x * y =", prod)
    print("  (re, im) product:", prod.re, prod.im)

    print("Test 5: Likhet")
    assert x == Complex(1, 2)
    assert x != y
    print("Test 5: x == y:", x == y)
    print("Test 5: x == Complex(1,2):", x == Complex(1,2))
    print("Test 5: x != y:", x != y)

    print("Test 6: Regning med vanlige tall")
    assert (x + 3) == Complex(4, 2)
    assert (3 + x) == Complex(4, 2)
    assert (x * 2) == Complex(2, 4)
    assert (2 * x) == Complex(2, 4)
    print("Test 6: x + 3 =", x + 3)
    print("Test 6: 3 + x =", 3 + x)
    print("Test 6: x * 2 =", x * 2)
    print("Test 6: 2 * x =", 2 * x)

    print("Alle tester bestått!")

if __name__ == "__main__":
    test_complex()