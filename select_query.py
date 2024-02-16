import sqlite3
import sys

def execute_query(sql):
    with sqlite3.connect('hw_06.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


file_path = sys.argv[1]
with open(file_path, 'r') as f:
    sql = f.read()

print(execute_query(sql))
