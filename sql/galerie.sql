-- Vytvoření tabulky "Galerie"
CREATE TABLE Galerie (
    galerie_id INT AUTO_INCREMENT PRIMARY KEY,
    nazev_galerie VARCHAR(255),
    adresa VARCHAR(255),
    telefon VARCHAR(20)
);

-- Vytvoření tabulky "Maliri"
CREATE TABLE Maliri (
    malir_id INT AUTO_INCREMENT PRIMARY KEY,
    jmeno_malire VARCHAR(255),
    styl_malire VARCHAR(255)
);

-- Vytvoření tabulky "Obrazy"
CREATE TABLE Obrazy (
    obraz_id INT AUTO_INCREMENT PRIMARY KEY,
    nazev_obrazu VARCHAR(255),
    rok_vytvoreni INT,
    malir_id INT,
    styl_malby VARCHAR(255),
    FOREIGN KEY (malir_id) REFERENCES Maliri(malir_id)
);

-- Vytvoření tabulky "Zapujcky"
CREATE TABLE Zapujcky (
    zapujcka_id INT AUTO_INCREMENT PRIMARY KEY,
    obraz_id INT,
    galerie_id INT,
    datum_od DATE,
    datum_do DATE,
    FOREIGN KEY (obraz_id) REFERENCES Obrazy(obraz_id),
    FOREIGN KEY (galerie_id) REFERENCES Galerie(galerie_id)
);

-- Výpis všech uměleckých stylů, ve kterých maloval zadaný malíř
SELECT DISTINCT styl_malby
FROM Obrazy
WHERE malir_id = [ID_malire];

-- Výpis všech malířů a jejich obrazů, kteří malovali v určitém zadaném stylu
SELECT Maliri.jmeno_malire, Obrazy.nazev_obrazu
FROM Maliri
JOIN Obrazy ON Maliri.malir_id = Obrazy.malir_id
WHERE Obrazy.styl_malby = '[Zadany_styl]';

-- Výpis všech obrazů, zapůjčených k určitému datu podle galerií
SELECT Obrazy.nazev_obrazu, Galerie.nazev_galerie
FROM Zapujcky
JOIN Obrazy ON Zapujcky.obraz_id = Obrazy.obraz_id
JOIN Galerie ON Zapujcky.galerie_id = Galerie.galerie_id
WHERE '[Zadane_datum]' BETWEEN Zapujcky.datum_od AND Zapujcky.datum_do;

-- Výpis všech obrazů (včetně malíře a stylu), které si lze zapůjčit (nejsou teď půjčené)
SELECT Obrazy.nazev_obrazu, Maliri.jmeno_malire, Obrazy.styl_malby
FROM Obrazy
LEFT JOIN Zapujcky ON Obrazy.obraz_id = Zapujcky.obraz_id
WHERE Zapujcky.zapujcka_id IS NULL OR '[Zadane_datum]' > Zapujcky.datum_do;