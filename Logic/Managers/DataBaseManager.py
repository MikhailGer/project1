import psycopg2
from config import host, user, password, db_name


class DBManager:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.connect_to_DB()

    def connect_to_DB(self):
        try:
            self.connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name,
            )
            self.cursor = self.connection.cursor()

        except Exception as _ex:
            print("Error while working with postgres", _ex)

    def execute_query(self, query, params=()):
        try:
            if self.connection.closed:
                self.connect_to_DB()
            self.cursor.execute(query, params)
            self.connection.commit()
            return True
        except Exception as _ex:
            print(f"Ошибка подключения к postgre{_ex}")
            return False

    def fetch_all(self, query, params=()):
        try:
            if self.connection.closed:
                self.connect_to_DB()
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except Exception as _ex:
            print("Ошибка подключения к postgre")

    def fetch_one(self, query, params=()):
        try:
            if self.connection.closed:
                self.connect_to_DB()
            self.cursor.execute(query, params)
            return self.cursor.fetchone()
        except Exception as _ex:
            print("Ошибка подключения к postgre")

    def fetch_many(self, query, size, params=()):
        try:
            if self.connection.closed:
                self.connect_to_DB()
            self.cursor.execute(query, params)
            return self.cursor.fetchmany(size)
        except Exception as _ex:
            print("Ошибка подключения к postgre")

    def status(self):
        try:
            if self.connection.closed:
                self.connect_to_DB()
            return self.cursor.statusmessage
        except Exception as _ex:
            print("Ошибка подключения к postgre")

    def close(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
        except Exception as _ex:
            print("Ошибка подключения")