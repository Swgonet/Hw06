SELECT DISTINCT s.name, subj.name, t.name
FROM students AS s
JOIN subjects AS subj
JOIN ratings AS r ON r.student_id = s.id
JOIN teachers AS t ON t.id = subj.teacher_id
WHERE s.id = '1';
