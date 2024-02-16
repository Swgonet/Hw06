import sqlite3

def execute_query(sql):
    with sqlite3.connect('hw_06.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT s.id, s.name, AVG(r.rating) AS average_rating
FROM students as s
LEFT JOIN ratings as r ON s.id = r.id
GROUP BY s.id, s.name
ORDER BY average_rating DESC
LIMIT 5;
"""

print(execute_query(sql))
