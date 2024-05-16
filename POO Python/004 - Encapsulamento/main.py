class Encapsulamento:
    def __init__(self, saldo : float) -> None:
        # variavel privada
        self._saldo = saldo

    def depositar(self, valor : float) -> None:
        self._saldo += valor

    def sacar(self, valor : float) -> None:
        self._saldo -= valor

    def mostrar_saldo(self) -> float:
        return self._saldo

conta = Encapsulamento(550.50)
print(f"R${conta.mostrar_saldo():.2f}")