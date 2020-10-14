use vk;
-- 1. Выбираем пользователя, который больше всех общался с пользователем (users.id = 1).
select firstname, lastname from users where id = 
	(select 
	from_user_id 
	from messages 
	where to_user_id = 1
	order by from_user_id 
	desc limit 1);

-- 2. Вывести общее колличество лайков, которые получили пользоаватели младше 10 лет.
select count(*) from likes where user_id in (
select user_id from profiles where timestampdiff(year, birthday,now()) <= 10);

-- 3. Определить кто больше поставил лайков(всего):мужчины или женщины.
select
	(select count(*) from likes where 
		(select count(*) from profiles where likes.user_id = user_id and gender = 'm')) as male_likes, 
	(select count(*) from likes where 
		(select count(*) from profiles where likes.user_id = user_id and gender = 'f')) as female_likes;
	
use shop;
-- 4.(1) Составьте список пользователей users, которые осуществили хотя бы один заказ orders в интернет магазине.
select id, name 
from users 
where exists (select * from orders where user_id = users.id);

-- 5.(2) Выведите список товаров products из разделов catalogs, который соответствует товару.
select name 
from catalogs 
where id in (select catalog_id from products where catalog_id = catalogs.id);





