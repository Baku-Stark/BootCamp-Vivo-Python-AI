# TODO: Crie a classe PlanoTelefone, seu método de inicialização e encapsule os atributos, 'nome' e 'saldo':
class PlanoTelefone:
    def __init__(self, nome_plano, saldo_inicial) -> None:
        self._nome_plano = nome_plano
        self._saldo_inicial = saldo_inicial

    # ENCAPSULAMENTO
    def get_nome_plano(self):
        return self._nome_plano
    
    def get_saldo(self):
        return self._saldo_inicial
    
    # TODO: Crie um método 'verificar_saldo' para verificar o saldo do plano sem acessar diretamente o atributo:
    def verificar_saldo(self) -> float:
        return self.get_saldo(), self.mensagem_personalizada()

    # TODO: Crie um método 'mensagem_personalizada' para gerar uma mensagem personalizada com base no saldo:
    def mensagem_personalizada(self) -> str:
        mensagem = ""

        # Caso o saldo seja menor do que 10, retorne: "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        if self.get_saldo() < 10:
            mensagem = "Seu saldo está baixo. Recarregue e use os serviços do seu plano."

        # Caso o saldo seja maior ou igual a 50, retorne: "Parabéns! Continue aproveitando seu plano sem preocupações."
        elif self.get_saldo() >= 50:
            mensagem = "Parabéns! Continue aproveitando seu plano sem preocupações."

        else:
            mensagem = "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

        return mensagem
    

# Classe UsuarioTelefone:
class UsuarioTelefone(PlanoTelefone):
    def __init__(self, nome, plano):
        super().__init__(nome_plano, saldo_inicial)
        self.nome = nome
        self.plano = plano


# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

 # Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial) 
usuario = UsuarioTelefone(nome_usuario, plano_usuario)  

# Chamada do método para get_saldo sem acessar diretamente os atributos do plano:
saldo_usuario, mensagem_usuario = usuario.verificar_saldo()
print(mensagem_usuario)