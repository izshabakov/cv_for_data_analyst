-- Выберите из таблицы users всех пользователей, чьи фамилии начинаются на А без учета регистра.
SELECT first_name, last_name 
FROM users u 
WHERE first_name LIKE 'А%'
ORDER BY 2,1 ASC ;

-- Выберите из таблицы domains имена всех доменов в зоне .ru и отсортируйте их по дате создания.
SELECT domain  FROM domains d 
WHERE DOMAIN LIKE '_%.ru'
ORDER BY created ;

-- Отдел маркетинга посчитал, что цены, которые заканчиваются на два нуля, следует уменьшить на 1 рубль, чтобы в конце было 99 (400 -> 399).
UPDATE wines 
SET price = price - 1
WHERE price LIKE '%00';

-- Правильное название марки автомобилей — BMW (все буквы заглавные).
-- Однако в таблице много автомобилей BMW, которые записаны неверно.
-- Найдите все автомобили с неверным названием.
SELECT * FROM cars c 
WHERE mark LIKE 'bmw ' AND mark NOT LIKE  BINARY 'BMW';

-- Выберите из таблицы domains имена всех доменов, у которых домен первого уровня состоит из 3 символов.
-- Отсортируйте данные по имени домена в алфавитном порядке.
SELECT `domain` FROM domains d 
WHERE `domain` LIKE '%.___';

-- Один из участников ДТП скрылся с места аварии.
-- Однако прохожие успели заметить часть номера автомобиля нарушителя.
-- В частности они запомнили, что серия заканчивается на ОР (русскими буквами), а регистрационный номер начинается с единицы. Также они запомнили марку автомобиля — Ford, и его цвет — желтый или зеленый (мнения разделились, так как на улице было уже темно).
SELECT * FROM cars c 
WHERE `number` LIKE '_1__ОР%' AND mark = 'Ford' AND (color = 'желтый' OR color = 'зеленый');

-- Получите из таблицы products все джинсы и жилеты, за исключеним товаров фирмы Mango.
SELECT * FROM products p 
WHERE MATCH(name)
AGAINST('Джинсы Жилет -Mango' IN BOOLEAN MODE);

-- Найдите в таблице products все товары, которые содержат фразу «Джинсы Mango».
SELECT * FROM products p 
WHERE MATCH(name)
AGAINST('"Джинсы Mango"' IN BOOLEAN MODE);

-- Получите из таблицы products все джинсы и юбки компании Mango.
SELECT * FROM products p  WHERE
MATCH (name) AGAINST ('+Джинсы +Mango' IN BOOLEAN MODE) OR
MATCH (name) AGAINST ('+Юбка +Mango' IN BOOLEAN MODE);

-- В таблице products содержатся товары из женского магазина. 
-- Пользователь ищет джинсы фирмы Mango 36 или 38 размера. 
-- Получите из таблицы id, название и цену всех подходящих товаров. 
-- Учитывайте, что некоторых позиций на складе нет.
SELECT * FROM products p  WHERE
MATCH (name) AGAINST ('"Джинсы Mango"') AND
(FIND_IN_SET(36,sizes) OR FIND_IN_SET(38,sizes));
-- Найдите в таблице forum все посты, которые содержат слова «ошибка» или «проблема».
SELECT * FROM forum f WHERE
MATCH (subject, post) AGAINST ('Ошибк* Проблем*' IN BOOLEAN MODE)