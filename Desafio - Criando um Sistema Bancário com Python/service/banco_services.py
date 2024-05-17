from abc import ABC, abstractproperty, abstractclassmethod

class Transacao(ABC):
    """
        # Sistema (abstração) para transição de contas.
    """
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    """
        # Sistema para depósito do banco.
    """
    def __init__(self, valor, created_at) -> None:
        self._valor = valor
        self._created_at = created_at
    
    @property
    def valor(self):
        return self._valor
    
    @property
    def created_at(self):
        return self._created_at
    
    def registrar(self, conta):
        """
            registrar() -> Class Deposito
        """
        # print(self.valor)
        # print("registrar() -> Class 'Deposito'")
        # print(conta)
        sucesso_transicao = conta.depositar(self.valor)

        if sucesso_transicao:
            # print(self.created_at)
            conta.historico.adicionar_transacao(self, self.created_at)

class Saque(Transacao):
    """
        # Sistema para saque do banco.
    """
    def __init__(self, valor, created_at) -> None:
        self._valor = valor
        self._created_at = created_at
    
    @property
    def valor(self):
        return self._valor
    
    @property
    def created_at(self):
        return self._created_at

    def registrar(self, conta):
        sucesso_transicao = conta.sacar(self.valor)

        if sucesso_transicao:
            # print(self.created_at)
            conta.historico.adicionar_transacao(self, self.created_at)

class Historico:
    """
        # Sistema de histórico da aplicação.
    """
    def __init__(self) -> None:
        self._transacoes : list[object] = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao, created_at : str):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": created_at
            }
        )