SELECT s.name, r.rating
FROM ratings as r
JOIN subjects as subj ON r.subject_id = subj.id
JOIN students AS s ON s.id = r.student_id
JOIN groups AS g ON g.id = s.group_id
WHERE subj.name = 'best' AND g.name = 'game';
