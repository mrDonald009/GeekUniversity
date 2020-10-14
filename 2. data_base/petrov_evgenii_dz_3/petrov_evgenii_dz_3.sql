drop table if exists media_list;
create table media_list(
	id serial,
	name varchar(255)
);

drop table if exists  album_old_foto;
create table album_old_foto (
	id serial,
	user_id bigint unsigned not null,
	old_foto_id bigint unsigned not null,
	body text,
	created_at datetime default now(),
	updated_at datetime on update current_timestamp,
	
	foreign key (old_foto_id) references media_list(id),
	foreign key (user_id) references users(id)
);

drop table if exists  album_new_foto;
create table album_new_foto (
	id serial,
	user_id bigint unsigned not null,
	new_foto_id bigint unsigned not null,
	body text,
	created_at datetime default now(),
	updated_at datetime on update current_timestamp,
	
	foreign key (new_foto_id) references media_list(id),
	foreign key (user_id) references users(id)
);