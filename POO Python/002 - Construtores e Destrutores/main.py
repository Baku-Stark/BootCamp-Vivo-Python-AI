class ConsDest():
    def __init__(self, nome : str, cor : str, acordado : bool = True) -> None:
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self) -> None:
        print("Removendo instancia da classe")

    def latir(self) -> None:
        print("au! au! au!")

ConsDest("Chappie", "Amarelo").latir() if __name__ == '__main__' else None