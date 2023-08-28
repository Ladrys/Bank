Bankovní Aplikace - README

Vítejte v dokumentaci projektu Bankovní Aplikace. Tento README soubor obsahuje podrobný popis projektu, jeho strukturu, použité moduly, funkce a jak jej nastavit a spustit.

Popis Projektu

Projekt Bankovní Aplikace je implementací aplikace pro správu bankovních operací. Aplikace umožňuje spravovat informace o pobočkách, zaměstnancích, klientech, účtech a operacích.¨

Struktura Projektu

Projekt je organizován následujícím způsobem:


Banka/src/
│
├── db_connect.py
├── main.py
├── ui.py
└── db_factory.py

Moduly
db_connect.py

Modul db_connect.py obsahuje funkci pro navázání spojení s databází pomocí knihovny mysql.connector.

main.py

Hlavní modul main.py obsahuje spouštěcí kód aplikace. Zde můžete definovat uživatelské scénáře, volání funkcí z ostatních modulů a interakci s uživatelem.

ui.py

Modul ui.py se stará o uživatelské rozhraní (UI) aplikace. Obsahuje třídu UI, která zajišťuje zobrazování informací a interakci s uživatelem přes příkazový řádek.

db_factory.py

Modul db_factory.py obsahuje implementaci továrního vzoru pro vytváření objektů spojených s databází. Obsahuje třídy pro vytváření poboček, zaměstnanců, klientů, účtů a operací.

Použití

    Stáhněte a nainstalujte MySQL s příslušnými adony.
    Vytvořte připojení k localhostu s následujícími parametry:
        Hostname: 127.0.0.1
        Port: 3306
        Uživatelské jméno: root
        Heslo: root

    Vytvořte nový SQL dotaz a zkopírujte obsah souboru export_struc.sql z adresáře sql do tohoto dotazu.
    Nejprve vytvořte a použijte databázi, poté vytvořte tabulky a nakonec můžete vložit data dle potřeby a spusťte SQL dotaz pro vytvoření pohledů.

Nyní jste připraveni spustit aplikaci. Otevřete terminál ve složce src v rámci projektu pomocí příkazu:


cd Bank\src

A poté spusťte program příkazem:

python main.py




Základní Funkce

Bankovní aplikace obsahuje několik základních funkcí pro práci s daty:
Klienti

    create_klient(jmeno, prijmeni): Vytvoří nového klienta a vloží ho do tabulky "Klient".
    read_klient(klient_id): Získá záznam o klientovi podle ID z tabulky "Klient".
    update_klient(klient_id, jmeno, prijmeni): Aktualizuje informace o existujícím klientovi v tabulce "Klient".
    delete_klient(klient_id): Odstraní klienta z tabulky "Klient".

Pobočky

    create_pobocka(nazev, adresa): Vytvoří novou pobočku a vloží ji do tabulky "Pobocky".
    read_pobocka(pobocka_id): Získá záznam o pobočce podle ID z tabulky "Pobocky".
    update_pobocka(pobocka_id, nazev, adresa): Aktualizuje informace o existující pobočce v tabulce "Pobocky".
    delete_pobocka(pobocka_id): Odstraní pobočku z tabulky "Pobocky".

Zaměstnanci

    create_zamestnanec(pobocka_id, ucet_id, jmeno, prijmeni): Vytvoří nového zaměstnance a vloží ho do tabulky "Zamestnanci".
    read_zamestnanec(zamestnanec_id): Získá záznam o zaměstnanci podle ID z tabulky "Zamestnanci".
    update_zamestnanec(zamestnanec_id, pobocka_id, ucet_id, jmeno, prijmeni): Aktualizuje informace o existujícím zaměstnanci v tabulce "Zamestnanci".
    delete_zamestnanec(zamestnanec_id): Odstraní zaměstnance z tabulky "Zamestnanci".

Účty

    create_ucet(klient_id, cislo_uctu, pocatecni_zustatek, datum_vytvoreni): Vytvoří nový účet a vloží ho do tabulky "Ucty".
    read_ucet(ucet_id): Získá záznam o účtu podle ID z tabulky "Ucty".
    update_ucet(ucet_id, klient_id, cislo_uctu, pocatecni_zustatek, datum_vytvoreni): Aktualizuje informace o existujícím účtu v tabulce "Ucty".
    delete_ucet(ucet_id): Odstraní účet z tabulky "Ucty".

Operace

    create_operace(zamestnanec_id, ucet_id, typ_operace, datum_operace, cislo_zdroj_uctu, cislo_cil_uctu, castka): Vytvoří novou operaci a vloží ji do tabulky "Operace".
    read_operace(operace_id): Získá záznam o operaci podle ID z tabulky "Operace".
    update_operace(operace_id, zamestnanec_id, ucet_id, typ_operace, datum_operace, cislo_zdroj_uctu, cislo_cil_uctu, castka): Aktualizuje informace o existující operaci v tabulce "Operace".
    delete_operace(operace_id): Odstraní operaci z tabulky "Operace".

Tyto základní funkce umožňují vytvářet, číst, aktualizovat a mazat záznamy v různých tabulkách v rámci bankovní aplikace. Každá funkce je zaměřena na specifickou část databáze, a tím umožňuje efektivně spravovat informace o klientech, pobočkách, zaměstnancích, účtech a operacích.


Program vyžaduje ošetření několika výjimek. Dále je potřeba pro lepší zabezpečení aplikace dodělat login, který poskytne přihlášeným uživatelům práva k manipulaci s konkréními tabulkami. 
Např. klient který chce otevřít účet, ho neotevre, ale otevře ho zaměstnanec a až pak může dělat crud funkce na přeposílání peněz. 






Autor

    Jméno: Michal Ladra
    Třída: C4b
    Telefon: +420 773 615 534
    Email: ladra@spsejecna.cz
    Škola: SPŠE Ječná, Praha 2

Děkuji za použití mé aplikace a přeji vám úspěšné zvládnutí bankovních operací!
