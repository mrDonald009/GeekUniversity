ALTER TABLE users ADD new_created_at DATETIME
UPDATE users SET new_created_at = STR_TO_DATE(created_at, '%d.%m.%Y %l:%i')
ALTER TABLE users DROP created_at;
