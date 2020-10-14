DROP TABLE IF EXISTS logs;
CREATE TABLE logs (
	id bigint,
	table_name varchar(255),
	name varchar(255),
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- users
DROP TRIGGER IF EXISTS l

CREATE TRIGGER log_users AFTER INSERT ON users
FOR EACH ROW
BEGIN 
	INSERT INTO logs (id, table_name, name) VALUES 
	(NEW.id, 'users', NEW.name);
END// 

-- обновление таблицы users
INSERT INTO shop.users (name, birthday_at, created_at, updated_at) 
VALUES 
('Jack','1990-01-01','2020-07-19 11:32:28','2020-07-19 11:32:28');

-- проверка
SELECT * FROM logs;


-- catalogs
DROP TRIGGER IF EXISTS log_catalogs;
delimiter //

CREATE TRIGGER log_catalogs AFTER INSERT ON catalogs
FOR EACH ROW
BEGIN 
	INSERT INTO logs (id, table_name, name) VALUES 
	(NEW.id, 'catalogs', NEW.name);
END//

-- обновление таблицы catalogs
INSERT INTO shop.catalogs (name) VALUES  ('Принтер');

-- проверка
SELECT * FROM logs;


-- products

DROP TRIGGER IF EXISTS log_products;

delimiter //
CREATE TRIGGER log_products AFTER INSERT ON products
FOR EACH ROW
BEGIN 
	INSERT INTO logs (id,table_name,name) VALUES 
	(NEW.id, 'products', NEW.name);
END//

-- обновление таблицы catalogs
INSERT INTO products
  (name, description, price, catalog_id)
VALUES
  ('Intel Core i3-8100', 'Процессор ', 10000.00, 1);

-- проверка таблицы products
SELECT * FROM logs;
