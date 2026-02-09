CREATE TABLE STAFF (
    STAFF_ID TEXT,
    FULL_NAME TEXT,
    TEAM_ID TEXT,
    SUPERVISOR_ID TEXT,
    PAY REAL
);

INSERT INTO STAFF (STAFF_ID, FULL_NAME, TEAM_ID, SUPERVISOR_ID, PAY) VALUES
('301', 'AHMED ALI', 'A1', '301',18000),
('302', 'ZARA KHAN', 'A1', '301',15000),
('303', 'OMAR FAROOQ', 'B1', '302',9000),
('304', 'MAHAM NOOR', 'B1', '302',9500),
('305', 'DANISH IQBAL', 'C1', '301',7000),
('306', 'SANA RIAZ', 'A1', '301',12000),
('307', 'HAMMAD SHAH', 'C1', '305',6500),
('308', 'LAIBA ANWAR', 'B1', '302',10000);

SELECT team_id AS "Team Code",
    COUNT(*) AS "No of Staff"
FROM STAFF
GROUP BY team_id;

SELECT team_id, SUM(pay)
FROM STAFF
GROUP BY team_id;

SELECT team_id AS "Team Code",
    COUNT(*) AS "No of Staff",
    SUM(pay) AS "Total Pay"
FROM STAFF
GROUP BY team_id;

SELECT team_id AS "Team Code",
    SUM(pay) AS "Total Pay"
FROM STAFF
WHERE SUPERVISOR_ID = "302"
GROUP BY team_id;

SELECT team_id, COUNT(*) AS "No of Staff"
FROM STAFF
GROUP BY team_id
HAVING COUNT(*) > 2;
