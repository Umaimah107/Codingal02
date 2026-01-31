CREATE TABLE students(
    students_id TEXT PRIMARY KEY,
    name TEXT,
    age TEXT,
    class TEXT
);

INSERT INTO students(students_id, name, age, class) VALUES
('201','Ana','12','6 grade'),
('205','Tim','15','9 grade'),
('210','Ben','13','7 grade'),
('215','jim','8','4 grade');

SELECT * FROM students;