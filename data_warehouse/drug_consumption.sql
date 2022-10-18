drop table if exists background; 
drop table if exists personality; 

create table background (
    id integer,
    age integer,
    gender integer,
    education integer,
    country integer,
    ethnicity integer
);

insert into background
values(1, 2, 3, 4, 5, 6)
returning *; 

create table personality (
    nscore integer, 
    escore integer, 
    oscore integer, 
    ascore integer, 
    cscore integer
);