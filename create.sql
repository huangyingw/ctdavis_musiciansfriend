CREATE TABLE IF NOT EXISTS quotes (
    id int AUTO_INCREMENT PRIMARY KEY, 
    title      varchar(255),
    movie_name varchar(255),
    actress    varchar(255),
    mosaic     varchar(255),
    size       varchar(255),
    torrents   text,
    magnets    text,
    link       varchar(255)
);
