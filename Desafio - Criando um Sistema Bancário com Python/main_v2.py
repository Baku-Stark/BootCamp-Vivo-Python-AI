from datetime import datetime
from service import *
from service.banco_services import *


class Conta:
    def __init__(self, numero, cliente) -> None:
        self._saldo = 0
        self._agencia = "0001"
        self._numero = numero
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor_saque : float, created_at : str):
        if valor_saque > self.saldo:
            print("[x] Você não pode realizar este tipo de ação porquê o valor de saque excede seu saldo...")

        else:
            self.saldo -= valor_saque
            f"[SAQUE] Valor de R${valor_saque:.2f} - {created_at}\n"
            print(Colors.BACK_GREEN + "=== SAQUE REALIZADO COM SUCESSO! ===" + Colors.END)
        return False

    def depositar(self, valor_deposito : float, created_at : str):
        if valor_deposito > 0:
            self.saldo += valor_deposito

            print(Colors.BACK_GREEN + f"=== DEPÓSITO DE 'R${valor_deposito:.2f}' REALIZADO COM SUCESSO ÀS {created_at}! ===" + Colors.END)

        else:
            print("[x] Este valor não pode ser adicionado em sua conta")

        return False

    @classmethod
    def nova_conta(cls, cliente_selecionado : object, numero_conta : int):
        return cls(numero_conta, cliente_selecionado)

class ContaCorrente(Conta):
    def __init__(self, numero_conta : int, cliente : object, limite : int = 500, limite_saque = 3) -> None:
        super().__init__(numero_conta, cliente)
        self._limite = limite
        self._limite_saque = limite_saque

    def sacar(self, valor_saque: float, created_at: str):
        if valor_saque > self._limite:
            print(Colors.RED + f"[x] Você não pode realizar este tipo de ação porquê seu limite é de R${self._limite:.2f}..."  + Colors.END)

        elif self._limite_saque == 0:
            print(Colors.RED + "[x] Você não pode realizar este tipo de ação porquê sua quantidade de saques por semana acabou..." + Colors.END)

        else:
            return super().sacar(valor_saque, created_at)
        
        return False

    def __str__(self):
        return f"""\
            Agência:\t{self._agencia}
            C/C:\t{self._numero}
            Titular:\t{self._cliente['nome']}
        """

class Cliente:
    def __init__(self, endereco : str) -> None:
        self.contas : list[object] = []
        self.endereco = endereco

    @property
    def adiciona_conta(self):
        return self.contas
    
    @adiciona_conta.setter
    def adiciona_conta(self, req : object):
        return True if req in self.contas.append(req) else False
    
    def realizar_transacao(self, conta, transacao):
        pass

class PessoaFisica(Cliente):
    def __init__(
            self,
            nome : str,
            data_nascimento : str,
            cpf : str,
            endereco : str
        ) -> None:
        super().__init__(endereco)
        
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

    def __str__(self) -> str:
        return str(
            {
                "nome" : self.nome,
                "data_nascimento" : self.data_nascimento,
                "cpf" : self.cpf
            }
        )

class BANCO_SISTEMA:
    """
        Aplicação principal do Banco.
    """

    def __init__(self) -> None:
        self._contas : list[object] = []
        self._clientes : list[object] = [
            {
                'contas': [],
                'endereco': 'Rio de Janeiro - Brazil', 
                'nome': 'Wallace De Freitas', 
                'data_nascimento': '07/07/2000',
                'cpf': '123.456.789-55'
            }
        ]

        self._data_atual = datetime.now().strftime("%d/%m/%y")
        self._hora_atual = datetime.now().strftime("%H:%M")
        self.created_at = f"{self._data_atual} - {self._hora_atual}"

        self.__extrato : str = ""
        # --- vars ---

        self.__start : bool = True
        while self.__start:
            print(Colors.CYAN + "=== SEJA BEM-VINDO AO $BANCO CENTRAL$ ===" + Colors.END)
            print("Criador da aplicação: Baku-Stark")
            self.__MENU_PRINCIPAL()

    def filtrar_cliente(self, cpf : str) -> object:
        clientes_filtrados = [cliente for cliente in self._clientes if cpf == cliente['cpf']]
        # print(clientes_filtrados)

        return clientes_filtrados[0] if clientes_filtrados else None

    def __MENU_PRINCIPAL(self) -> None:
        """
            Menu principal da aplicação com interação
        """

        try:
            print("""
            [ 1 ]\tDepositar
            [ 2 ]\tSaque
            [ 3 ]\tExtrato
            [ 4 ]\tNova conta
            [ 5 ]\tListar contas
            [ 6 ]\tCriar um novo usuário
            [ 7+ ]\tSair
            """)
            menu_choice = int(input("Escolha uma das opções acima: "))
            print('')

            if menu_choice == 1:
                self.__DEPOSITAR(self.created_at)

            elif menu_choice == 2:
                self.__SAQUE(self.created_at)

            elif menu_choice == 3:
                print("=== EXTRATO BANCÁRIO ===")
                print(self.__EXTRATO())

            elif menu_choice == 4:
                self.__NOVA_CONTA(self._contas)

            elif menu_choice == 5:
                self.__LISTAR_CONTAS()

            elif menu_choice == 6:
                self.__NOVO_CLIENTE(self._clientes)

            else:# menu_choice >= 7
                self.__start = False

            print('\n' * 3)

        except ValueError:
            print(Colors.RED + f"[x] Este tipo de valor não é permitido como escolha.\n- {ValueError}" + Colors.END)

    def __DEPOSITAR(self, created_at : str) -> None:
        """
            Módulo para depósito do dinheiro
        """

        print("=$ DEPOSITANDO VALOR NA CONTA $=")
        valor_deposito = float(input("Qual o valor para depósito?\nR$"))
        print('=' * 10)

        Conta.depositar(valor_deposito, created_at)

    def __SAQUE(self, created_at : str) -> None:
        """
            Módulo para saque do dinheiro
        """
        print("=$ SACANDO VALOR DA CONTA $=")
        valor_saque = float(input("Qual o valor que será feito para saque?\nR$"))
        print('=' * 10)

        cpf = str(input("Informe seu CPF(somente número)\nr: ")).strip() # 123.456.789-89
        model_cpf = RegexSys.model_cpf(cpf)
        print('')

        cliente_selecionado = self.filtrar_cliente(model_cpf)

        if not cliente_selecionado:
            Conta.sacar(valor_saque, created_at)

    def __EXTRATO(self) -> str:
        """
            Módulo para mostrar o extrato do cliente.
        """
        return f"{self.__extrato}" if len(self.__extrato) > 0 else "[x] Nenhuma função foi feita no momento..."

    def __NOVA_CONTA(self, contas : list[object]) -> None:
        """
                Módulo para criar uma nova conta.
        """
        numero_conta = len(self._contas) + 1

        cpf = str(input("Informe seu CPF(somente número)\nr: ")).strip() # 123.456.789-89
        model_cpf = RegexSys.model_cpf(cpf)
        print('')

        cliente_selecionado = self.filtrar_cliente(model_cpf)

        if not cliente_selecionado:
            print(Colors.BACK_PURPLE + f"[-] Não foi possível encontrar um cliente com esse CPF! -- ({model_cpf})" + Colors.END)
            print(Colors.PURPLE + "└── Encerrando fluxo de criação de conta" + Colors.END)
            return

        else:
            conta = ContaCorrente.nova_conta(cliente_selecionado, numero_conta)

            self._contas.append(conta)
            cliente_selecionado['contas'].append(contas)

    def __LISTAR_CONTAS(self):
        """
                Módulo para listar todas as contas de um usuário.
        """
        if len(self._contas) > 0:
            print('= CONTAS =')
            for conta in self._contas:
                print(f"- {conta}")

        else:
            print(Colors.BACK_PURPLE + f"[-] Nenhuma conta foi criada ainda" + Colors.END)

    def __NOVO_CLIENTE(self, clientes : list[object]) -> None:
        """
                Módulo para criar um novo usuario.
        """
        cpf = str(input("Informe seu CPF(somente número)\nr: ")).strip() # 123.456.789-89
        model_cpf = RegexSys.model_cpf(cpf)
        print('')

        if self.filtrar_cliente(model_cpf):
            print(Colors.BACK_PURPLE + f"[-] Existe um cliente com esse CPF! -- ({model_cpf})" + Colors.END)
            print(Colors.PURPLE + "└── Encerrando fluxo de criação de cliente" + Colors.END)
            #print(self.filtrar_cliente(model_cpf))

            return # finalizar o módulo
        
        if model_cpf:
            if RegexSys.match_cpf(model_cpf):
                nome = str(input("Insira seu nome completo\nr: ")).strip().title()
                print('')

                data_nascimento = str(input("Data De Nascimento(dd/mm/aaaa)\nr: ")).strip()
                print('')

                endereco = str(input("Informe seu endereço (logradouro, nro - bairro - cidade/sigla estado)\nr: ")).strip()
                print('')

                cliente = PessoaFisica(nome, data_nascimento, model_cpf, endereco)
                # print(cliente.__dict__)
                # print(cliente.__dict__['cpf'])

                clientes.append(cliente.__dict__)
                
                print(Colors.BACK_GREEN + "[-] Cliente criado com sucesso!" + Colors.END)

            else:
                print(Colors.BACK_RED + "[x] Modelo de CPF incorreto. Tente novamente!" + Colors.END)
        
        else:
            print(Colors.BACK_RED + "[x] Modelo de CPF incorreto... Tente de novo!" + Colors.END)
            
if __name__ == '__main__':
    OperationalSys.clean_console()

    try:
        BANCO_SISTEMA()

    except Exception as error:
        print(error)

    except KeyboardInterrupt:
        print(Colors.BACK_GRAY + f"[CRTL + C] {KeyboardInterrupt}" + Colors.END)

    finally:
        print("== APLICAÇÃO ENCERRADA! ==")