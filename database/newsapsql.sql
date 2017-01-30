create database news_db

use news_db

create table resolved_news_type (id tinyint(3) unsigned primary key auto_increment not null,resolved_news_type varchar(250) unique);

create table unresolved_news_type(id tinyint(3) unsigned primary key auto_increment not null,unresolved_news_type_name varchar(250) unique);

create table map_unresolved_resolved_news_type_map(id tinyint(3) primary key auto_increment, resolved_news_type_id tinyint(3) unsigned, unresolved_news_type_id tinyint(3) unsigned, foreign key(resolved_news_type_id) references resolved_news_type(id),  foreign key(unresolved_news_type_id) references unresolved_news_type(id) );

create table resolved_location(id smallint unsigned primary key auto_increment, resolved_location_name varchar(250) unique);Query OK, 0 rows affected 
create table unresolved_location(id smallint unsigned primary key not null auto_increment, unresolved_location_name varchar(250) unique); 

create table map_unresolved_resolved_location(id smallint primary key auto_increment, resolved_location_id smallint unsigned ,foreign key(resolved_location_id) references resolved_location(id), unresolved_location_id smallint unsigned ,foreign key(unresolved_location_id) references unresolved_location(id));


create table source(id smallint unsigned primary key not null auto_increment, source_name varchar(250) unique,source_url varchar(250));

create table author(id smallint unsigned primary key auto_increment, author_name varchar(250) unique, source_id smallint unsigned, foreign key(source_id) references source(id));

create table article_download(id int unsigned primary key not null auto_increment, local_file_path varchar(250), article_download_created_date date,article_download_last_updated date, is_parsed tinyint);

create table article_parsed(id int unsigned primary key auto_increment, article_title varchar(250), uresolved_news_type_id tinyint(3) unsigned, foreign key(uresolved_news_type_id) references unresolved_news_type(id), url varchar(250), published_date date, created_date date, last_updated_date date, unresolved_location_id smallint unsigned, foreign key(unresolved_location_id) references unresolved_location(id), author_id smallint unsigned , foreign key(author_id) references author(id), Source_id smallint unsigned, foreign key(source_id) references source(id), unique_id varchar(250), article_download_id int unsigned, foreign key(article_download_id) references article_download(id));

create table article_content(id int unsigned primary key auto_increment, article_parsed_id int unsigned, foreign key (article_parsed_id) references article_parsed(id), content text);




