CREATE DEFINER=`root`@`localhost` PROCEDURE `library_1`.`friendship_book`(for_reader_id bigint)
BEGIN
	-- пользователи которые прочитали одни книги и живут в одном городе.
select pr2.reader_id
	from profiles_readers pr1
	join profiles_readers pr2 on pr1.hometown = pr2.hometown 
	where pr1.reader_id = for_reader_id
	and pr2.reader_id != for_reader_id
	union
select b2.id
	from books b1
	join books b2 on b1.book_title = b2.book_title 
	where b1.id = for_reader_id
	and b2.id != for_reader_id;
END
