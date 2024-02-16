SELECT t.name, AVG(r.rating)
FROM teachers AS t
JOIN ratings AS r ON t.id = r.subject_id
GROUP BY t.id, t.name;