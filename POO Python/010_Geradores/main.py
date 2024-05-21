def Geradores():
    text = "Python"
    yield text

def Geradores_A(lista: list[int]):
    for numero in lista:
        yield numero * 2 if numero % 2 == 0 else ''

for i in Geradores_A(list(num for num in range(1, 101))):
    print(i)