create table Zamestnanec(
Zamestnanec_id int primary key not null auto_increment,
jmeno varchar(50),
prijmeni varchar(50)

);

create table Ucet(
Ucet_id int primary key not null auto_increment,
Zamestnanec_id int,
FOREIGN KEY (Zamestnanec_id) REFERENCES Zamestnanec(Zamestnanec_id),
Klient_id int,
FOREIGN KEY (Klient_id) REFERENCES Klient(Klient_id),
datum_vytvoreni date

);

create table Klient(
Klient_id int primary key not null auto_increment,
jmeno varchar(50),
prijmeni varchar(50),
telefoni_cislo int,
Operator_id int,
Tarif_id int,
FOREIGN KEY (Operator_id) REFERENCES operator(Operator_id),
FOREIGN KEY (Tarif_id) REFERENCES Tarif(Tarif_id),
pocatecni_kredit int
);

create table Hovor(
Hovor_id int primary key not null auto_increment,
cislo_volajciho int,
cislo_volaneho int,
datum_hovoru date,
delka_hovoru int,
Ucet_id int,
FOREIGN KEY (Ucet_id) REFERENCES Ucet(Ucet_id)
);
create table Tarif(
Tarif_id int primary key not null auto_increment,
nazev varchar(30)
);
create table Operator(
Operator_id int primary key not null auto_increment,
nazev enum('O2','Vodafone', 'T-Mobile')
);


SELECT jmeno , SUM(pocatecni_kredit) 
FROM Klient 
INNER JOIN Ucet  ON Klien.Klient_id = Ucet.Klient_id
WHERE Klient.jmeno = 'JmenoUzivatele'
GROUP BY Klient.jmeno;




CREATE VIEW TelefonniCislaMajitele AS
SELECT Klient.telefoni_cislo, Klient.jmeno, Tarif.nazev
FROM Klient
INNER JOIN Operator ON Klient.Operator_id = Operator.Operator_id
INNER JOIN Tarif ON Klient.Tarif_id = Tarif.Tarif_id
WHERE Operator.nazev = 'ZadanyOperator'
ORDER BY Tarif.nazev;