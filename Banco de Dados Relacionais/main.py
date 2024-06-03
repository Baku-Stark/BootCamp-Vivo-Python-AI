from service import Colors, OperationalSys
from service.sqlite_functions import SQLITE_FUNCTIONS

class Main(SQLITE_FUNCTIONS):
    """
        Main class app.
    """

    def __init__(self) -> None:
        super().__init__()
        #self.criar_novo_cliente(["Wallace", "wallace@email.com"])
        #self.criar_novo_cliente(["Satoru Gojo", "gojo@jujutsu.com"])
        #self.criar_novo_cliente(["Roronoa Zoro", "zoro@one_piece.com"])
        
        print('=*=' * 50)
        
        print("ID \t Nome \t\t Email")
        print('-' * 50)

        rec = self.recuperar_cliente(1)
        cliente = dict(rec)
        print(f"{cliente['id']} \t {cliente['nome']} \t {cliente['email']}")

        print('-' * 50)
        print('')
        print('=*=' * 50)

OperationalSys.clean_console()
Main()