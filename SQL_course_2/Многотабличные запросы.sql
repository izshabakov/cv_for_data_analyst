-- Объедините с помощью UNION таблицы bank_transactions и cashbox_transactions.
SELECT * FROM bank_transactions bt 
UNION ALL
SELECT * FROM cashbox_transactions ct;

-- Ваша задача — объединить таблицы из разных регионов так, чтобы получилась таблица со следующий структурой:
-- number — номер автомобиля в формате а111аа.
-- region — регион регистрации автомобиля (целое число).
-- mark — марка автомобиля.
-- model — модель автомобиля.
SELECT substring(number,1,6) AS `number` , RIGHT(`number`,2) AS region, mark, model
FROM cars c
UNION ALL
SELECT `number`, 39, mark, model
FROM region39 r
UNION ALL
SELECT LOWER(`number`), region, mark, model
FROM avto a 
UNION ALL
SELECT substring(number,1,6), RIGHT(`number`,2), SUBSTRING_INDEX( car," ", 1 ), SUBSTRING_INDEX( car," ", -1 )
FROM autos a2;

-- Получите из таблицы games данные для вывода на главную страницу сайта для категорий: 
-- 1 - Action, 2 - RPG, 3 - Adventure, 4 - Strategy и 5 - Shooter. 
-- Выведите поля id, name, rating и genre, где genre — название категории
(SELECT id, name, rating, 'Action' AS genre
FROM games g
WHERE category_id = 1
ORDER BY rating DESC
LIMIT 2)
UNION
(SELECT id, name, rating, 'RPG' AS genre
FROM games g
WHERE category_id = 2
ORDER BY rating DESC
LIMIT 2)
UNION
(SELECT id, name, rating, 'Adventure' AS genre
FROM games g
WHERE category_id = 3
ORDER BY rating DESC
LIMIT 2)
UNION
(SELECT id, name, rating, 'Strategy' AS genre
FROM games g
WHERE category_id = 4
ORDER BY rating DESC
LIMIT 2)
UNION
(SELECT id, name, rating, 'Shooter' AS genre
FROM games g
WHERE category_id = 5
ORDER BY rating DESC
LIMIT 2);

-- Платежи клиентов в базе данных хранятся в трех таблицах:
--    1. bank_transactions — прямые платежи на расчетный счет,
--    2. cashbox_transactions — платежи наличными в кассу организации,
--    3. paypal_transactions — платежи через сервис PayPal.

-- Получите общую сумму всех платежей клиентов. 
-- Колонку с результатом назовите all_money.
SELECT
	SUM(amount) AS all_money
FROM
	(
	SELECT
		amount
	FROM
		bank_transactions
UNION
	SELECT
		amount
	FROM
		cashbox_transactions
UNION
	SELECT
		amount
	FROM
		paypal_transactions)t;

-- На сайте интернет-магазина нужно выводить все категории, а не только те, в которых есть товары.
-- Получите имена категорий, а также количество товаров в каждой категории.
SELECT c.name, SUM(count) AS Количество
FROM products p 
INNER JOIN categories c ON c.id = p.category
GROUP BY c.id;

-- Получите список всех активных сотрудников с указанием их должностей.
-- Если у сотрудника нет должности, то нужно вывести NULL.
-- Выведите 3 столбца: имя, фамилию и должность (role).
-- Данные отсортируйте по фамилии, а после по имени в алфавитном порядке.
SELECT first_name, last_name, name
FROM employees e 
LEFT JOIN roles r ON e.role_id = r.id
ORDER BY 2, 1;

-- На сайте интернет-магазина нужно выводить только те категории, в которых есть товары.
-- Получите имена категорий, в которых есть товары, а также количество товаров в каждой категории.
SELECT c.name, SUM(count) AS Количество_вещей
FROM categories c 
INNER JOIN products p ON c.id = p.category
WHERE count > 0
GROUP BY c.name
HAVING SUM(count)>0
;

-- Получите все страны и города из таблиц countries и cities.
SELECT countries.name, cities.name
FROM countries 
LEFT JOIN cities ON countries.id = cities.country
UNION ALL 
SELECT countries.name, cities.name
FROM countries 
RIGHT JOIN cities ON countries.id = cities.country
ORDER BY 1, 2;

-- Получите все марки представленные в салоне, а также суммарную стоимость автомобилей каждой марки.
SELECT m2.name AS Марка, SUM(price)  AS Суммарная_стоимость
FROM cars c 
INNER JOIN models m ON c.model_id = m.id 
INNER JOIN marks m2 ON m.mark_id = m2.id
GROUP BY m2.name

-- Получите данные о звонках за 5 апреля 2018 года.
SELECT date_format(`date`,'%h:%s'), concat(m.first_name,' ',m.last_name),
concat(c2.first_name,' ',c2.last_name), c3.name, sec_to_time(c.duration_sec)
FROM calls c 
LEFT JOIN clients c2 ON c.client_id = c2.id 
LEFT JOIN managers m ON c.manager_id = m.id 
LEFT JOIN companies c3 ON c2.company_id = c3.id
WHERE CAST(c.`date`AS DATE) = '2018-04-05';

-- Получите список из пяти клиентов, которые потратили больше всего денег в интернет-магазине.
-- Учитывайте только выполненные заказы.
-- Выведите четыре поля: id, фамилию и имя клиента, а также потраченную им сумму (в поле value).
-- Данные отсортируйте по сумме в обратном порядке.
SELECT u.id, concat(u.first_name,' ',u.last_name) AS Клиент, SUM(price) AS Сумма_заказов
FROM users u 
INNER JOIN orders o ON u.id = o.user_id 
INNER JOIN orders_details od ON o.id = od.order_id 
INNER JOIN products p ON od.product_id = p.id
WHERE status = 'success'
GROUP BY u.id;