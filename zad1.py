def factorial(n):
    if n == 0:
        return 0
    return n * factorial(n - 1)
###problem polega na tym, że 0! to 1 a nie 0 tak jak w zadaniu

###poprawny kod
def factorial_poprawiony(n):
    if n == 0:
        return 1
    return n * factorial_poprawiony(n - 1)


###testy
def test_factorial():
    assert factorial_poprawiony(0) == 1, "Test dla 0! nie przeszedl"
    assert factorial_poprawiony(3) == 6, "Test dla 3! nie przeszedl"
    assert factorial_poprawiony(5) == 120, "Test dla 5! nie przeszedl"
    print("Wszystkie testy przeszly pomyslnie!")


test_factorial()


