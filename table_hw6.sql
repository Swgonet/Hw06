drop table if exists students;
CREATE TABLE IF NOT EXISTS students (
  id INT PRIMARY KEY,
  fullname VARCHAR(150),
  group_id REFERENCES groups(id)
  );

drop table if exists groups;
CREATE TABLE IF NOT EXISTS groups (
  id INT PRIMARY KEY,
  name VARCHAR(150)
);

drop table if exists teachers;
CREATE TABLE IF NOT EXISTS teachers (
  id INT PRIMARY KEY,
  fullname VARCHAR(150)
);

drop table if exists subject;
CREATE TABLE IF NOT EXISTS subject (
  id INT PRIMARY KEY,
  name VARCHAR(150),
  teachers_id REFERENCES teachers(id)
);

drop table if exists rating;
CREATE TABLE IF NOT EXISTS rating (
  rating_id INT PRIMARY KEY,
  student_id INTEGER REFERENCES students(id),
  subject_id INTEGER REFERENCES subject(id),
  ratin INTEGER CHECK (ratin >= 0 AND ratin <= 100),
  rating date DATE NOT NULL
);