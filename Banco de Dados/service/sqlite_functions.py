import shutil, os
import sqlite3 as lite
from service import Colors, CurrentTime

class SQLITE_FUNCTIONS:
    def __init__(self) -> None:
        self._PATH = 'service/db/viagens.db'
        self._con = lite.connect(self._PATH)
        self._cur = self._con.cursor()

        # realizar backup
        self.backup_database()

        self.create_table_usuarios()
        self.create_table_destinos()
        self.create_table_reservas()

    def backup_database(self):
        db_file = "service/db/viagens.db"
        print(os.path.join("service/backup"))

        shutil.copy2(db_file, "service/backup")

        print(Colors.BACK_GREEN + "=== BACKUP DO BANCO DE DADOS FEITO COM SUCESSO ===" + Colors.END)
        print(Colors.GREEN + f"└── ({CurrentTime.created_at()})" + Colors.END)

    def create_table_usuarios(self):
        with self._con:
            try:
                self._cur.execute(
                """
                    CREATE TABLE IF NOT EXISTS usuarios(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome VARCHAR(255) NOT NULL,
                        email VARCHAR(100) NOT NULL UNIQUE,
                        endereco VARCHAR(50) NOT NULL,
                        data_nascimento DATE NOT NULL,
                        created_at Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                        updated_at Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                    )
                """
                )

                print(Colors.BACK_GREEN + "=== Tabela criada com sucesso ===" + Colors.END)
                print(Colors.GREEN + f"└──[TABELA `viagens.usuarios`] - ({CurrentTime.created_at()})" + Colors.END)

            except lite.OperationalError as error:
                print(Colors.BACK_RED + "=== `sqlite3.OperationalError` ===" + Colors.END)
                print(f"└──[{__name__}] - ({error})")
    
    def create_table_destinos(self):
        with self._con:
            try:
                self._cur.execute(
                """
                    CREATE TABLE IF NOT EXISTS destinos(
                        id INTEGER,
                        nome VARCHAR(255) NOT NULL,
                        descricao VARCHAR(255) NOT NULL
                    )
                """
                )

                print(Colors.BACK_GREEN + "=== Tabela criada com sucesso ===" + Colors.END)
                print(Colors.GREEN + f"└──[TABELA `viagens.destinos`] - ({CurrentTime.created_at()})" + Colors.END)

            except lite.OperationalError as error:
                print(Colors.BACK_RED + "=== `sqlite3.OperationalError` ===" + Colors.END)
                print(f"└──[{__name__}] - ({error})")

    def create_table_reservas(self):
        with self._con:
            try:
                self._cur.execute(
                """
                    CREATE TABLE IF NOT EXISTS reservas(
                        id INTEGER,
                        id_usuario INTEGER,
                        id_destino INTEGER,
                        status VARCHAR(255),
                        data DATE NOT NULL,
                        FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
                    )
                """
                )

                print(Colors.BACK_GREEN + "=== Tabela criada com sucesso ===" + Colors.END)
                print(Colors.GREEN + f"└──[TABELA `viagens.reservas`] - ({CurrentTime.created_at()})" + Colors.END)

            except lite.OperationalError as error:
                print(Colors.BACK_RED + "=== `sqlite3.OperationalError` ===" + Colors.END)
                print(f"└──[{__name__}] - ({error})")

    def criar_novo_usuario(self, usuario : list):
        with self._con:
            try:
                query = "INSERT INTO usuarios (nome, email, endereco, data_nascimento) VALUES (?, ?, ?, ?)"

                self._cur.execute(query, usuario)

                print(Colors.BACK_GREEN + "=== USUÁRIO CRIADO COM SUCESSO ===" + Colors.END)
                print(Colors.GREEN + f"└──[TABELA `viagens.usuarios`] '{usuario[0]}' INSERT - ({CurrentTime.created_at()})" + Colors.END)

            except lite.OperationalError as error:
                print(Colors.BACK_RED + "=== `sqlite3.OperationalError` ===" + Colors.END)
                print(f"└──[{__name__}] - ({error})")

            except lite.IntegrityError as error:
                print(Colors.BACK_RED + "=== `IntegrityError` ===" + Colors.END)
                print(f"└──[{__name__}] - ({error})")

    def criar_novo_destino(self, destino : list):
        with self._con:
            try:
                query = "INSERT INTO destinos (id, nome, descricao) VALUES (?, ?, ?)"

                self._cur.execute(query, destino)

                print(Colors.BACK_GREEN + "=== DESTINO CRIADO COM SUCESSO ===" + Colors.END)
                print(Colors.GREEN + f"└──[TABELA `viagens.destino`] '{destino[1]}' INSERT - ({CurrentTime.created_at()})" + Colors.END)

            except lite.OperationalError as error:
                print(Colors.BACK_RED + "=== `sqlite3.OperationalError` ===" + Colors.END)
                print(f"└──[{__name__}] - ({error})")

            except lite.IntegrityError as error:
                print(Colors.BACK_RED + "=== `IntegrityError` ===" + Colors.END)
                print(f"└──[{__name__}] - ({error})")

    def criar_nova_reserva(self, reserva: list):
        with self._con:
            try:
                query = "INSERT INTO reservas (id, id_usuario, id_destino, status, data) VALUES (?, ?, ?, ?, ?)"

                self._cur.execute(query, reserva)

                print(Colors.BACK_GREEN + "=== NOVA RESERVA CRIADA COM SUCESSO ===" + Colors.END)
                print(Colors.GREEN + f"└──[TABELA `viagens.reservas`] '{reserva}' INSERT - ({CurrentTime.created_at()})" + Colors.END)

            except lite.OperationalError as error:
                print(Colors.BACK_RED + "=== `sqlite3.OperationalError` ===" + Colors.END)
                print(f"└──[{__name__}] - ({error})")

            except lite.IntegrityError as error:
                print(Colors.BACK_RED + "=== `IntegrityError` ===" + Colors.END)
                print(f"└──[{__name__}] - ({error})")

    def ler_usuarios_viagens(self, table):
        try:
            with self._con:
                query = f"SELECT * FROM {table}"
                self._cur.execute(query)

                list_usuarios = self._cur.fetchall()

                print(list_usuarios)

        except lite.OperationalError as error:
            print(Colors.BACK_RED + "=== `sqlite3.OperationalError` ===" + Colors.END)
            print(f"└──[{__name__}] - ({error})")

        except lite.IntegrityError as error:
            print(Colors.BACK_RED + "=== `IntegrityError` ===" + Colors.END)
            print(f"└──[{__name__}] - ({error})")

    def atualizar(self, _id, email_update):
        try:
            with self._con:
                query = f"UPDATE usuarios SET email='{email_update}' WHERE id={_id}"
                self._cur.execute(query)

                print(Colors.BACK_GREEN + "=== ATUALIZAÇÃO FEITA COM SUCESSO! ===" + Colors.END)
                print(Colors.GREEN + f"└──[TABELA `viagens.usuarios`] '{email_update}' UPDATE - ({CurrentTime.created_at()})" + Colors.END)

        except lite.OperationalError as error:
            print(Colors.BACK_RED + "=== `sqlite3.OperationalError` ===" + Colors.END)
            print(f"└──[{__name__}] - ({error})")

        except lite.IntegrityError as error:
            print(Colors.BACK_RED + "=== `IntegrityError` ===" + Colors.END)
            print(f"└──[{__name__}] - ({error})")

    def deletar(self, _id):
        with self._con:
            query = f"DELETE FROM reservas WHERE id={_id}"
            self._cur.execute(query)
            print("deletado")