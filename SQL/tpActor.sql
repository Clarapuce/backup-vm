/*2c
select first_name, last_name from actor where last_name like '%LI%' order by last_name;*/

/* 2d
select country_id, country from country where country in ('Afghanistan','Bangladesh','China');

--alter table actor add middle_name blob after first_name;
--alter table actor modify last_name blob NOT NULL;

--4a

select last_name, count(*) as occurences from actor group by last_name having occurences >= 2;
*/

update actor set first_name ='Harpo' where first_name = 'Groucho' and last_name = 'Williams';
