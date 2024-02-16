SELECT s.name
FROM students AS s
JOIN groups AS g ON s.group_id = g.id
WHERE s.group_id = '1';