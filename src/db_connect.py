from mysql.connector import Error, MySQLConnection

class DbConnection:

    db_config = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': 'root',
        'database': 'bank'
    }

    __instance = None

    @staticmethod 
    def get_instance():
        """ Static access method. """
        if DbConnection.__instance is None:
            DbConnection()
        return DbConnection.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if DbConnection.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            DbConnection.__instance = self
            self.connection = self.connect()

    def connect(self):
        try:
            print("Connecting to MySQL database...")
            conn = MySQLConnection(**self.db_config)  

            if conn.is_connected():
                print("Connection established.")
                return conn
            else:  
                raise Exception("Connection failed.")

        except Error as error:
            print("Error connecting to MySQL database:", error)

    def cursor(self):
        try:
            return self.connection.cursor()
        except Error as error:
            print("Error creating cursor:", error)