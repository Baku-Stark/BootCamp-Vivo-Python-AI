class Veiculo:
    def __init__(self, cor : str, placa : str, n_rodas : int) -> None:
        self.cor = cor
        self.placa = placa
        self.n_rodas = n_rodas

    def ligar_motor(self):
        print("Ligando motor")

class Carro(Veiculo):
    pass

class Motocicleta(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor : str, placa : str, n_rodas : int, carregado : bool) -> None:
        super().__init__(cor, placa, n_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"[{self.placa}] Carregado : {'Sim' if self.carregado else 'Não está carregado'}")

veiculo = Caminhao("preto", "KGB8080", 6, True)
veiculo.ligar_motor()
veiculo.esta_carregado()