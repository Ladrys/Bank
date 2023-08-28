create database bank;
use bank;

create table Pobocky(
Pobocka_id int primary key not null auto_increment,
nazev varchar(50),
adresa varchar(50)
);

create table Zamestnanci(
Zamestnanec_id int primary key not null auto_increment,
Pobocka_id int,
FOREIGN KEY (Pobocka_id) REFERENCES Pobocky(Pobocka_id),
Ucet_id int,
FOREIGN KEY (Ucet_id) REFERENCES Ucty(Ucet_id),
jmeno varchar(50),
prijmeni varchar(50)

);

create table Ucty(
Ucet_id int primary key not null auto_increment,
Klient_id int,
FOREIGN KEY (Klient_id) REFERENCES Klient(Klient_id),
cislo_uctu int,
pocatecni_zustatek int,
datum_vytvoreni date

);

create table Klient(
Klient_id int primary key not null auto_increment,
jmeno varchar(50),
prijmeni varchar(50)
);

create table Operace(
Operace_id int primary key not null auto_increment,
Zamestnanec_id int,
FOREIGN KEY (Zamestnanec_id) REFERENCES Zamestnanci(Zamestnanec_id),
Ucet_id int,
FOREIGN KEY (Ucet_id) REFERENCES Ucty(Ucet_id),
typ_operace enum('Vklad', 'Vyber','Prevod'),
datum_operace date,
cislo_zdroj_uctu int,
cislo_cil_uctu int,
castka int
);

create view soucet_zustatku AS
SELECT SUM(pocatecni_zustatek) 
FROM Ucty
WHERE Klient_id = 1;

SELECT * FROM soucet_zustatku;

create view soucet_transakci AS
SELECT SUM(castka) 
FROM Operace
WHERE Zamestnanec_id = 1;

SELECT * FROM soucet_transakci;

