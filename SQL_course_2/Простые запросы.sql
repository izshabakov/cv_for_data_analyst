USE sql_course;
-- Получите всю информацию о товарах из таблицы products.
SELECT
	*
FROM
	products p;
-- Получите название (name) и цену (price) всех товаров из таблицы products.
SELECT
	name,
	price
FROM
	products p;
-- Выберите из таблицы products все записи, в которых цена (price) меньше 3000.
SELECT
	*
FROM
	products p
WHERE
	price < 3000;
-- Выберите из таблицы products имена (name) и цены (price) всех товаров, стоимостью от 10 000 и выше.
SELECT
	*
FROM
	products p
WHERE
	price >= 10000;
-- Получите из таблицы products имена (name) товаров, которые закончились.
SELECT
	*
FROM
	products p
WHERE
	count  = 0;
-- Выберите из таблицы products название (name) и цены (price) товаров, стоимостью до 4000 включительно.
SELECT
	*
FROM
	products p
WHERE
	price  <= 4000;

