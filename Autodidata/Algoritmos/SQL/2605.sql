-- Seu trabalho é retornar os nomes dos produtos e dos fornecedores cujo código da categoria é 6.
SELECT products.name, providers.name
FROM providers
JOIN products ON products.id_providers = providers.id 
WHERE id_categories = 6;