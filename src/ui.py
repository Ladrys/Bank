from db_factory import *

class UI:
    def __init__(self):
        self.factory = None

    def set_factory(self, factory):
        self.factory = factory
        
    def table_menu(self):
        while True:
            if self.factory is None:
                print("\nPlease select a table first.")
                break

            print(f"\n--- {self.factory.table_name} menu ---")
            print("1. Create new record")
            print("2. Read record details")
            print("3. Update record details")
            print("4. Delete record")
            print("5. Go back")
            choice = input("\nEnter your choice: ")

            if choice == "5":
                break

            if choice == "1":
                data = self.factory.get_input_data()  
                self.factory.create_record(*data)
                print("\nRecord created successfully!")
            elif choice == "2":
                record_id = int(input("Enter record ID: "))
                record = self.factory.read_record(record_id)
                if record:
                    for i, column in enumerate(self.factory.columns):
                        print(f"{column}: {record[i]}")
                else:
                    print("Record not found!")
            elif choice == "3":
                record_id = int(input("\nEnter record ID: "))
                record = self.factory.read_record(record_id)
                if record:
                    new_data = self.factory.get_input_data()  
                    self.factory.update_record(record_id, *new_data)
                    print("Record updated successfully!")
                else:
                    print("Record not found!")
            elif choice == "4":
                record_id = int(input("\nEnter record ID: "))
                if self.factory.delete_record(record_id):
                    print("Record deleted successfully!")
                else:
                    print("Record not found!")
            else:
                print("Invalid choice!")
