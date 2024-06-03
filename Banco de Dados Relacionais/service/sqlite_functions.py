import shutil, os
import sqlite3 as lite
from service import Colors, CurrentTime

class SQLITE_FUNCTIONS:
    def __init__(self) -> None:
        self._PATH = 'service/db/meu_banco.db'
        self._con = lite.connect(self._PATH)
        self._cur = self._con.cursor()

        # realizar backup
        self.backup_database()
        self.create_table()

    def backup_database(self):
        shutil.copy2(self._PATH, "service/backup")

        print(Colors.BACK_GREEN + "=== BACKUP DO BANCO DE DADOS FEITO COM SUCESSO ===" + Colors.END)
        print(Colors.GREEN + f"└── 'meu_banco.db' | ({CurrentTime.created_at()})" + Colors.END)

    def create_table(self):
        with self._con:
            try:
                self._cur.execute(
                """
                    CREATE TABLE IF NOT EXISTS clientes(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome VARCHAR(100),
                        email VARCHAR(150)
                    )
                """
                )

                print(Colors.BACK_GREEN + "=== Tabela criada com sucesso ===" + Colors.END)
                print(Colors.GREEN + f"└──[TABELA `meu_banco.clientes`] - ({CurrentTime.created_at()})" + Colors.END)

            except lite.OperationalError as error:
                print(Colors.BACK_RED + "=== `sqlite3.OperationalError` ===" + Colors.END)
                print(f"└──[{__name__}] - ({error})")

    def criar_novo_cliente(self, cliente : list):
        with self._con:
            try:
                query = "INSERT INTO clientes (nome, email) VALUES (?, ?)"

                self._cur.execute(query, cliente)
                # [inserir lotes de dados] -> self._cur.executemany()

                print(Colors.BACK_GREEN + "=== USUÁRIO CRIADO COM SUCESSO ===" + Colors.END)
                print(Colors.GREEN + f"└──[TABELA `meu_banco.clientes`] '{cliente[0]}' INSERT - ({CurrentTime.created_at()})" + Colors.END)

            except lite.OperationalError as error:
                print(Colors.BACK_RED + "=== `sqlite3.OperationalError` ===" + Colors.END)
                print(f"└──[{__name__}] - ({error})")

            except lite.IntegrityError as error:
                print(Colors.BACK_RED + "=== `IntegrityError` ===" + Colors.END)
                print(f"└──[{__name__}] - ({error})")

            finally:
                self._con.commit()

    def ler_clientes(self):
        try:
            with self._con:
                query = "SELECT * FROM clientes"
                self._cur.execute(query)

                list_clientes = self._cur.fetchall()

                return list_clientes

        except lite.OperationalError as error:
            print(Colors.BACK_RED + "=== `sqlite3.OperationalError` ===" + Colors.END)
            print(f"└──[{__name__}] - ({error})")

        except lite.IntegrityError as error:
            print(Colors.BACK_RED + "=== `IntegrityError` ===" + Colors.END)
            print(f"└──[{__name__}] - ({error})")

    def atualizar_cliente(self, _id, set_update : tuple):
        try:
            with self._con:
                query = "UPDATE clientes SET nome=?, email=? WHERE id=?"
                self._cur.execute(query, (set_update[0], set_update[1], _id,))

                print(Colors.BACK_GREEN + "=== ATUALIZAÇÃO FEITA COM SUCESSO! ===" + Colors.END)
                print(Colors.GREEN + f"└──[TABELA `clientes.db`] '{set_update}' UPDATE | ({CurrentTime.created_at()})" + Colors.END)

        except lite.OperationalError as error:
            print(Colors.BACK_RED + "=== `sqlite3.OperationalError` ===" + Colors.END)
            print(f"└──[{__name__}] - ({error})")

        except lite.IntegrityError as error:
            print(Colors.BACK_RED + "=== `IntegrityError` ===" + Colors.END)
            print(f"└──[{__name__}] - ({error})")

        finally:
            self._con.commit()

    def deletar_cliente(self, _id):
        try:
            with self._con:
                query = "DELETE FROM clientes WHERE id=?"
                
                self._cur.execute(query, (_id,))
                
                print(Colors.BACK_GREEN + "=== USUÁRIO DELETADO! ===" + Colors.END)
                print(Colors.GREEN + f"└──[TABELA `clientes.db`] DELETE | ({CurrentTime.created_at()})" + Colors.END)

        except lite.OperationalError as error:
            print(Colors.BACK_RED + "=== `sqlite3.OperationalError` ===" + Colors.END)
            print(f"└──[{__name__}] - ({error})")

        except lite.IntegrityError as error:
            print(Colors.BACK_RED + "=== `IntegrityError` ===" + Colors.END)
            print(f"└──[{__name__}] - ({error})")

        finally:
            self._con.commit()

    def recuperar_cliente(self, _id):
        try:
            with self._con:
                self._cur.row_factory = lite.Row

                query = "SELECT * FROM clientes WHERE id=?"
                self._cur.execute(query, (_id,))

                return self._cur.fetchone()


        except lite.OperationalError as error:
            print(Colors.BACK_RED + "=== `sqlite3.OperationalError` ===" + Colors.END)
            print(f"└──[{__name__}] - ({error})")

        except lite.IntegrityError as error:
            print(Colors.BACK_RED + "=== `IntegrityError` ===" + Colors.END)
            print(f"└──[{__name__}] - ({error})")