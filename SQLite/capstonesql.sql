CREATE TABLE Salesman3(
    Salesman_id TEXT PRIMARY KEY,
    NAME TEXT,
    CITY TEXT,
    COMISSION TEXT
);

INSERT INTO Salesman3(Salesman_id, NAME, CITY, COMISSION)VALUES
('5001','James Hoog','New York','0.15'),
('5002','Nail Kite','Paris','0.13'),
('5005','Pit Alex','London','0.11'),
('5006','Mc Lyon','Paris','0.14'),
('5007','Paul Adam','Rome','0.13'),
('5003','Lauson Hen','San Jose','0.12');

CREATE TABLE Customer1(
customer_id TEXT,
CUST_NAME TEXT PRIMARY KEY,
CITY TEXT,
GRADE TEXT,
Salesman_id TEXT
);

INSERT INTO Customer1(customer_id, CUST_NAME, CITY, GRADE, Salesman_id)VALUES
('3002','NICK RAMANDO','NEW YORK','100','5001'),
('3007','BRAD DAVIS','CALIFORNIA','200','5001'),
('3005','GRAHAM ZUSI','LONDON','200','5002'),
('3008','JULIAN GREEN','LONDON','300','5002'),
('3004','FABIAN JOHNSON','PARIS','300','5006'),
('3009','GEOFF CAMERON','BERLIN','100','5007'),
('3003','JOZY ALTIDIOR','MOSCOW','200','5007'),
('3001','BRAD GUZAN','LONDON','','5005');

CREATE TABLE Orders4(
    ORD_NO TEXT PRIMARY KEY,
    PURCH_AMT TEXT,
    ORD_DATE TEXT,
    customer_id text,
    Salesman_id TEXT
);

INSERT INTO Orders4(ORD_NO, PURCH_AMT, ORD_DATE, customer_id, Salesman_id)VALUES
('70001','150.5','2012-10-05','3005','5002'),
('70009','270.65','2012-09-10','3001','5001'),
('70002','65.26','2012-10-05','3002','5003'),
('70004','110.5','2012-08-17','3009','5007'),
('70007','948.5','2012-09-10','3005','5005'),
('70005','2400.6','2012-07-27','3007','5006');

SELECT Customer1.CUST_NAME,Salesman3.NAME, Salesman3.CITY
FROM Customer1
JOIN Salesman3 ON Customer1.CITY= Salesman3.CITY;

SELECT Customer1.CUST_NAME, Salesman3.NAME
FROM Customer1
JOIN Salesman3 ON Customer1.Salesman_id = Salesman3.Salesman_id;

SELECT Orders4.ORD_NO,Customer1.CUST_NAME, Orders4.customer_id,Orders4.Salesman_id
FROM Orders4
JOIN Customer1 ON Orders4.customer_id = Customer1.customer_id
JOIN Salesman3 ON Orders4.Salesman_id = Salesman3.Salesman_id
WHERE Customer1.CITY <> Salesman3.CITY;

SELECT Orders4.ORD_NO, Customer1.CUST_NAME
FROM Orders4
JOIN Customer1 ON Orders4.customer_id = Customer1.customer_id;

SELECT Customer1.CUST_NAME AS 'Customer', Customer1.GRADE AS "Grade"
FROM Orders4
JOIN Salesman3 ON Orders4.Salesman_id = Salesman3.Salesman_id
JOIN Customer1 ON Orders4.customer_id = Customer1.customer_id
WHERE Customer1.GRADE IS NOT NULL;

SELECT Customer1.CUST_NAME AS "Customer", Customer1.city AS "City", Salesman3.NAME AS "Salesman", Salesman3.COMISSION
FROM Customer1
JOIN Salesman3 ON Customer1.Salesman_id = Salesman3.Salesman_id
WHERE Salesman3.COMISSION BETWEEN 0.12 AND 0.14;

SELECT Orders4.ORD_NO, Customer1.CUST_NAME,Salesman3.COMISSION AS "COMISSION"
FROM Orders4
JOIN Customer1 ON Orders4.customer_id = Customer1.customer_id
JOIN Salesman3 ON Orders4.Salesman_id = Salesman3.Salesman_id
WHERE Customer1.GRADE >= 200;

SELECT *
FROM Customer1
JOIN Orders4 ON Customer1.customer_id = Orders4.customer_id
WHERE Orders4.ORD_DATE = '2012-10-05';