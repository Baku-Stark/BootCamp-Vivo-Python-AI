class FirstAPP():
    def __init__(self, cor : str, modelo : str, ano : int, valor : float) -> None:
        # --- objetos
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = 1

        # print(self.mostrar_cor())
        # print(self.buzinar())
        # print(self.freiar())
        # print(self.correr())

    # --- método
    def __str__(self) -> str:
        # return f"{self.__class__.__name__}: {[f'{chave}-{valor}' for chave, valor in self.__dict__.items()]}"
        # OUTPUT: FirstAPP: ['cor-vermelha', 'modelo-caloi', 'ano-2015', 'valor-600.0']

        return f"{self.__class__.__name__}: {', '.join([f'{chave}-{valor}' for chave, valor in self.__dict__.items()])}"
        # OUTPUT: FirstAPP: cor-vermelha, modelo-caloi, ano-2015, valor-600.0

    def trocar_marcha(self, nro_marcha : int):
        _self = self

        def _trocar_marcha():
            print("Marcha trocada...") if nro_marcha > _self.marcha else print("não foi possível trocar a marcha")
    
    def buzinar(self) -> str:
        print("Plim plim...")

    def freiar(self) -> str:
        print("A bicicleta parou.")

    def correr(self) -> str:
        print("A bicicleta está andando.")

print(FirstAPP("vermelha", "caloi", 2015, 600.00)) if __name__ == '__main__' else print("None")