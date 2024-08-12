from Managers.DataBaseManager import DBManager


class DiscScanManager:
    def __init__(self):
        self.db_connection = DBManager()

    def addScan(self, disc_id, is_training=bool):
        sql = """
           INSERT INTO disc_scan (disc_id, is_traning, is_current, created_at)
           VALUES (%s, %s, TRUE, NOW())
           """
        values = (disc_id, is_training)
        try:
            return self.db_connection.execute_query(sql, values)
        except Exception as e:
            print(f"Ошибка при создании нового сканирования диска: {e}")
            return False

    def getCurrentScanID(self):
        sql = f"SELECT id FROM public.disc_scan WHERE is_current = TRUE;"
        try:
            return self.db_connection.fetch_one(sql)[0]
        except Exception as e:
            print(f"Ошибка при получении текущего сканирования: {e}")
            return []

    def NotCurrentYet(self):
        sql = f"UPDATE public.disc_scan SET is_current = FALSE WHERE is_current = TRUE;"
        try:
            results = self.db_connection.execute_query(sql)
            return True
        except Exception as e:
            print(f"Ошибка при получении текущего сканирования: {e}")
            return False

    def getScanIDList(self, disc_id):
        sql = f"SELECT id FROM public.disc_scan WHERE disc_id = %s;"
        try:
            results = self.db_connection.fetch_all(sql)
            return [disc_scan[0] for disc_scan in results]
        except Exception as e:
            print(f"Ошибка при получении списка сканирований дисков: {e}")
            return []

    def deleteScan(self, disc_id):
        sql = """
           DELETE FROM public.disc_scan
	       WHERE disc_id = %s;
           """
        try:
            return self.db_connection.execute_query(sql, disc_id)

        except Exception as e:
            print(f"Ошибка при удалении сканирования диска: {e}")
            return False

    def deleteCurrentScan(self):
        sql = """
                   DELETE FROM public.disc_scan
        	       WHERE is_current = TRUE;
                   """
        try:
            return self.db_connection.execute_query(sql)

        except Exception as e:
            print(f"Ошибка при удалении сканирования диска: {e}")
            return False

    def close(self):
        self.db_connection.close()

