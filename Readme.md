Bankovní Aplikace - Readme

Vítejte v readme projektu Bankovní Aplikace. Tato readme poskytne přehled projektu, jeho struktury, a klíčových funkcí implementovaných v několika hlavních modulech.

    Struktura Projektu

Projekt je organizován následujícím způsobem:

    Banka/
    │
    ├── src/
        ├── db_connect.py
        ├── main.py
        ├── ui.py
        └── db_factory.py


Moduly

Modul db_connect.py obsahuje funkce pro navázání spojení s databází pomocí knihovny mysql.connector. Zajišťuje správu spojení s databází.


Hlavní modul main.py obsahuje spouštěcí kód aplikace. Zde můžete definovat uživatelské scénáře, volání funkcí z ostatních modulů a interakci s uživatelem.

Modul ui.py se stará o uživatelské rozhraní (UI) aplikace. Obsahuje třídu UI, která zajišťuje zobrazování informací a interakci s uživatelem přes příkazový řádek.

Modul db_factory.py obsahuje implementaci továrního vzoru pro vytváření objektů spojených s databází. Obsahuje třídy pro vytváření poboček, zaměstnanců, klientů, účtů a operací.
Nastavení

Pro správné fungování aplikace je třeba provést následující kroky:

    Stáhněte a nainstalujte MySQL s příslušnými adony.

    Vytvořte připojení k databázi na localhostu s následujícími parametry:
        Hostname: 127.0.0.1
        Port: 3306
        Uživatelské jméno: root
        Heslo: root

    Vytvořte nový SQL dotaz a zkopírujte obsah souboru export_struc.sql z adresáře sql do tohoto dotazu.

    Nejprve vytvořte a použijte databázi, poté vytvořte tabulky a nakonec můžete vložit data dle potřeby a spusťte SQL dotaz pro vytvoření pohledů.

Spuštění

Nyní jste připraveni spustit aplikaci. Otevřete terminál ve složce src v rámci projektu pomocí příkazu:

bash

cd Bank\src

A poté spusťte program příkazem:

python main.py

    Základní Funkce

Bankovní aplikace obsahuje několik základních funkcí pro práci s daty. Následují klíčové funkce pro každý modul:

Modul db_factory.py
BaseFactory

Třída BaseFactory slouží k vytváření, čtení, aktualizaci a mazání záznamů v tabulce databáze. Poskytuje následující metody:

    create_record(*data): Vytvoří nový záznam v tabulce.
    read_record(record_id): Přečte záznam podle zadaného ID.
    update_record(record_id, *new_data): Aktualizuje existující záznam.
    delete_record(record_id): Smaže záznam podle zadaného ID.
    get_input_data(): Získá uživatelský vstup pro vytvoření nebo aktualizaci záznamu.

Modul db_connect.py
DbConnection

Třída DbConnection zajišťuje spojení s databází. Je implementována jako singleton a poskytuje metody pro získání instance a práci s připojením.

Modul main.py
Main

Třída Main slouží jako vstupní bod aplikace. Obsahuje statickou metodu main, která spouští aplikaci. Tento modul se používá k inicializaci připojení k databázi a začátku interakce s uživatelem.

Modul ui.py
UI

Třída UI implementuje uživatelské rozhraní aplikace. Umožňuje uživatelům vytvářet, číst, aktualizovat a mazat záznamy v databázi prostřednictvím příkazového řádku. Třída UI obsahuje následující metody:

    set_factory(factory): Nastaví továrnu pro práci s konkrétní tabulkou.
    table_menu(): Zobrazuje hlavní menu pro výběr akce nad vybranou tabulkou. Umožňuje vytvářet, číst, aktualizovat a mazat záznamy, stejně jako se vrátit zpět do hlavního menu.

Výjimky

db_factory.py

 V tomto modulu jsou implementovány výjimky pro zpracování nesrovnalostí v datech a s databází.

db_connect.py

 Modul db_connect.py zajišťuje spojení s databází a může generovat výjimku v případě selhání spojení.

main.py

 V tomto modulu je vtupní bod do aplikace, ale výjimky zde nejsou implementovány.

ui.py

 Tento modul také neobsahuje implementaci výjimek, ale může generovat výjimky v případě, že uživatel zadal neplatnou volbu nebo pokud došlo k chybám při interakci s databází.

Závěr

Pro dokončení aplikace je třeba udělat několik věcí. Prvně, je důležité přidat zpracování výjimek. To znamená, že bychom měli řešit situace, kdy se něco nepovede, například při komunikaci s databází.

Dále by bylo rozumné přidat funkci přihlášení, aby se zajistilo, že pouze oprávnění uživatelé budou mít přístup k určitým akcím, jako je otevření účtu. Tím se zvýší bezpečnost a zamezí se nepovoleným operacím.

Celkově by mělo dojít k vylepšení uživatelského rozhraní, aby bylo snazší a příjemnější používat aplikaci. Tyto kroky by měly pomoci k tomu, aby aplikace lépe fungovala a byla více užitečná pro uživatele.

Autor

Jméno: Michal Ladra
Třída: C4b
Telefon: +420 773 615 534
Email: ladra@spsejecna.cz
Škola: SPŠE Ječná, Praha 2

Děkuji za použití mé aplikace a přeji vám úspěšné zvládnutí bankovních operací!
