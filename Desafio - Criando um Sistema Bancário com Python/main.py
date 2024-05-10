from colors import Colors
from datetime import datetime
class MEU_BANCO():

    def __init__(self) -> None:
        self._hora_atual = datetime.now().strftime("%H:%M")

        self.__extrato : str = ""
        self.__saldo : int = 0
        self.__limite : int = 500
        self.__numero_saques : int = 0
        self.__LIMITE_SAQUES : int = 3
        # --- vars ---

        self.__start : bool = True
        while self.__start:
            print(Colors.CYAN + "=== SEJA BEM-VINDO AO $BANCO CENTRAL$ ===" + Colors.END)
            self.__MENU_PRINCIPAL()

    def __MENU_PRINCIPAL(self) -> None:
        """
            Menu principal da aplicação com interação
        """

        print("""
        [ 1 ] Depositar
        [ 2 ] Saque
        [ 3 ] Extrato
        [ 4+ ] Sair
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

        else:
            self.__start = False

        print('\n' * 3)

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
            Módulo para mostrar o extrato do cliente
        """
        return f"{self.__extrato}" if len(self.__extrato) > 0 else "[x] Nenhuma função foi feita no momento..."
            
if __name__ == '__main__':
    try:
        MEU_BANCO()

    except ExceptionGroup:
        print(ExceptionGroup)

    finally:
        print("== APLICAÇÃO ENCERRADA! ==")