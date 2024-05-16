class Estudante:
    escola: str

    def __init__(self, nome : str, num : int, escola = "DIO") -> None:
        self._nome = nome
        self._num = num
        self._escola = escola

    def __str__(self) -> str:
        return f"{self._nome} ({self._num}) - {self._escola}"
    
    @classmethod
    def criar_data_nascimento(cls, ano : int, data : int, mes : int, nome : str):
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod
    def maior_idade(idade : int):
        return idade >= 18


# estudante = Estudante("Wallace", 555776)
estudante = Estudante.criar_data_nascimento(2000, 7, 7, "Wallace")
print(estudante)

print(Estudante.maior_idade(18))