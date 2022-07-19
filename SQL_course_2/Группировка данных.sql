-- Получите средний чек магазина за 2015 год.
-- Средний чек — это средняя стоимость выполненных (success) заказов.
SELECT avg(amount) AS avg_check
FROM orders o  
WHERE status = 'success' AND YEAR(`date`) = 2015;

-- Получите дату первого отмененного заказа.
-- Значение выведите в формате ДД.ММ.ГГГГ в колонке date.
SELECT MIN(date)
FROM orders o 
WHERE status = 'cancelled';

-- Сгруппируйте данные в таблице users по возрасту и получите количество сотрудников каждого возраста.
SELECT age, count(*) AS client_count 
FROM users u 
GROUP BY age 
ORDER BY age;

-- Сгруппируйте данные в таблице orders по году и месяцу, а затем получите сумму и количество заказов в каждом месяце. 
-- Данные должны быть отсортированы в хронологическом порядке по году и месяцу.
SELECT 
	YEAR (date) AS year, 
	MONTH (`date`) AS month, 
	SUM(amount) AS income, 
	COUNT(*) AS orders FROM orders o
GROUP BY 
	YEAR (date), 
	MONTH (`date`)
ORDER BY 
	YEAR (date), 
	MONTH (`date`);