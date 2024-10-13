SELECT p.name, f.name, c.name
FROM products AS p
JOIN providers AS f ON f.id = p.id_providers
JOIN categories AS c ON p.id_categories = c.id
WHERE f.name = 'Sansul SA' AND c.name = 'Imported';