DROP DATABASE IF EXISTS library_1;
CREATE DATABASE library_1;
USE library_1;

DROP TABLE IF EXISTS authors;
CREATE TABLE authors (
	id SERIAL PRIMARY KEY, 
    firstname VARCHAR(100),
    lastname VARCHAR(100),
   	INDEX authors_firstname_lastname_idx(firstname, lastname)
) COMMENT 'авторы';

DROP TABLE IF EXISTS media;
CREATE TABLE media ( 
	id SERIAL PRIMARY KEY,
    filename VARCHAR(255),
    body text,
    size INT,
    metadata JSON
) COMMENT 'фотографии читателей и авторов';

DROP TABLE IF EXISTS profiles_authors;
CREATE TABLE profiles_authors (
	author_id BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    gender CHAR(1),
    birthday DATE,
	photo_id BIGINT UNSIGNED NULL,
    hometown VARCHAR(100),
    
    FOREIGN KEY (author_id) REFERENCES authors(id) ON UPDATE CASCADE ON DELETE restrict,
    FOREIGN KEY (photo_id) REFERENCES media(id) ON UPDATE CASCADE ON DELETE restrict
) COMMENT 'общая информация о авторе';

DROP TABLE IF EXISTS genres;
CREATE TABLE genres (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100)
) COMMENT 'жанры';

DROP TABLE IF EXISTS publishing_office;
CREATE TABLE publishing_office (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100),
	country VARCHAR(100)
) COMMENT 'издательство';

DROP TABLE IF EXISTS year_edition;
CREATE TABLE year_edition (
	id SERIAL PRIMARY KEY,
	year_edition SMALLINT UNSIGNED NOT NULL
) COMMENT 'год издания';

DROP TABLE IF EXISTS readers;
CREATE TABLE readers ( 
	id SERIAL PRIMARY KEY,
	nickname VARCHAR(100),
	status ENUM ('active', 'inactive') NOT NULL,
	start_subscription DATE NULL,
    finish_subscription DATE NULL
) COMMENT 'читатели(подписчики)';

DROP TABLE IF EXISTS repository;
CREATE TABLE repository ( 
	id SERIAL PRIMARY KEY,
	total BIGINT UNSIGNED NOT NULL   
) COMMENT 'колличество книг в библиотеке';

DROP TABLE IF EXISTS books;
CREATE TABLE books (
	id SERIAL PRIMARY KEY, 
	book_title VARCHAR(150) NOT NULL,
	authors_id BIGINT UNSIGNED NOT NULL,
	genre_id BIGINT UNSIGNED NOT NULL,
	edition_id BIGINT UNSIGNED NOT NULL,
	publilishing_id BIGINT UNSIGNED NOT NULL,
	summary TEXT,
	
	FOREIGN KEY (id) REFERENCES repository(id),
	FOREIGN KEY (authors_id) REFERENCES authors(id),
	FOREIGN KEY (genre_id) REFERENCES genres(id),
	FOREIGN KEY (edition_id) REFERENCES year_edition(id),
	FOREIGN KEY (publilishing_id) REFERENCES publishing_office(id),
	FOREIGN KEY (id) REFERENCES readers(id) ON UPDATE CASCADE ON DELETE restrict
	
) COMMENT 'название и краткое содержание книги';

DROP TABLE IF EXISTS profiles_readers;
CREATE TABLE profiles_readers (
	reader_id BIGINT UNSIGNED NOT NULL PRIMARY KEY,
	firstname VARCHAR(100),
    lastname VARCHAR(100),
	gender CHAR(1),
	birthday DATE,
	hometown VARCHAR(100),
	email VARCHAR(120) UNIQUE,
    phone BIGINT,
	photo_id BIGINT UNSIGNED NULL,
    created_at DATETIME DEFAULT NOW(),
    INDEX profiles_readers_firstname_lastname_idx(firstname, lastname),
    
    FOREIGN KEY (reader_id) REFERENCES readers(id) ON UPDATE CASCADE ON DELETE restrict,
    FOREIGN KEY (photo_id) REFERENCES media(id) ON UPDATE CASCADE ON DELETE restrict
) COMMENT 'общая информация о читателе';

DROP TABLE IF EXISTS likes;
CREATE TABLE likes(
	id SERIAL,
    books_id BIGINT UNSIGNED NOT NULL,
    created_at DATETIME DEFAULT NOW(),
    
    FOREIGN KEY (books_id) REFERENCES books(id)

) COMMENT 'симпатия';


