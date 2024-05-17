from service import *
from service.banco_services import *

class Conta:
    def __init__(self, numero, cliente) -> None:
        self._saldo = 0
        self._agencia = "0001"
        self._numero = numero
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        """
        # Classe 'Conta' - @classmethod
            Criar nova conta para um cliente.
        """
        return cls(numero, cliente)

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
    
    def sacar(self, valor_saque):
        if valor_saque > self._saldo:
            print("[x] Você não pode realizar este tipo de ação porquê o valor de saque excede seu saldo...")

        else:
            self._saldo -= valor_saque
            print(Colors.BACK_GREEN + "=== SAQUE REALIZADO COM SUCESSO! ===" + Colors.END)
            print(f"└──[SAQUE] Valor de R${valor_saque:.2f} - {CurrentTime.created_at()}")
            return True

        return False

    def depositar(self, valor_deposito):
        if valor_deposito > 0:
            self._saldo += valor_deposito

            print(Colors.BACK_GREEN + f"=== DEPÓSITO REALIZADO COM SUCESSO! ===" + Colors.END)
            print(f"└──[DEPÓSITO] Valor de R${valor_deposito:.2f} ({CurrentTime.created_at()})")

        else:
            print("[x] Este valor não pode ser adicionado em sua conta")

            return False
        
        return True

class ContaCorrente(Conta):
    def __init__(self, numero_conta : int, cliente : object, limite : float = 500.00, limite_saque = 3) -> None:
        super().__init__(numero_conta, cliente)
        self._limite = limite
        self._limite_saque = limite_saque

    def sacar(self, valor_saque: float):
        if valor_saque > self._limite:
            print(Colors.RED + f"[x] Você não pode realizar este tipo de ação porquê seu limite é de R${self._limite:.2f}..."  + Colors.END)

        elif self._limite_saque == 0:
            print(Colors.RED + "[x] Você não pode realizar este tipo de ação porquê sua quantidade de saques por semana acabou..." + Colors.END)

        else:
            return super().sacar(valor_saque)
        
        return False

    def __str__(self):
        return f"""
            Agência:\t{self.agencia}
            C/C:\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class Cliente:
    def __init__(self, endereco) -> None:
        self.contas = []
        self.endereco = endereco

    def realizar_transacao(self, conta, transacao):
        """
            # Classe 'Cliente'

            Transação do cliente.

            args:
                - conta : str
        """
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf,endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class BANCO_SISTEMA:
    """
        Aplicação principal do Banco.
    """

    def __init__(self) -> None:
        self._contas : list = []
        self._clientes : list = []

        self.__start : bool = True
        while self.__start:
            print(Colors.CYAN + "=== SEJA BEM-VINDO AO $BANCO CENTRAL$ ===" + Colors.END)
            print("Criador da aplicação: Baku-Stark")
            self.__MENU_PRINCIPAL()

    def filtrar_cliente(self, cpf : str):
        """
            Retornar apenas o cliente desejado pelo seu CPF.

            return :
                list[]
        """
        clientes_filtrados = [cliente for cliente in self._clientes if cpf == cliente.cpf]
        # print(clientes_filtrados)

        return clientes_filtrados[0] if clientes_filtrados else None
    
    def recuperar_conta_cliente(self, cliente):
        """
            Retornar a conta do cliente desejado.

            return :
                - cliente.contas -> conta do cliente
        """
        if not cliente.contas:
            print(Colors.BACK_PURPLE + f"[-] Cliente não possui uma conta" + Colors.END)
            print(Colors.PURPLE + "└── Encerrando fluxo de recuperação de conta" + Colors.END)
            return
        
        else:
            # print('recuperar_conta_cliente')
            # print(cliente.contas[0])
            return cliente.contas[0]

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
                self.__DEPOSITAR()

            elif menu_choice == 2:
                self.__SAQUE()

            elif menu_choice == 3:
                print("=== EXTRATO BANCÁRIO ===")
                print(self.__EXTRATO())

            elif menu_choice == 4:
                self.__NOVA_CONTA()

            elif menu_choice == 5:
                self.__LISTAR_CONTAS()

            elif menu_choice == 6:
                self.__NOVO_CLIENTE()

            else:# menu_choice >= 7
                self.__start = False

            print('\n' * 3)

        except ValueError:
            print(Colors.RED + f"[x] Este tipo de valor não é permitido como escolha.\n- {ValueError}" + Colors.END)

    def __DEPOSITAR(self) -> None:
        """
            Módulo para depósito do dinheiro
        """
        
        cpf = str(input("Informe seu CPF(somente número)\nr: ")).strip() # 123.456.789-89
        model_cpf = RegexSys.model_cpf(cpf)
        print('')

        cliente = self.filtrar_cliente(model_cpf)
        #print(cliente)
        
        if not cliente:
            print(Colors.BACK_PURPLE + f"[-] Não foi possível encontrar um cliente com esse CPF! -- ({model_cpf})" + Colors.END)
            print(Colors.PURPLE + "└── Encerrando fluxo de criação de conta" + Colors.END)
            return
        
        else:
            print(Colors.BACK_GREEN + f"[-] Cliente $= Banco Cental =$ encontrado! -- ({model_cpf})" + Colors.END)
            print(Colors.GREEN + f"└── Depósito sendo realizado por: {cliente.nome}!\n" + Colors.END)
            
            print("=$ DEPOSITANDO VALOR NA CONTA $=")
            valor_deposito = float(input("Qual o valor para depósito?\nR$"))
            print('=' * 10)
            print('')

            transacao = Deposito(valor_deposito, CurrentTime.created_at())
            # print(f"Transação: {transacao}")

            conta = self.recuperar_conta_cliente(cliente)

            if not conta:
                return
            
            cliente.realizar_transacao(conta, transacao)
                

    def __SAQUE(self) -> None:
        """
            Módulo para saque do dinheiro
        """
        cpf = str(input("Informe seu CPF(somente número)\nr: ")).strip() # 123.456.789-89
        model_cpf = RegexSys.model_cpf(cpf)
        print('')

        cliente = self.filtrar_cliente(model_cpf)
        #print(cliente)
        
        if not cliente:
            print(Colors.BACK_PURPLE + f"[-] Não foi possível encontrar um cliente com esse CPF! -- ({model_cpf})" + Colors.END)
            print(Colors.PURPLE + "└── Encerrando fluxo de saque de dinheiro" + Colors.END)
            return
        
        else:
            print(Colors.BACK_GREEN + f"[-] Cliente $= Banco Cental =$ encontrado! -- ({model_cpf})" + Colors.END)
            print(Colors.GREEN + f"└── '{cliente.nome}' está realizando seu saque!\n" + Colors.END)

            print("=$ SACANDO VALOR DA CONTA $=")
            valor_saque = float(input("Qual o valor que será feito para saque?\nR$"))
            print('=' * 10)
            print('')

            transacao = Saque(valor_saque, CurrentTime.created_at())
            # print(f"Transação: {transacao}")

            conta = self.recuperar_conta_cliente(cliente)

            if not conta:
                return
            
            cliente.realizar_transacao(conta, transacao)

    def __EXTRATO(self) -> None:
        """
            Módulo para mostrar o extrato do cliente.
        """
        cpf = str(input("Informe seu CPF(somente número)\nr: ")).strip() # 123.456.789-89
        model_cpf = RegexSys.model_cpf(cpf)
        print('')

        cliente = self.filtrar_cliente(model_cpf)
        #print(cliente)
        
        if not cliente:
            print(Colors.BACK_PURPLE + f"[-] Não foi possível encontrar um cliente com esse CPF! -- ({model_cpf})" + Colors.END)
            print(Colors.PURPLE + "└── Encerrando fluxo de exibição do extrato bancário." + Colors.END)
            return
        
        else:
            print(Colors.BACK_GREEN + f"[-] Cliente $= Banco Cental =$ encontrado! -- ({model_cpf})" + Colors.END)
            print(Colors.GREEN + f"└── Extrato de '{cliente.nome}'\n" + Colors.END)

            conta = self.recuperar_conta_cliente(cliente)
            if not conta:
                return

            transacoes = conta.historico.transacoes
            
            extrato = ""
            print(f"{'=' * 10} EXTRATO {'=' * 10}")
            if not transacoes:
                print(Colors.BACK_PURPLE + f"[-] Não foram realizadas movimentações -- ({model_cpf})" + Colors.END)

            else:
                for transacao in transacoes:
                    extrato += f"{transacao['tipo']} - ({transacao['data']})\n- R${transacao['valor']:.2f}\n\n"
            print(extrato)
            print(f"\nSaldo:\tR${conta.saldo:.2f}")
            print("=" * 29)

    def __NOVA_CONTA(self) -> None:
        """
                Módulo para criar uma nova conta.
        """
        numero_conta = len(self._contas) + 1

        print("=$ CRIANDO UMA NOVA CONTA $=")
        cpf = str(input("Informe seu CPF(somente número)\nr: ")).strip() # 123.456.789-89
        model_cpf = RegexSys.model_cpf(cpf)
        print('')

        cliente_selecionado = self.filtrar_cliente(model_cpf)

        if not cliente_selecionado:
            print(Colors.BACK_PURPLE + f"[-] Não foi possível encontrar um cliente com esse CPF! -- ({model_cpf})" + Colors.END)
            print(Colors.PURPLE + "└── Encerrando fluxo de criação de conta" + Colors.END)
            return

        else:
            print(Colors.BACK_GREEN + f"[-] Cliente $= Banco Cental =$ encontrado! -- ({model_cpf})" + Colors.END)
            print(Colors.GREEN + f"└── O cliente '{cliente_selecionado.nome}' criou uma nova conta!\n" + Colors.END)

            conta = ContaCorrente.nova_conta(cliente_selecionado, numero_conta)

            self._contas.append(conta)
            cliente_selecionado.contas.append(conta)

    def __LISTAR_CONTAS(self):
        """
                Módulo para listar todas as contas de um usuário.
        """
        #print(self._contas)

        if len(self._contas) > 0:
            print('\t=====\tCONTAS\t=====')
            for conta in self._contas:
                print(conta)

        else:
            print(Colors.BACK_PURPLE + f"[-] Nenhuma conta foi criada ainda." + Colors.END)

    def __NOVO_CLIENTE(self) -> None:
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

                self._clientes.append(cliente)
                
                print(Colors.BACK_GREEN + "[-] Cliente criado com sucesso!" + Colors.END)

                # === Criar a primeira conta para o novo usuário
                print(Colors.GREEN + f"└── '{cliente.nome}' crie sua primeira conta no banco." + Colors.END)
                self.__NOVA_CONTA()

            else:
                print(Colors.BACK_RED + "[x] Modelo de CPF incorreto. Tente novamente!" + Colors.END)
        
        else:
            print(Colors.BACK_RED + "[x] Modelo de CPF incorreto... Tente de novo!" + Colors.END)
            
if __name__ == '__main__':
    OperationalSys.clean_console()

    try:
        BANCO_SISTEMA()
        
    except KeyboardInterrupt:
        print(Colors.BACK_GRAY + f"[CRTL + C] {KeyboardInterrupt}" + Colors.END)

    finally:
        print("== APLICAÇÃO ENCERRADA! ==")