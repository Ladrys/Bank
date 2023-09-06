from db_connect import DbConnection
import mysql


from db_connect import DbConnection

class BaseFactory:
    def __init__(self, table_name, columns):
        self.db_conn = DbConnection.get_instance()
        self.table_name = table_name
        self.columns = columns

    def create_record(self, *data):
        cursor = self.db_conn.cursor()
        if len(data) != len(self.columns) - 1:
            print("Error: Number of data values does not match the number of columns.")
            return

        placeholders = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO {self.table_name} ({', '.join(self.columns[1:])}) VALUES ({placeholders})"
        cursor.execute(query, data)
        self.db_conn.connection.commit()
        cursor.close()

    def read_record(self, record_id):
        cursor = self.db_conn.cursor()
        cursor.execute(f"SELECT * FROM {self.table_name} WHERE {self.columns[0]} = %s", (record_id,))
        record = cursor.fetchone()
        cursor.close()
        return record if record else ()  

    def update_record(self, record_id, *new_data):
        cursor = self.db_conn.cursor()
        set_statements = ', '.join([f"{col} = %s" for col in self.columns[1:]])
        query = f"UPDATE {self.table_name} SET {set_statements} WHERE {self.columns[0]} = %s"
        cursor.execute(query, new_data + (record_id,))
        self.db_conn.connection.commit()
        cursor.close()

    def delete_record(self, record_id):
        cursor = self.db_conn.cursor()
        cursor.execute(f"DELETE FROM {self.table_name} WHERE {self.columns[0]} = %s", (record_id,))
        self.db_conn.connection.commit()
        row_count = cursor.rowcount  
        cursor.close()
        
        if row_count > 0:
            return True  
        else:
            return False  

    def get_input_data(self):
        data = []
        for column in self.columns[1:]:
            value = input(f"Enter {column}: ")
            data.append(value)
        return data
