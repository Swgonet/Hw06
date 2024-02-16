SELECT DISTINCT s.name, subj.name
FROM students AS s
JOIN subjects AS subj
JOIN ratings AS r ON r.student_id = r.subject_id 
WHERE s.id = '2';