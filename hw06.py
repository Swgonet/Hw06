import sqlite3
from faker import Faker
import random


conn = sqlite3.connect('hw_06.db')
cursor = conn.cursor()

cursor.executescript('''DROP TABLE IF EXISTS students;
               CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    group_id INTEGER,
                    FOREIGN KEY (group_id) REFERENCES groups(id)
                )''')

cursor.executescript('''DROP TABLE IF EXISTS groups;
               CREATE TABLE IF NOT EXISTS groups (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )''')

cursor.executescript('''DROP TABLE IF EXISTS teachers;
               CREATE TABLE IF NOT EXISTS teachers (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )''')

cursor.executescript('''DROP TABLE IF EXISTS subjects;
               CREATE TABLE IF NOT EXISTS subjects (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    teacher_id INTEGER,
                    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
                )''')

cursor.executescript('''DROP TABLE IF EXISTS ratings;
               CREATE TABLE IF NOT EXISTS ratings (
                    id INTEGER PRIMARY KEY,
                    student_id INTEGER,
                    subject_id INTEGER,
                    rating INTEGER,
                    date TEXT,
                    FOREIGN KEY (student_id) REFERENCES students(id),
                    FOREIGN KEY (subject_id) REFERENCES subjects(id)
                )''')

fake = Faker()

for _ in range(3):
    cursor.execute('''INSERT INTO groups (name) VALUES (?)''', (fake.word(),))

for _ in range(30):
    group_id = random.randint(1, 3)
    cursor.execute('''INSERT INTO students (name, group_id) VALUES (?, ?)''', (fake.name(), group_id))

for _ in range(3):
    cursor.execute('''INSERT INTO teachers (name) VALUES (?)''', (fake.name(),))

for _ in range(5):
    teacher_id = random.randint(1, 3)
    cursor.execute('''INSERT INTO subjects (name, teacher_id) VALUES (?, ?)''', (fake.word(), teacher_id))

for student_id in range(1, 31):
    for subject_id in range(1, 6):
        rating = random.randint(1, 100)
        cursor.execute('''INSERT INTO ratings (student_id, subject_id, rating, date) VALUES (?, ?, ?, ?)''', (student_id, subject_id, rating, fake.date_this_decade()))

conn.commit()
conn.close()
