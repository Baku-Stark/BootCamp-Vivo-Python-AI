from service import Colors, OperationalSys
from service.sqlite_functions import SQLITE_FUNCTIONS

class Main():
    def __init__(self) -> None:
        sql_func = SQLITE_FUNCTIONS()
        #sql_func.backup_database()

        # nome (STRING), email [STRING], endereco [STRING], data_nascimento [STRING (ANO-DIA-MES)]
        #sql_func.criar_novo_usuario(["Wallace", "wallace@email.com", "Rio de Janeiro - Brazil", "2000-07-07"])
        

        # id [INT], nome [STRING], descricao [STRING] 
        #sql_func.criar_novo_destino([1, "Toronto - Canada", "Viajar para o Canada e fazer uma visitar aos melhores lugares"])
        

        # id [INT], id_usuario [INT], id_destino [INT], status [STRING], data [STRING (ANO-DIA-MES)]
        #sql_func.criar_nova_reserva([1, 1, 1, "pendente", "2028-12-12"])
        
        sql_func.ler_usuarios_viagens("usuarios")

OperationalSys.clean_console()
Main()