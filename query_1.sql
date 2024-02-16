SELECT s.id, s.name, AVG(r.rating) AS average_rating
FROM students as s
LEFT JOIN ratings as r ON s.id = r.student_id
GROUP BY s.id
ORDER BY average_rating DESC
LIMIT 5;
