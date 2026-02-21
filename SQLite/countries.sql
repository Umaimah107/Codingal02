CREATE TABLE Countries (
    Country_ID TEXT PRIMARY KEY,
    Country_Name TEXT,
    Continent TEXT,
    Popularity_Rank INTEGER,
    Population_Millions REAL,
    Famous_For TEXT
);

INSERT INTO Countries (Country_ID, Country_Name, Continent, Popularity_Rank, Population_Millions, Famous_For) VALUES
('C01', 'Pakistan', 'Asia', 7, 241.5, 'Mountains'),
('C02', 'France', 'Europe', 5, 67.8, 'Eiffel Tower'),
('C03', 'Japan', 'Asia', 4, 125.7, 'Technology'),
('C04', 'Brazil', 'South America', 6, 203.1, 'Amazon Forest'),
('C05', 'Canada', 'North America', 8, 38.2, 'Natural Beauty'),
('C06', 'Italy', 'Europe', 3, 59.1, 'Historic Sites'),
('C07', 'Australia', 'Australia', 9, 26.4, 'Beaches'),
('C08', 'Germany', 'Europe', 2, 83.2, 'Engineering'),
('C09', 'India', 'Asia', 1, 1428.6, 'Culture'),
('C10', 'Argentina', 'South America', 10, 45.8, 'Football');

SELECT * FROM Countries
WHERE Continent = 'Asia';

SELECT * FROM Countries
ORDER BY Popularity_Rank ASC;

SELECT * FROM Countries
WHERE Country_Name LIKE 'A%';

SELECT DISTINCT Continent FROM Countries;

SELECT Country_Name, Popularity_Rank
FROM Countries
WHERE Country_Name LIKE '%a%'
ORDER BY Popularity_Rank DESC;  