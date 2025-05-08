use library_1;

-- Название книги, которая понравилась болшинству читателей.
select book_title, count(*) as likes_count 
from books 
	join likes on books.id = likes.books_id
group by books.id
order by likes_count desc 
limit 1;

-- Имена и фотографии пользователей, которые взяли книги на прочтение. 
select nickname, filename
from profiles_readers pr
	join readers on pr.reader_id = readers.id and stauts = 'active'
	join media on pr.photo_id = media.id;
	
-- Название книги, колличество которой больше всего в библиотеке.
select book_title, total
from books 
	join repository on books.id = repository.id
order by total desc
limit 1;

-- Название жанра, которое нравится пользователю readers.id = 1.
select name
from genres
	join books on genres.id = books.genre_id 
	join readers on books.id = readers.id
	where readers.id = 1
order by name desc
limit 1
;
