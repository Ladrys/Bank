
from db_connect import DbConnection
import mysql


class PobockyFactory:
    def __init__(self):
        self.db_conn = DbConnection.get_instance()

    def create_pobocka(self, nazev, adresa):
        cursor = self.db_conn.cursor()
        query = "INSERT INTO Pobocky (nazev, adresa) VALUES (%s, %s)"
        cursor.execute(query, (nazev, adresa))
        self.db_conn.connection.commit()
        cursor.close()
        return True

    def read_pobocka(self, pobocka_id):
        cursor = self.db_conn.cursor()
        cursor.execute(
            "SELECT * FROM Pobocky WHERE Pobocka_id = %s",
            (pobocka_id,)
        )
        return cursor.fetchone()

    def update_pobocka(self, pobocka_id, nazev, adresa):
        cursor = self.db_conn.cursor()
        cursor.execute(
            "UPDATE Pobocky SET nazev = %s, adresa = %s WHERE Pobocka_id = %s",
            (nazev, adresa, pobocka_id)
        )
        self.db_conn.connection.commit()

    def delete_pobocka(self, pobocka_id):
        cursor = self.db_conn.cursor()
        cursor.execute("DELETE FROM Pobocky WHERE Pobocka_id = %s", (pobocka_id,))
        self.db_conn.connection.commit()
        cursor.close()
        return True


class ZamestnanciFactory:
    def __init__(self):
        self.db_conn = DbConnection.get_instance()

    def create_zamestnanec(self, pobocka_id, ucet_id, jmeno, prijmeni):
        cursor = self.db_conn.cursor()
        query = "INSERT INTO Zamestnanci (Pobocka_id, Ucet_id, jmeno, prijmeni) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (pobocka_id, ucet_id, jmeno, prijmeni))
        self.db_conn.connection.commit()
        cursor.close()
        return True

    def read_zamestnanec(self, zamestnanec_id):
        cursor = self.db_conn.cursor()
        cursor.execute(
            "SELECT * FROM Zamestnanci WHERE Zamestnanec_id = %s",
            (zamestnanec_id,)
        )
        return cursor.fetchone()

    def update_zamestnanec(self, zamestnanec_id, pobocka_id, ucet_id, jmeno, prijmeni):
        cursor = self.db_conn.cursor()
        cursor.execute(
            "UPDATE Zamestnanci SET Pobocka_id = %s, Ucet_id = %s, jmeno = %s, prijmeni = %s WHERE Zamestnanec_id = %s",
            (pobocka_id, ucet_id, jmeno, prijmeni, zamestnanec_id)
        )
        self.db_conn.connection.commit()

    def delete_zamestnanec(self, zamestnanec_id):
        cursor = self.db_conn.cursor()
        cursor.execute("DELETE FROM Zamestnanci WHERE Zamestnanec_id = %s", (zamestnanec_id,))
        self.db_conn.connection.commit()
        cursor.close()
        return True
    
class UctyFactory:
    def __init__(self):
        self.db_conn = DbConnection.get_instance()

    def create_ucet(self, klient_id, cislo_uctu, pocatecni_zustatek, datum_vytvoreni):
        cursor = self.db_conn.cursor()
        query = "INSERT INTO Ucty (Klient_id, cislo_uctu, pocatecni_zustatek, datum_vytvoreni) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (klient_id, cislo_uctu, pocatecni_zustatek, datum_vytvoreni))
        self.db_conn.connection.commit()
        cursor.close()
        return True

    def read_ucet(self, ucet_id):
        cursor = self.db_conn.cursor()
        cursor.execute(
            "SELECT * FROM Ucty WHERE Ucet_id = %s",
            (ucet_id,)
        )
        return cursor.fetchone()

    def update_ucet(self, ucet_id, klient_id, cislo_uctu, pocatecni_zustatek, datum_vytvoreni):
        cursor = self.db_conn.cursor()
        cursor.execute(
            "UPDATE Ucty SET Klient_id = %s, cislo_uctu = %s, pocatecni_zustatek = %s, datum_vytvoreni = %s WHERE Ucet_id = %s",
            (klient_id, cislo_uctu, pocatecni_zustatek, datum_vytvoreni, ucet_id)
        )
        self.db_conn.connection.commit()

    def delete_ucet(self, ucet_id):
        cursor = self.db_conn.cursor()
        cursor.execute("DELETE FROM Ucty WHERE Ucet_id = %s", (ucet_id,))
        self.db_conn.connection.commit()
        cursor.close()
        return True
class KlientFactory:
    def __init__(self):
        self.db_conn = DbConnection.get_instance()

    def create_klient(self, jmeno, prijmeni):
        cursor = self.db_conn.cursor()
        query = "INSERT INTO Klient (jmeno, prijmeni) VALUES (%s, %s)"
        cursor.execute(query, (jmeno, prijmeni))
        self.db_conn.connection.commit()
        cursor.close()
        return True

    def read_klient(self, klient_id):
        cursor = self.db_conn.cursor()
        cursor.execute(
            "SELECT * FROM Klient WHERE Klient_id = %s",
            (klient_id,)
        )
        return cursor.fetchone()

    def update_klient(self, klient_id, jmeno, prijmeni):
        cursor = self.db_conn.cursor()
        cursor.execute(
            "UPDATE Klient SET jmeno = %s, prijmeni = %s WHERE Klient_id = %s",
            (jmeno, prijmeni, klient_id)
        )
        self.db_conn.connection.commit()

    def delete_klient(self, klient_id):
        cursor = self.db_conn.cursor()
        cursor.execute("DELETE FROM Klient WHERE Klient_id = %s", (klient_id,))
        self.db_conn.connection.commit()
        cursor.close()
        return True
    
class OperaceFactory:
    def __init__(self):
        self.db_conn = DbConnection.get_instance()

    def create_operace(self, zamestnanec_id, ucet_id, typ_operace, datum_operace, cislo_zdroj_uctu, cislo_cil_uctu, castka):
        cursor = self.db_conn.cursor()
        query = "INSERT INTO Operace (Zamestnanec_id, Ucet_id, typ_operace, datum_operace, cislo_zdroj_uctu, cislo_cil_uctu, castka) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (zamestnanec_id, ucet_id, typ_operace, datum_operace, cislo_zdroj_uctu, cislo_cil_uctu, castka))
        self.db_conn.connection.commit()
        cursor.close()
        return True

    def read_operace(self, operace_id):
        cursor = self.db_conn.cursor()
        cursor.execute(
            "SELECT * FROM Operace WHERE Operace_id = %s",
            (operace_id,)
        )
        return cursor.fetchone()

    def update_operace(self, operace_id, zamestnanec_id, ucet_id, typ_operace, datum_operace, cislo_zdroj_uctu, cislo_cil_uctu, castka):
        cursor = self.db_conn.cursor()
        cursor.execute(
            "UPDATE Operace SET Zamestnanec_id = %s, Ucet_id = %s, typ_operace = %s, datum_operace = %s, cislo_zdroj_uctu = %s, cislo_cil_uctu = %s, castka = %s WHERE Operace_id = %s",
            (zamestnanec_id, ucet_id, typ_operace, datum_operace, cislo_zdroj_uctu, cislo_cil_uctu, castka, operace_id)
        )
        self.db_conn.connection.commit()

    def delete_operace(self, operace_id):
        cursor = self.db_conn.cursor()
        cursor.execute("DELETE FROM Operace WHERE Operace_id = %s", (operace_id,))
        self.db_conn.connection.commit()
        cursor.close()
        return True
