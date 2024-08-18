from Logic.Managers.DataBaseManager import DBManager


class ParameterManager:
    def __init__(self):
        self.connection = DBManager()

    def getParamtersIDList(self):
        sql = "SELECT id FROM public.param;"
        try:
            result = self.connection.fetch_all(sql)
            id_list = [row[0] for row in result]  # Преобразование списка кортежей в список значений
            return id_list
        except Exception as e:
            print(f"Ошибка при получении списка id: {e}")
            return None

    def getParam(self, id):
        try:
            sql = "SELECT diameter, blade_distance, blade_force, created_at FROM public.param WHERE id = %s;"
            return self.connection.fetch_one(sql, (id,))
        except Exception as e:
            print(f"Ошибка при получении параметра: {e}")

    def createNewParam(self, diameter, blade_distance, blade_force):
        sql = """
        INSERT INTO param (diameter, blade_distance, blade_force, created_at)
        VALUES (%s, %s, %s, NOW())
        """
        values = (diameter, blade_distance, blade_force)
        try:
            return self.connection.execute_query(sql, values)
        except Exception as e:
            print(f"Ошибка при создании нового параметра: {e}")
            return False

    def deleteParam(self, id):
        try:
            sql = "DELETE FROM public.param WHERE id = %s;"
            return self.connection.execute_query(sql, (id,))
        except Exception as e:
            print(f"Ошибка удаления параметра: {e}")
            return False


    def close(self):
        self.connection.close()
