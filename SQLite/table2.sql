CREATE TABLE Salesman1 (
    Salesman_id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    Comission REAL
);

INSERT INTO Salesman1( Salesman_id, name, city, Comission) VALUES
('5001','James Hoog', 'New York', 0.15),
('5002','Nail Knite', 'Paris', 0.13),
('5005','Pit Alex', 'London', 0.11),
('5006','Mc Lyon', 'Paris', 0.14),
('5007','Paul Adam', 'Rome', 0.13),
('5003','Lauson Hen', 'San Hose', 0.12);

SELECT * FROM Salesman1;

CREATE TABLE Orders2 (
    ord_no  INT PRIMARY KEY,
    purch_amt REAL,
    ord_date TEXT,
    customer_id TEXT,
    salesman_id TEXT,
);

INSERT INTO Orders2 ( ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES
('70001', 150.5, '2012-10-05', '3005','5002'),
('70009', 150.5, '2012-10-05', '3005','5002'),
('70002', 150.5, '2012-10-05', '3005','5002'),
('70004', 150.5, '2012-10-05', '3005','5002'),
('70007', 150.5, '2012-10-05', '3005','5002'),
('70001', 150.5, '2012-10-05', '3005','5002');

SELECT * FROM Orders2;
SELECT name, Comission
FROM Salesman1;
