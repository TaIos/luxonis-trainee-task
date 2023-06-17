-- Create initial tables
-- if they already exists, do nothing

create table if not exists advertisement
(
    id bigserial primary key,
    title varchar(100) not null,
    image varchar not null,
    url varchar(100) not null,
);

comment on table advertisement is 'Advertisements from sreality.cz – flats, sell';
comment on column advertisement.id is 'Id of the advertisement.';
comment on column advertisement.title is 'Title of the advertisement';
comment on column advertisement.image is 'Image of the advertisement stored as base64';
comment on column advertisement.url 'Url of the advertisement.';

-- TODO might add check for valid base64 advertisement.image here or in the application logic
-- TODO might add check for valid advertisement.url here or in the application logic
