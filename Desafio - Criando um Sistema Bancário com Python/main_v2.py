from datetime import datetime
from service import OperationalSys, RegexSys, Colors

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

class BANCO_SISTEMA(PessoaFisica):
    """
        Aplicação principal do Banco.
    """

    def __init__(self) -> None:
        self.contas : list[object] = []
        self._clientes : list[object] = []

        self._data_atual = datetime.now().strftime("%d/%m/%y")
        self._hora_atual = datetime.now().strftime("%H:%M")
        self._created_at = f"{self._data_atual} - {self._hora_atual}"

        self.__extrato : str = ""
        self.__saldo : int = 0
        self.__limite : int = 500
        self.__numero_saques : int = 0
        self.__LIMITE_SAQUES : int = 3
        # --- vars ---

        self.__start : bool = True
        while self.__start:
            print(Colors.CYAN + "=== SEJA BEM-VINDO AO $BANCO CENTRAL$ ===" + Colors.END)
            print("Criador da aplicação: Baku-Stark")
            self.__MENU_PRINCIPAL()

    def filtrar_cliente(self, cpf : str) -> list:
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
            [ 6 ]\tNovo usuário
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
                self.__NOVO_USUARIO(self._clientes)

            else:# menu_choice >= 7
                self.__start = False

            print('\n' * 3)

        except ValueError:
            print(Colors.RED + f"[x] Este tipo de valor não é permitido como escolha.\n- {ValueError}" + Colors.END)

    def __DEPOSITAR(self) -> None:
        """
            Módulo para depósito do dinheiro
        """

        print("=$ DEPOSITANDO VALOR NA CONTA $=")
        valor_deposito = float(input("Qual o valor para depósito?\nR$"))
        print('=' * 10)

        if valor_deposito > 0:
            self.__saldo += valor_deposito
            self.__extrato += f"[Depósito feito] Valor de R${valor_deposito:.2f} - {self._hora_atual}\n"
            print(Colors.GREEN + "=== DEPÓSITO REALIZADO COM SUCESSO! ===" + Colors.END)

        else:
            print(Colors.RED + "[x] Este valor não pode ser adicionado em sua conta"  + Colors.END)

    def __SAQUE(self) -> None:
        """
            Módulo para saque do dinheiro
        """

        print("=$ SACANDO VALOR DA CONTA $=")
        valor_saque = float(input("Qual o valor que será feito para saque?\nR$"))
        print('=' * 10)

        if valor_saque > self.__saldo:
            print("[x] Você não pode realizar este tipo de ação porquê o valor de saque excede seu saldo...")

        elif valor_saque > self.__limite:
            print(Colors.RED + f"[x] Você não pode realizar este tipo de ação porquê seu limite é de R${self.__limite:.2f}..."  + Colors.END)

        elif self.__LIMITE_SAQUES == 0:
            print(Colors.RED + "[x] Você não pode realizar este tipo de ação porquê sua quantidade de saques por semana acabou..." + Colors.END)

        else:
            self.__extrato += f"[SAQUE] Valor de R${valor_saque:.2f} - {self._hora_atual}\n"
            print(Colors.GREEN + "=== SAQUE REALIZADO COM SUCESSO! ===" + Colors.END)

            self.__numero_saques += 1

    def __EXTRATO(self) -> str:
        """
            Módulo para mostrar o extrato do cliente.
        """
        return f"{self.__extrato}" if len(self.__extrato) > 0 else "[x] Nenhuma função foi feita no momento..."

    def __NOVO_USUARIO(self, clientes : list[object]) -> None:
        """
                Módulo para criar um novo usuario.
        """
        cpf = str(input("Informe seu CPF(somente número)\nr: ")).strip() # 123.456.789-89
        model_cpf = RegexSys.model_cpf(cpf)
        print('')

        if self.filtrar_cliente(model_cpf):
            print(Colors.BACK_PURPLE + "[-] Existe um cliente com esse CPF!" + Colors.END)
            print(self.filtrar_cliente(model_cpf))
            return
        
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