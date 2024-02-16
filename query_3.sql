SELECT g.id, g.name, AVG(r.rating) AS average_rating
FROM groups AS g
JOIN students AS s ON g.id = s.group_id
JOIN ratings AS r ON s.id = r.student_id
JOIN subjects AS subj ON r.subject_id = subj.id
WHERE subj.name = 'get'
GROUP BY g.id, g.name
ORDER BY average_rating DESC;