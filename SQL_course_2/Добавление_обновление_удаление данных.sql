-- Добавьте в таблицу orders данные о новом заказе стоимостью 3000 рублей. В заказе 3 товара (products).
INSERT INTO orders(id, products,sum)
VALUES(6, 3, 3000);

-- Добавьте в таблицу products новый товар — «Xbox», стоимостью 30000 рублей в количестве (count) трех штук.
INSERT INTO products  (name, count, price)
VALUES('Xbox', 3, 30000);

-- Добавьте в таблицу products новый товар — «iMac 21», стоимостью 100100 рублей. Товар пока не завезли на склад.
INSERT INTO products  (name, count, price)
VALUES('Imac 21', 0, 100100);

-- Добавьте в таблицу users нового пользователя Антона Пепеляева с датой рождения 12 июля 1992 года
INSERT INTO users  (first_name , last_name, birthday)
VALUES('Антон', 'Пепеляев', '1992-07-12');