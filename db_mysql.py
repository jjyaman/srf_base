import pymysql

class DataBaseMySQL:

    # Parámetros para establecer la conexión
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "srf"
        self.connection = None

    # Método para establecer la conexión con la Base de Datos
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

    # Método para terminar la conexión con la Base de Datos
    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada.")

    # Método para seleccionar todos los campos de un registro de una tabla, filtrados por ID
    def select_all_from_table(self, table_name, id):
        if not self.connection:
            print("No hay conexión a la base de datos.")
            return

        try:
            with self.connection.cursor() as cursor:
                query = f"SELECT * FROM {table_name} WHERE numero_documento = {id}"
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except pymysql.Error as e:
            print(f"Error al realizar la consulta: {e}")
    
    # Método para realizar la inserción de datos en una tabla
    def insert_into_vector(self, table_name, num_doc, name, last_name, vector, genero):
        if not self.connection:
            print("No hay conexión a la base de datos.")
            return

        try:
            with self.connection.cursor() as cursor:
                query = f"INSERT INTO {table_name} (numero_documento, tipo_documento, nombre_completo, apellido_completo, rostro, genero) VALUES ('{num_doc}', 123, '{name}', '{last_name}', '{vector}', '{genero}')"
                cursor.execute(query)
                self.connection.commit()
                print("Inserción realizada correctamente")
        except pymysql.Error as e:
            print(f"Error al realizar la inserción: {e}")

    # Método para seleccionar el rostro de un registro filtrado por ID
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

    # Método para extraer campos especificos de todos los registros en una tabla
    def select_all_register_from_table(self, columna1, columna2, table):
        if not self.connection:
            print("No hay conexión a la base de datos.")
            return
        try:
            with self.connection.cursor() as cursor:
                query = f"SELECT {columna1}, {columna2} FROM {table}"
                cursor.execute(query)
                return cursor
        except pymysql.Error as e:
            print(f"Error al realizar la consulta: {e}")
