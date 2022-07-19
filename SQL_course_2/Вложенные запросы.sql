-- Получите из таблицы products джинсы, стоимость которых больше средней цены за джинсы.
SELECT p.name
FROM products p 
INNER JOIN categories c ON p.category = c.id 
WHERE c.name = 'Джинсы' AND price > 
(SELECT AVG(price) FROM products
INNER JOIN categories ON products.category = categories.id 
WHERE categories.name = 'Джинсы');

-- Магазину нужно заказать только те фрукты, количество которых меньше самого маленького количества овощей. 
-- Получите список фруктов, которые необходимо заказать.
SELECT p.name
FROM products p 
INNER JOIN categories c ON c.id = p.category_id  
WHERE c.name = 'Фрукты' AND p.count < ALL
(SELECT count 
FROM products p 
INNER JOIN categories c ON c.id = p.category_id  
WHERE c.name = 'Овощи');

-- Получите список овощей, цена которых больше чем ЛЮБАЯ из цен фруктов.
SELECT p.name
FROM products p 
INNER JOIN categories c ON c.id = p.category_id  
WHERE c.name = 'Овощи' AND p.price > ANY
(SELECT count 
FROM products p 
INNER JOIN categories c ON c.id = p.category_id  
WHERE c.name = 'Фрукты');

-- Получите все песни за 2008 год.
SELECT name, album_id 
FROM songs s
WHERE EXISTS(SELECT * FROM albums a WHERE s.album_id = a.id AND a.`year` = '2008');

-- Получите список всех сотрудников, которые не выполняют ни одной роли.
SELECT first_name, last_name 
FROM users u 
WHERE NOT EXISTS (SELECT * FROM users_roles ur WHERE u.id = ur.user_id);

-- Получите из people всех подозреваемых основываясь на данных из таблицы suspects.
SELECT *
FROM people p
WHERE (first_name, last_name, age) IN (SELECT  fn, ln, age FROM suspects s);

-- Получите из people всех людей, у которых неверные имена или фамилии.
SELECT first_name, last_name
FROM people p
WHERE (p.first_name, p.last_name) NOT IN 
(SELECT fn.first_name, ln2.last_name 
 FROM first_names fn
 INNER JOIN last_names ln2 
 ON fn.id = ln2.id )
 
 -- Выведите дату (колонка date), сумму и тип последних трех транзакций.
(SELECT `date`
FROM bank_transactions bt ) 
UNION ALL
(SELECT `date`
FROM cashbox_transactions ct ) 
UNION ALL
(SELECT `date`
FROM paypal_transactions pt )
ORDER BY 1 DESC 
LIMIT 3

-- 