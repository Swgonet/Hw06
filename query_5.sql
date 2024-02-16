SELECT subj.name
FROM subjects AS subj
JOIN teachers AS t ON subj.teacher_id = t.id
WHERE t.name = 'Diane Donovan';