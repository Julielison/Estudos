-- Então seu trabalho será exibir o nome e a quantidade de produtos de cada uma categoria.
SELECT b.name, SUM(amount)
FROM products AS a
JOIN categories AS b ON b.id = a.id_categories
GROUP BY b.name;