SELECT p.name, f.name
FROM providers AS f
JOIN products AS p ON p.id_providers = f.id
WHERE f.name = 'Ajax SA';