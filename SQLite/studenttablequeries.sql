CREATE TABLE student(
    ROLL_NO TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    ADRESS TEXT,
    PHONE TEXT,
    AGE INTEGER
);

INSERT INTO student( ROLL_NO, NAME, ADRESS, PHONE, AGE) VALUES
('1', 'Ram', 'Delhi', '********', 18),
('2', 'Ramesh', 'Gurgaon', '********', 18),
('3', 'Sujit', 'Rohtak', '********', 20),
('4', 'Suresh', 'Delhi', '********', 18),
('5', 'Aman', 'Rohtak', '********', 20),
('6', 'Harsh', 'Gurgaon', '********', 18);

SELECT * FROM student;

SELECT * FROM student WHERE AGE = 18 AND ADRESS = 'Delhi';
SELECT * FROM student WHERE AGE = 18 AND NAME = 'Ram';
SELECT * FROM student WHERE NAME = 'Ram' OR NAME = 'Sujit';
SELECT * FROM student WHERE NAME = 'Ram' OR AGE = 20;
SELECT * FROM student WHERE AGE = 18 AND (NAME = 'Ram' OR NAME = 'Ramesh');