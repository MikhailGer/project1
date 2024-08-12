from Managers.DataBaseManager import DBManager


class BladeManager:
    def __init__(self):
        self.db_connection = DBManager()

    def addBlade(self, disc_scan_id, num, scan, prediction):
        sql = """
                   INSERT INTO blade (disc_scan_id, num, scan, prediction,created_at)
                   VALUES (%s, %s, %s, %s, TRUE, NOW())
                   """
        values = (disc_scan_id, num, scan, prediction)
        try:
            return self.db_connection.execute_query(sql, values)
        except Exception as e:
            print(f"Ошибка при добавлении лезвия: {e}")
            return False

    def getBladeList(self, disc_scan_id):
        sql = """
                   SELECT id, disc_scan_id, num, scan, prediction, created_at
	FROM public.blade WHERE disc_scan_id = %s;
                   """
        try:
            return self.db_connection.fetch_all(sql, disc_scan_id)
        except Exception as e:
            print(f"Ошибка при получении списка лезвий: {e}")
            return False

    def getBlade(self, blade_id):
        sql = """
                           SELECT id, disc_scan_id, num, scan, prediction, created_at
        	FROM public.blade WHERE id = %s;
                           """
        try:
            return self.db_connection.fetch_one(sql, blade_id)
        except Exception as e:
            print(f"Ошибка при получении лезвия: {e}")
            return False


    def close(self):
        self.connection.close()