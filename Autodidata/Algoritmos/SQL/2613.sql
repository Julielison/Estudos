SELECT m.id, m.name
FROM movies AS m
JOIN prices ON m.id_prices = prices.id
WHERE value < 2;