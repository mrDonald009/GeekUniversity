alter table vk.profiles add is_acitve bit default 1;

update profiles 
set is_active = 0
where created_at - birthday > 18;