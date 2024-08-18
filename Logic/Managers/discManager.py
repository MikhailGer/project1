from Logic.Managers.DataBaseManager import DBManager


class DiscManager:
    def __init__(self):
        self.connection = DBManager()

    def getCurrentDiscID(self, id_or_name, mode):
        valid_columns = ['id', 'name']
        if mode not in valid_columns:
            raise ValueError(f"Invalid column name: {mode}")
        sql = f"SELECT id FROM public.disc WHERE {mode} = %s;"
        try:
            return self.connection.fetch_one(sql, (id_or_name,))
        except Exception as e:
            print(f"Ошибка получения текущего диска: {e}")
            return False

    def getDiscsList(self, mode='id'):
        valid_columns = ['id', 'name']
        if mode not in valid_columns:
            raise ValueError(f"Invalid column name: {mode}")

        sql = f"SELECT {mode} FROM public.disc;"
        try:
            results = self.connection.fetch_all(sql)
            return [disc[0] for disc in results]
        except Exception as e:
            print(f"Ошибка при получении списка дисков: {e}")
            return []

    def createNewDiscWithID(self, id, name, param_id):
        sql = """
        INSERT INTO disc (id, name, param_id, created_at)
        VALUES (%s, %s, %s, NOW())
        """
        values = (id, name, param_id)
        try:
            return self.connection.execute_query(sql, values)

        except Exception as e:
            print(f"Ошибка при создании нового диска: {e}")
            return False

    def createNewDiscWithName(self, name, param_id):
        sql = """
        INSERT INTO disc (name, param_id, created_at)
        VALUES (%s, %s, NOW())
        """
        values = (name, param_id)
        try:
            return self.connection.execute_query(sql, values)
        except Exception as e:
            print(f"Ошибка при создании нового диска: {e}")
            return False

    def getDiscParams(self, id):
        sql = """
                SELECT p.diameter, p.blade_distance, p.blade_force
                FROM disc d
                JOIN param p ON d.param_id = p.id
                WHERE d.id = %s
                """
        try:
            return self.connection.fetch_one(sql, (id,))
        except Exception as e:
            print(f"Ошибка поиска параметров диска: {e}")
            return None
    def deleteDisc(self, id_or_name, mode):
        valid_columns = ['id', 'name']
        if mode not in valid_columns:
            raise ValueError(f"Invalid column name: {mode}")
        sql = f"DELETE FROM public.disc WHERE {mode} = %s;"
        try:
            return self.connection.execute_query(sql, (id_or_name,))
        except Exception as e:
            print(f"Ошибка удаления диска: {e}")
            return False

    def close(self):
        self.connection.close()
