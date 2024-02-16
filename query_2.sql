SELECT s.id, s.name, AVG(r.rating) AS average_rating
FROM students AS s
JOIN ratings AS r ON s.id = r.student_id
WHERE r.subject_id = r.subject_id
GROUP BY s.id, s.name
ORDER BY average_rating DESC
LIMIT 1;
