from db_connect import DbConnection
from db_factory import BaseFactory
from ui import UI

class Main:
    @staticmethod
    def main():
        db_conn = DbConnection.get_instance()
        connection = db_conn.connection
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE()")
        result = cursor.fetchone()
        print("Connected to database: ", result)

if __name__ == "__main__":
            db_conn = DbConnection.get_instance()
            connection = db_conn.connection
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE()")
            result = cursor.fetchone()
            print("Connected to database: ", result)
            
            factories = {
                "Pobocky": BaseFactory("Pobocky", ["Pobocka_id", "nazev", "adresa"]),
                "Zamestnanci": BaseFactory("Zamestnanci", ["Zamestnanec_id", "Pobocka_id", "Ucet_id", "jmeno", "prijmeni"]),
                "Ucty": BaseFactory("Ucty", ["Ucet_id", "Klient_id", "cislo_uctu", "pocatecni_zustatek", "datum_vytvoreni"]),
                "Klient": BaseFactory("Klient", ["Klient_id", "jmeno", "prijmeni"]),
                "Operace": BaseFactory("Operace", ["Operace_id", "Zamestnanec_id", "Ucet_id", "typ_operace", "datum_operace", "cislo_zdroj_uctu", "cislo_cil_uctu", "castka"])
            }

            while True:
                print("\nSelect a table to work with:")
                for i, table_name in enumerate(factories.keys(), start=1):
                    print(f"{i}. {table_name}")

                choice = input("\nEnter the number of your choice (or 'q' to quit): ")

                if choice == 'q':
                    break

                try:
                    choice = int(choice)
                    if 1 <= choice <= len(factories):
                        selected_table = list(factories.keys())[choice - 1]
                        ui = UI()
                        ui.set_factory(factories[selected_table])
                        ui.table_menu()
                    else:
                        print("Invalid choice. Please select a valid number.")
                except ValueError:
                    print("Invalid input. Please enter a valid number or 'q' to quit.")
