from db_factory import PobockyFactory, ZamestnanciFactory, UctyFactory, KlientFactory, OperaceFactory

class UI:
    def __init__(self):
        self.pobocky_factory = PobockyFactory()
        self.zamestnanci_factory = ZamestnanciFactory()
        self.ucty_factory = UctyFactory()
        self.klient_factory = KlientFactory()
        self.operace_factory = OperaceFactory()

    def menu(self):
        while True:
            print("\nWelcome to the bank application")
            print("1. Pobocky table")
            print("2. Zamestnanci table")
            print("3. Ucty table")
            print("4. Klient table")
            print("5. Operace table")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.pobocky_menu()
            elif choice == "2":
                self.zamestnanci_menu()
            elif choice == "3":
                self.ucty_menu()
            elif choice == "4":
                self.klient_menu()
            elif choice == "5":
                self.operace_menu()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")

    def pobocky_menu(self):
        while True:
            print("\n--- Pobocky menu ---")
            print("1. Create new pobocka")
            print("2. Read pobocka details")
            print("3. Update pobocka details")
            print("4. Delete pobocka")
            print("5. Go back")
            choice = input("\nEnter your choice: ")

            if choice == "1":
                nazev = input("\nEnter nazev: ")
                adresa = input("Enter adresa: ")
                self.pobocky_factory.create_pobocka(nazev, adresa)
                print("\nPobocka created successfully!")
            elif choice == "2":
                pobocka_id = int(input("Enter pobocka ID: "))
                pobocka = self.pobocky_factory.read_pobocka(pobocka_id)
                if pobocka:
                    print("ID: ", pobocka[0])
                    print("Nazev: ", pobocka[1])
                    print("Adresa: ", pobocka[2])
                else:
                    print("Pobocka not found!")
            elif choice == "3":
                pobocka_id = int(input("\nEnter pobocka ID: "))
                pobocka = self.pobocky_factory.read_pobocka(pobocka_id)
                if pobocka:
                    nazev = input("Enter new nazev: ")
                    adresa = input("Enter new adresa: ")
                    self.pobocky_factory.update_pobocka(pobocka_id, nazev, adresa)
                    print("Pobocka updated successfully!")
                else:
                    print("Pobocka not found!")
            elif choice == "4":
                pobocka_id = int(input("\nEnter pobocka ID: "))
                if self.pobocky_factory.delete_pobocka(pobocka_id):
                    print("Pobocka deleted successfully")
                else:
                    print("Pobocka not found!")
            elif choice == "5":
                break
            else:
                print("Invalid choice!")




    def zamestnanci_menu(self):
        while True:
            print("\n--- Zamestnanci menu ---")
            print("1. Create new zamestnanec")
            print("2. Read zamestnanec details")
            print("3. Update zamestnanec details")
            print("4. Delete zamestnanec")
            print("5. Go back")
            choice = input("\nEnter your choice: ")

            if choice == "1":
                pobocka_id = int(input("\nEnter Pobocka ID: "))
                ucet_id = int(input("Enter Ucet ID: "))
                jmeno = input("Enter jmeno: ")
                prijmeni = input("Enter prijmeni: ")
                self.zamestnanci_factory.create_zamestnanec(pobocka_id, ucet_id, jmeno, prijmeni)
                print("\nZamestnanec created successfully!")
            elif choice == "2":
                zamestnanec_id = int(input("Enter zamestnanec ID: "))
                zamestnanec = self.zamestnanci_factory.read_zamestnanec(zamestnanec_id)
                if zamestnanec:
                    print("ID: ", zamestnanec[0])
                    print("Pobocka ID: ", zamestnanec[1])
                    print("Ucet ID: ", zamestnanec[2])
                    print("Jmeno: ", zamestnanec[3])
                    print("Prijmeni: ", zamestnanec[4])
                else:
                    print("Zamestnanec not found!")
            elif choice == "3":
                zamestnanec_id = int(input("\nEnter zamestnanec ID: "))
                zamestnanec = self.zamestnanci_factory.read_zamestnanec(zamestnanec_id)
                if zamestnanec:
                    pobocka_id = input("Enter new Pobocka ID: ")
                    ucet_id = input("Enter new Ucet ID: ")
                    jmeno = input("Enter new jmeno: ")
                    prijmeni = input("Enter new prijmeni: ")
                    self.zamestnanci_factory.update_zamestnanec(zamestnanec_id, pobocka_id, ucet_id, jmeno, prijmeni)
                    print("Zamestnanec updated successfully!")
                else:
                    print("Zamestnanec not found!")
            elif choice == "4":
                zamestnanec_id = int(input("\nEnter zamestnanec ID: "))
                if self.zamestnanci_factory.delete_zamestnanec(zamestnanec_id):
                    print("Zamestnanec deleted successfully")
                else:
                    print("Zamestnanec not found!")
            elif choice == "5":
                break
            else:
                print("Invalid choice!") 




    def ucty_menu(self):
        while True:
            print("\n--- Ucty menu ---")
            print("1. Create new ucet")
            print("2. Read ucet details")
            print("3. Update ucet details")
            print("4. Delete ucet")
            print("5. Go back")
            choice = input("\nEnter your choice: ")

            if choice == "1":
                klient_id = int(input("\nEnter Klient ID: "))
                cislo_uctu = int(input("Enter cislo uctu: "))
                pocatecni_zustatek = int(input("Enter pocatecni zustatek: "))
                datum_vytvoreni = input("Enter datum vytvoreni (yyyy-mm-dd): ")
                self.ucty_factory.create_ucet(klient_id, cislo_uctu, pocatecni_zustatek, datum_vytvoreni)
                print("\nUcet created successfully!")
            elif choice == "2":
                ucet_id = int(input("Enter ucet ID: "))
                ucet = self.ucty_factory.read_ucet(ucet_id)
                if ucet:
                    print("ID: ", ucet[0])
                    print("Klient ID: ", ucet[1])
                    print("Cislo uctu: ", ucet[2])
                    print("Pocatecni zustatek: ", ucet[3])
                    print("Datum vytvoreni: ", ucet[4])
                else:
                    print("Ucet not found!")
            elif choice == "3":
                ucet_id = int(input("\nEnter ucet ID: "))
                ucet = self.ucty_factory.read_ucet(ucet_id)
                if ucet:
                    klient_id = input("Enter new Klient ID: ")
                    cislo_uctu = input("Enter new cislo uctu: ")
                    pocatecni_zustatek = input("Enter new pocatecni zustatek: ")
                    datum_vytvoreni = input("Enter new datum vytvoreni (yyyy-mm-dd): ")
                    self.ucty_factory.update_ucet(ucet_id, klient_id, cislo_uctu, pocatecni_zustatek, datum_vytvoreni)
                    print("Ucet updated successfully!")
                else:
                    print("Ucet not found!")
            elif choice == "4":
                ucet_id = int(input("\nEnter ucet ID: "))
                if self.ucty_factory.delete_ucet(ucet_id):
                    print("Ucet deleted successfully!")
                else:
                    print("Ucet not found!")
            elif choice == "5":
                break
            else:
                print("Invalid choice!") 

    def klient_menu(self):
        while True:
            print("\n--- Klient menu ---")
            print("1. Create new klient")
            print("2. Read klient details")
            print("3. Update klient details")
            print("4. Delete klient")
            print("5. Go back")
            choice = input("\nEnter your choice: ")

            if choice == "1":
                jmeno = input("\nEnter jmeno: ")
                prijmeni = input("Enter prijmeni: ")
                self.klient_factory.create_klient(jmeno, prijmeni)
                print("\nKlient created successfully!")
            elif choice == "2":
                klient_id = int(input("Enter klient ID: "))
                klient = self.klient_factory.read_klient(klient_id)
                if klient:
                    print("ID: ", klient[0])
                    print("Jmeno: ", klient[1])
                    print("Prijmeni: ", klient[2])
                else:
                    print("Klient not found!")
            elif choice == "3":
                klient_id = int(input("\nEnter klient ID: "))
                klient = self.klient_factory.read_klient(klient_id)
                if klient:
                    jmeno = input("Enter new jmeno: ")
                    prijmeni = input("Enter new prijmeni: ")
                    self.klient_factory.update_klient(klient_id, jmeno, prijmeni)
                    print("Klient updated successfully!")
                else:
                    print("Klient not found!")
            elif choice == "4":
                klient_id = int(input("\nEnter klient ID: "))
                if self.klient_factory.delete_klient(klient_id):
                    print("Klient deleted successfully!")
                else:
                    print("Klient not found!")
            elif choice == "5":
                break
            else:
                print("Invalid choice!")




    def operace_menu(self):
        while True:
            print("\n--- Operace menu ---")
            print("1. Create new operace")
            print("2. Read operace details")
            print("3. Update operace details")
            print("4. Delete operace")
            print("5. Go back")
            choice = input("\nEnter your choice: ")

            if choice == "1":
                zamestnanec_id = int(input("Enter Zamestnanec ID: "))
                ucet_id = int(input("Enter Ucet ID: "))
                typ_operace = input("Enter typ operace (Vklad/Vyber/Prevod): ")
                datum_operace = input("Enter datum operace (yyyy-mm-dd): ")
                cislo_zdroj_uctu = int(input("Enter cislo zdroj uctu: "))
                cislo_cil_uctu = int(input("Enter cislo cil uctu: "))
                castka = int(input("Enter castka: "))
                self.operace_factory.create_operace(zamestnanec_id, ucet_id, typ_operace, datum_operace, cislo_zdroj_uctu, cislo_cil_uctu, castka)
                print("\nOperace created successfully!")
            elif choice == "2":
                operace_id = int(input("Enter operace ID: "))
                operace = self.operace_factory.read_operace(operace_id)
                if operace:
                    print("ID: ", operace[0])
                    print("Zamestnanec ID: ", operace[1])
                    print("Ucet ID: ", operace[2])
                    print("Typ operace: ", operace[3])
                    print("Datum operace: ", operace[4])
                    print("Cislo zdroj uctu: ", operace[5])
                    print("Cislo cil uctu: ", operace[6])
                    print("Castka: ", operace[7])
                else:
                    print("Operace not found!")
            elif choice == "3":
                operace_id = int(input("\nEnter operace ID: "))
                operace = self.operace_factory.read_operace(operace_id)
                if operace:
                    zamestnanec_id = input("Enter new Zamestnanec ID : ")
                    ucet_id = input("Enter new Ucet ID : ")
                    typ_operace = input("Enter new typ operace : ")
                    datum_operace = input("Enter new datum operace : ")
                    cislo_zdroj_uctu = input("Enter new cislo zdroj uctu : ")
                    cislo_cil_uctu = input("Enter new cislo cil uctu : ")
                    castka = input("Enter new castka : ")
                    self.operace_factory.update_operace(operace_id, zamestnanec_id, ucet_id, typ_operace, datum_operace, cislo_zdroj_uctu, cislo_cil_uctu, castka)
                    print("Operace updated successfully!")
                else:
                    print("Operace not found!")
            elif choice == "4":
                operace_id = int(input("\nEnter operace ID: "))
                if self.operace_factory.delete_operace(operace_id):
                    print("Operace deleted successfully!")
                else:
                    print("Operace not found!")
            elif choice == "5":
                break
            else:
                print("Invalid choice!")                        