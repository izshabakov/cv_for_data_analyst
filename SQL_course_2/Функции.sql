-- Комментарии к посту на сайте разбиты на страницы – по 10 комментариев на каждой. 
-- Выведите из таблицы posts id поста, количество комментариев (comments) и количество страниц (pages), которое необходимо для вывода этих комментариев.
SELECT id, comments, CEIL(comments/10) AS pages FROM posts p;

-- Получите название фильма, а также его рейтинг округленный до 2 знаков после запятой (например 4.34).
SELECT name, ROUND(rating,2) 
FROM films f
ORDER BY rating DESC 
LIMIT 5;

-- Нормальная температура колеблется в пределах от -10 до +10 градусов включительно.
-- Если температура выходит за эти пределы в любую из сторон, то она считается критической.
-- Выведите эксперименты с критической температурой.
SELECT id, temperature 
FROM experiments e 
WHERE temperature BETWEEN -10 AND 10;

-- Измените исходный запрос так, чтобы короткие серии и номера получили лидирующие нули:
SELECT user_id, concat(rpad(series,4,'0'),' ', rpad(number,6,'0')) AS pp 
FROM passports p;

-- В таблице domains содержится список доменных имен. Некоторые домены оканчиваются на точку, например (google.com.). 
-- Обновите таблицу так, чтобы доменные имена не заканчивались точкой.
SELECT IF(RIGHT(DOMAIN,1)='.',TRIM(TRAILING '.' FROM DOMAIN),DOMAIN)
FROM domains d;

-- Перенесите на 1,5 часа вперед все записи после 13 часов дня (включительно) за 14 мая 2017 года.
SELECT visit_date + INTERVAL 90 MINUTE 
FROM calendar c 
WHERE CAST(visit_date AS DATE) = '2017-05-14' AND HOUR(visit_date) > 13;

-- Получите из таблицы tasks все задачи, запланированные на будущее. 



