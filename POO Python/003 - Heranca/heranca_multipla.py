class Animal():
    def __init__(self, n_patas : int, ) -> None:
        self.n_patas = n_patas

    def __str__(self) -> str:
        return f"|{self.__class__.__name__}| {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo : str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.cor_pelo = cor_pelo

class Ave(Animal):
    def __init__(self, cor_bico : str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.cor_bico = cor_bico

class Ornitorrinco(Mamifero, Ave):
    pass

a = Ornitorrinco(
    n_patas = 4,
    cor_pelo = "marrom",
    cor_bico = "preto"
)

print(a)
# OUTPUT -> |Ornitorrinco| n_patas: 4, cor_bico: preto, cor_pelo: marrom