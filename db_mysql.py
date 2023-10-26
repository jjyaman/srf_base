import pymysql

class DataBaseMySQL:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "srf"
        self.connection = None

    def connect(self):
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conexión exitosa a la base de datos.")
        except pymysql.Error as e:
            print(f"Error de conexión: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada.")

    def select_all_from_table(self, table_name):
        if not self.connection:
            print("No hay conexión a la base de datos.")
            return

        try:
            with self.connection.cursor() as cursor:
                query = f"SELECT * FROM {table_name}"
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except pymysql.Error as e:
            print(f"Error al realizar la consulta: {e}")

    def insert_into_vector(self, table_name, vector):
        if not self.connection:
            print("No hay conexión a la base de datos.")
            return

        try:
            with self.connection.cursor() as cursor:
                query = f"INSERT INTO {table_name} (numero_documento, tipo_documento, nombre_completo, apellido_completo, rostro, genero) VALUES (1128, 123, 'Juan', 'Fernandez', '{vector}', 'Maculino')"
                cursor.execute(query)
                self.connection.commit()
                print("Inserción realizada correctamente")
        except pymysql.Error as e:
            print(f"Error al realizar la inserción: {e}")

    def select_vector_from_table(self, table_name, id):
        if not self.connection:
            print("No hay conexión a la base de datos.")
            return
        try:
            with self.connection.cursor() as cursor:
                query = f"SELECT rostro FROM {table_name} WHERE numero_documento = {id}"
                cursor.execute(query)
                result = cursor.fetchone()
                return result
        except pymysql.Error as e:
            print(f"Error al realizar la consulta: {e}")
