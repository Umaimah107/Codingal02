CREATE TABLE COMPANIES1 (
    COMP_NAME TEXT PRIMARY KEY,
    YEARLY_CUSTOMERS TEXT,
    POPULARITY TEXT,
    PROFIT TEXT,
    PLACE TEXT
);

INSERT INTO COMPANIES1 (COMP_NAME, YEARLY_CUSTOMERS, POPULARITY, PROFIT, PLACE) VALUES
('McDonalds','24.8 billion','12 to 13%','2 billion','America'),
('KFC','4.4 billion','2nd largest fast food chain','2 billion','America'),
('Cinnabon','189 million','Popular bakery food chain','1 billion','Pakistan'),
('Gloria Jeans','11 million','Mid level global coffee brand','203 million','America');

SELECT * FROM COMPANIES1;

SELECT * FROM COMPANIES1
WHERE PROFIT = '2 billion' AND PLACE = 'America';

SELECT * FROM COMPANIES1
WHERE PLACE = 'America' OR POPULARITY = '12 to 13%';
