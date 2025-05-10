-- Практическое задание по теме "Транзакции, переменные, представления"

-- 1. В базе данных shop и sample присутствуют одни и те же таблицы, учебной базы данных.
-- переместите запись id = 1  из таблицы shop.users в таблицу sample.users. Используйте транзакции.

start transaction;
insert into sample.users select * from shop.users where id = 1;
delete from shop.users where id = 1;
commit;

select * from sample.users where id = 1;
select * from shop.users where id = 1;

-- Практическое задание по теме “Хранимые процедуры и функции, триггеры"

-- 1. Создайте хранимую функцию hello(), которая будет возвращать приветствие, в зависимости от текущего 
-- времени суток. С 6:00 до 12:00 функция должна возвращать фразу "Доброе утро", с 12:00 до 18:00 функция
-- должна возвращать фразу "Добрый день", с 18:00 до 00:00 — "Добрый вечер", с 00:00 до 6:00 — "Доброй ночи".

delimiter //
create function hello()
returns varchar(255) deterministic 
begin
	declare hour int;
	set hour = hour(now());
	case 
		when  hour between 6 and 11 then 
		return 'доброе утро';
		when  hour between 12 and 17 then 
		return 'добрый день';
		when  hour between 18 and 23 then 
		return 'добрый вечер';
		when  hour between 0 and 5 then 
		return  'доброй ночи';
	end case;
end //

select hello()	

