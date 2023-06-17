-- Create initial tables
-- if they already exists, do nothing

create table if not exists advertisements
(
    id bigserial primary key,
    "name" varchar(100) not null,
    image_url varchar(100) not null,
    scraped_hash_id varchar(100) not null
);

comment on table advertisements is 'Advertisements from sreality.cz – flats, sell';
comment on column advertisements.id is 'Id of the advertisement.';
comment on column advertisements.name is 'Title of the advertisement';
comment on column advertisements.image_url is 'Url of the advertised image';
comment on column advertisements.scraped_hash_id is 'Hash id from the sreality assigned to the advertisement';