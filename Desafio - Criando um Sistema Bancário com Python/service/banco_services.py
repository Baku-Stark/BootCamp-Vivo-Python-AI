from abc import ABC, abstractproperty, abstractclassmethod

class Transacao(ABC):
    """
        # Sistema (abstração) para transição de contas.
    """
    @property
    @abstractproperty
    def valor(self):
        pass

    @property
    @abstractproperty
    def created_at(self):
        pass

    @abstractclassmethod
    def registrar(self, conta, created_at):
        pass

class Deposito(Transacao):
    def __init__(self, valor : float, created_at : str) -> None:
        self._valor : valor
        self._created_at = created_at
    
    @property
    def valor(self):
        return self._valor
    
    @property
    def created_at(self):
        return self._created_at
    
    def registrar(self, conta):
        sucesso_transicao = conta.depositar(self.valor, self.created_at)

class Saque(Transacao):
    """
        # Sistema para saque do banco.
    """
    def __init__(self, valor : float, created_at : str) -> None:
        self._valor : valor
        self._created_at = created_at
    
    @property
    def valor(self):
        return self._valor
    
    @property
    def created_at(self):
        return self._created_at

    def registrar(self, Conta_Class):
        sucesso_transicao = Conta_Class.sacar(self.valor)

class Historico:
    """
        # Sistema de histórico da aplicação.
    """
    def __init__(self) -> None:
        self._transacoes : list[object] = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao : object, created_at : str):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": created_at
            }
        )