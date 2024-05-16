class Decorator:
    def __init__(self, nome = str, data_nascimento = str) -> None:
        self._nome = nome
        self._data_nascimento = data_nascimento


    @property # sem o decorator, o módulo não funciona e evitar uma inserção externa
    def mostrar_info(self):
        return f"Nome do usuário: {foo.mostrar_nome}\nIdade: {foo.mostrar_idade} anos" or any
    
    @property
    def mostrar_nome(self):
        return self._nome or any

    @property
    def mostrar_idade(self):
        return 2024 - self._data_nascimento

    @mostrar_info.setter
    def x(self, nome : str):
        self._nome = nome

foo = Decorator("Zoro", 1999)
print(foo.mostrar_info)

# foo.x = "Wallace"
# print("New Name: " + str(foo.x))