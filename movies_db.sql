/* 1. Описание базы данных. */

Целью проекта было создание базы данных фильмов. 
Данная база данных состоит из 10 таблиц.
База включает в себя информацию о фильме, жанры, номинации, в которых фильм победил, и назания студий.


/* 2. Создание базы данных */

DROP DATABASE IF EXISTS movies_db;
CREATE DATABASE movies_db;
USE movies_db;

DROP TABLE IF EXISTS movies;
CREATE TABLE movies (
	id SERIAL PRIMARY KEY,
    title_orig VARCHAR(100),
    title_rus VARCHAR(100),
    descr VARCHAR(250),
    INDEX movies_name(title_orig, title_rus)
);

DROP TABLE IF EXISTS `meta_info`;
CREATE TABLE `meta_info` (
	id SERIAL PRIMARY KEY,
	movie_id BIGINT UNSIGNED NOT NULL,
    year BIGINT,
    country VARCHAR(100),
    genre VARCHAR(100),
    director VARCHAR(100),
    composer VARCHAR(100),
    budget BIGINT,
    
    FOREIGN KEY (movie_id) REFERENCES movies(id) ON UPDATE CASCADE ON DELETE CASCADE
);

DROP TABLE IF EXISTS genres;
CREATE TABLE genres (
	id SERIAL PRIMARY KEY,
    genre_name VARCHAR(100)
);

DROP TABLE IF EXISTS movie_genres;
CREATE TABLE movie_genres (
    id SERIAL PRIMARY KEY,
    movie_id BIGINT UNSIGNED NOT NULL,
    genre_id BIGINT UNSIGNED NOT NULL,
    
    CONSTRAINT movie_genres_fk_movie FOREIGN KEY (movie_id) REFERENCES movies(id),
	CONSTRAINT movie_genres_fk_genre FOREIGN KEY (genre_id) REFERENCES genres(id)
);

DROP TABLE IF EXISTS countries;
CREATE TABLE countries (
	id SERIAL PRIMARY KEY,
    country_name VARCHAR(100)
);

DROP TABLE IF EXISTS movie_countries;
CREATE TABLE movie_countries (
	id SERIAL PRIMARY KEY,
    movie_id BIGINT UNSIGNED NOT NULL,
    country_id BIGINT UNSIGNED NOT NULL,
    
    CONSTRAINT movie_countries_fk_movie FOREIGN KEY (movie_id) REFERENCES movies(id),
    CONSTRAINT movie_countries_fk_country FOREIGN KEY (country_id) REFERENCES countries(id)
);

DROP TABLE IF EXISTS studios;
CREATE TABLE studios (
	id SERIAL PRIMARY KEY,
    studio_name VARCHAR(100)
 );
 
DROP TABLE IF EXISTS movie_studios;
CREATE TABLE movie_studios (
	id SERIAL PRIMARY KEY,
    movie_id BIGINT UNSIGNED NOT NULL,
    studio_id BIGINT UNSIGNED NOT NULL,
    
	CONSTRAINT movie_studios_fk_movie FOREIGN KEY (movie_id) REFERENCES movies(id),
    CONSTRAINT movie_studios_fk_country FOREIGN KEY (studio_id) REFERENCES studios(id)
 ); 

DROP TABLE IF EXISTS nominations;
CREATE TABLE nominations (
	id SERIAL PRIMARY KEY,
    title VARCHAR(250)
);

DROP TABLE IF EXISTS awards;
CREATE TABLE awards (
	id SERIAL PRIMARY KEY,
    movie_id BIGINT UNSIGNED NOT NULL,
    nomination_id BIGINT UNSIGNED NOT NULL,
	title VARCHAR(100),
    date BIGINT UNSIGNED NOT NULL,

	CONSTRAINT awards_fk_movie FOREIGN KEY (movie_id) REFERENCES movies(id),
    CONSTRAINT awards_fk_nomnation FOREIGN KEY (nomination_id) REFERENCES nominations(id)
);


/* 3. Заполнение базы данных.*/

INSERT INTO movies (title_orig, title_rus, descr) VALUES 
('The Shawshank Redemption', 'Побег из Шоушенка', 'Выдающаяся драма о силе таланта, важности дружбы, стремлении к свободе и Рите Хэйворт'),
('The Green Mile', 'Зелёная миля', 'В тюрьме для смертников появляется заключенный с божественным даром. Мистическая драма по роману Стивена Кинга'),
('The Lord of the Rings: The Return of the King', 'Властелин колец: Возвращение Короля', 'Арагорн штурмует Мордор, а Фродо устал бороться с чарами кольца. Эффектный финал саги, собравший 11 «Оскаров»'),
('Interstellar', 'Интерстеллар', 'Фантастический эпос про задыхающуюся Землю, космические полеты и парадоксы времени. «Оскар» за спецэффекты'),
('The Lord of the Rings: The Fellowship of the Ring', 'Властелин колец: Братство кольца', 'Фродо Бэггинс отправляется спасать Средиземье. Первая часть культовой фэнтези-трилогии Питера Джексона'),
('The Lord of the Rings: The Two Towers', 'Властелин колец: Две крепости', 'Голлум ведет хоббитов в Мордор, а великие армии готовятся к битве. Два «Оскара»'),
("Schindler's List", 'Список Шиндлера', 'Драма о холокосте и великом человеческом поступке'),
('Forrest Gump', 'Форрест Гамп', 'Том Хэнкс исполняет американскую мечту'),
('Sen to Chihiro no kamikakushi', 'Унесённые призраками', 'Девочка должна спасти своих родителей в мире духов. Шедевр Хаяо Миядзаки, фаворит анимационных рейтингов мира'),
('Intouchables', '1+1', 'Бывший зек возвращает вкус к жизни чопорному аристократу, прикованному к инвалидному креслу');

INSERT INTO meta_info (movie_id, year, country, genre, director, composer, budget) VALUES 
(1, 1994, 'США', 'драма', 'Фрэнк Дарабонт', 'Томас Ньюман', 25000000),
(2, 1999, 'США', 'фэнтези, драма, криминал, детектив', 'Фрэнк Дарабонт', 'Томас Ньюман', 60000000),
(3, 2003, 'Новая Зеландия, США', 'фэнтези, приключения, драма', 'Питер Джексон', 'Говард Шор', 94000000),
(4, 2014, 'США, Великобритания, Канада', 'фантастика, драма, приключения', 'Кристофер Нолан', 'Ханс Циммер', 165000000),
(5, 2001, 'США, Новая Зеландия', 'фэнтези, приключения, драма', 'Питер Джексон', 'Говард Шор', 93000000),
(6, 2002, 'Новая Зеландия, США', 'фэнтези, приключения, драма', 'Питер Джексон', 'Говард Шор', 94000000),
(7, 1993, 'США', 'драма, биография, история, военный', 'Стивен Спилберг', 'Джон Уильямс', 22000000),
(8, 1994, 'США', 'драма, мелодрама, комедия, история, военный', 'Роберт Земекис', 'Алан Сильвестри', 55000000),
(9, 2001, 'Япония', 'аниме, мультфильм, фэнтези, приключения, семейный', 'Хаяо Миядзаки', 'Дзё Хисаиси', 19000000),
(10, 2011, 'Франция', 'драма, комедия, биография', 'Оливье Накаш, Эрик Толедано', 'Людовико Эйнауди', 9500000);

INSERT INTO genres (genre_name) VALUES 
('аниме'), 
('биография'), 
('боевик'), 
('вестерн'), 
('военный'), 
('детектив'), 
('детский'), 
('документальный'), 
('драма'), 
('история'), 
('кинокомикс'), 
('комедия'), 
('концерт'), 
('короткометражный'), 
('криминал'), 
('мелодрама'), 
('мистика'), 
('мультфильм'), 
('мюзикл'), 
('научный'), 
('нуар'), 
('приключения'), 
('семейный'), 
('трилер'), 
('ужасы'), 
('фантастика'), 
('фэнтези'); 

INSERT INTO movie_genres (movie_id, genre_id) VALUES 
(1, 9),
(2, 9),
(2, 27),
(2, 15),
(2, 6),
(3, 27),
(3, 22),
(3, 9),
(4, 26),
(4, 9),
(4, 22),
(5, 27),
(5, 22),
(5, 9),
(6, 27),
(6, 22),
(6, 9),
(7, 9),
(7, 2),
(7, 10),
(7, 5),
(8, 9),
(8, 16),
(8, 12),
(8, 10),
(8, 5),
(9, 1),
(9, 18),
(9, 27),
(9, 22),
(9, 23), 
(10, 9),
(10, 12),
(10, 2);

INSERT INTO countries (country_name) VALUES 
('США'),
('Новая Зеландия'),
('Япония'),
('Франция'),
('Великобритания'), 
('Канада');

INSERT INTO movie_countries (movie_id, country_id) VALUES 
(1, 1),
(2, 1),
(3, 2),
(3, 1),
(4, 1),
(4, 5),
(4, 6),
(5, 1),
(5, 2),
(6, 2),
(6, 1),
(7, 1),
(8, 1),
(9, 3),
(10, 4);

INSERT INTO studios (studio_name) VALUES
('Castle Rock Entertainment'),
('Darkwoods Productions'), 
('Warner Bros. Pictures'), 
('New Line Cinema'), 
('The Saul Zaentz Company'), 
('WingNut Films'), 
('Legendary Pictures'), 
('Lynda Obst Productions'), 
('Paramount Pictures'), 
('Syncopy'), 
('Lord Zweite Productions Deutschland Filmproduktion GmbH & Co. KG'), 
('Amblin Entertainment'), 
('Universal Pictures'), 
('Canal+ [fr]'), 
('Chaocorp'), 
('Ciné Cinémas'), 
('Gaumont'), 
('Quad Productions'), 
('Ten Films'), 
('TF1'), 
('TF1 Films Production'), 
('Buena Vista International'), 
('DENTSU Music And Entertainment Inc.'), 
('Mitsubishi Commercial Affairs'), 
('Nippon Television Network'), 
('Studio Ghibli'), 
('Tohokushinsha Film Corp.'), 
('Tokuma Shoten');

INSERT INTO movie_studios (movie_id, studio_id) VALUES
(1, 1),
(2, 1),
(2, 2),
(2, 3),
(3, 4),
(3, 5),
(3, 6),
(4, 7),
(4, 8),
(4, 9),
(4, 10),
(4, 3),
(5, 4),
(5, 5),
(5, 6),
(6, 11),
(6, 4),
(6, 5),
(6, 6),
(7, 12),
(7, 13),
(8, 9),
(9, 22),
(9, 23),
(9, 24),
(9, 25),
(9, 26),
(9, 27),
(9, 28),
(10, 14),
(10, 15),
(10, 16),
(10, 17),
(10, 18),
(10, 19),
(10, 20),
(10, 21);

INSERT INTO nominations (title) VALUES
('Лучший анимационный фильм'), 
('Золотой Медведь'), 
('Лучший сценарий'), 
('Лучший фильм на иностранном языке'), 
('Лучшая музыка'), 
('Лучшая актриса второго плана'), 
('Лучший приключенческий фильм, боевик или триллер'), 
('Лучшее специальное DVD-издание'), 
('Лучший фильм'), 
('Лучший режиссер'), 
('Лучший адаптированный сценарий'), 
('Лучшие декорации'), 
('Лучшие костюмы'), 
('Лучший звук'), 
('Лучший монтаж'), 
('Лучшие визуальные эффекты'), 
('Лучший грим'), 
('Лучшая песня'), 
('Лучший оригинальный саундтрек'), 
('Лучший саундтрек'), 
('Лучшая экшн-сцена'), 
('Лучшая работа оператора'), 
('Приз зрительских симпатий'), 
('Лучшая зарубежная драма'),
('Лучший научно-фантастический фильм'), 
('Лучший молодой актер/актриса'), 
('Лучшие спецэффекты'), 
('Прорыв года'), 
('Премия имени Дэвида Лина за достижения в режиссуре'), 
('Лучший фэнтези-фильм'), 
('Лучший монтаж звука'), 
('Лучший виртуальный персонаж'), 
('Лучшая экранная команда'), 
('Лучший актер второго плана'), 
('Лучшая мужская роль второго плана'), 
('Лучшая мужская роль'), 
('Лучшая зарубежная комедия'), 
('Лучшая зарубежная драма'), 
('Лучший европейский фильм'), 
('Лучший актер'), 
('Лучший грим/прически');

INSERT INTO awards (movie_id, nomination_id, title, date) VALUES
(2, 36, 'Сатурн', 2000),
(2, 6, 'Сатурн', 2000),
(2, 7, 'Сатурн', 2000),
(3, 8, 'Сатурн', 2005),
(3, 9, 'Оскар', 2004),
(3, 10, 'Оскар', 2004),
(3, 11, 'Оскар', 2004),
(3, 12, 'Оскар', 2004),
(3, 13, 'Оскар', 2004),
(3, 14, 'Оскар', 2004),
(3, 15, 'Оскар', 2004),
(3, 16, 'Оскар', 2004),
(3, 17, 'Оскар', 2004),
(3, 18, 'Оскар', 2004),
(3, 19, 'Оскар', 2004),
(3, 9, 'Золотой глобус', 2004),
(3, 10, 'Золотой глобус', 2004),
(3, 18, 'Золотой глобус', 2004),
(3, 20, 'Золотой глобус', 2004),
(3, 9, 'Премия канала «MTV»', 2004),
(3, 21, 'Премия канала «MTV»', 2004),
(3, 9, 'Британская академия', 2004),
(3, 11, 'Британская академия', 2004),
(3, 22, 'Британская академия', 2004),
(3, 16, 'Британская академия', 2004),
(3, 23, 'Британская академия', 2004),
(3, 30, 'Сатурн', 2004),
(3, 10, 'Сатурн', 2004),
(3, 40, 'Сатурн', 2004),
(3, 34, 'Сатурн', 2004),
(3, 3, 'Сатурн', 2004),
(3, 27, 'Сатурн', 2004),
(3, 5, 'Сатурн', 2004),
(3, 17, 'Сатурн', 2004),
(4, 18, 'Оскар', 2015),
(4, 18, 'Британская академия', 2015),
(4, 24, 'Жорж', 2015),
(4, 25, 'Сатурн', 2015),
(4, 26, 'Сатурн', 2015),
(4, 3, 'Сатурн', 2015),
(4, 5, 'Сатурн', 2015),
(4, 27, 'Сатурн', 2015),
(4, 12, 'Сатурн', 2015),
(5, 8, 'Сатурн', 2003),
(5, 22, 'Оскар', 2002),
(5, 16, 'Оскар', 2002),
(5, 17, 'Оскар', 2002),
(5, 19, 'Оскар', 2002),
(5, 9, 'Премия канала «MTV»', 2002),
(5, 28, 'Премия канала «MTV»', 2002),
(5, 9, 'Британская академия', 2002),
(5, 16, 'Британская академия', 2002),
(5, 41, 'Британская академия', 2002),
(5, 29, 'Британская академия', 2002),
(5, 23, 'Британская академия', 2002),
(5, 30, 'Сатурн', 2002),
(5, 10, 'Сатурн', 2002),
(5, 34, 'Сатурн', 2002),
(5, 35, 'Премия Гильдии актеров', 2002),
(6, 8, 'Сатурн', 2004),
(6, 31, 'Оскар', 2003),
(6, 16, 'Оскар', 2003),
(6, 9, 'Премия канала «MTV»', 2003),
(6, 21, 'Премия канала «MTV»', 2003),
(6, 32, 'Премия канала «MTV»', 2003),
(6, 33, 'Премия канала «MTV»', 2003),
(6, 13, 'Британская академия', 2003),
(6, 16, 'Британская академия', 2003),
(6, 23, 'Британская академия', 2003),
(6, 30, 'Сатурн', 2003),
(6, 34, 'Сатурн', 2003),
(6, 13, 'Сатурн', 2003),
(6, 17, 'Сатурн', 2003),
(7, 9, 'Оскар', 1994),
(7, 10, 'Оскар', 1994),
(7, 11, 'Оскар', 1994),
(7, 22, 'Оскар', 1994),
(7, 12, 'Оскар', 1994),
(7, 15, 'Оскар', 1994),
(7, 19, 'Оскар', 1994),
(7, 9, 'Золотой глобус', 1994),
(7, 10, 'Золотой глобус', 1994),
(7, 3, 'Золотой глобус', 1994),
(7, 9, 'Британская академия', 1994),
(7, 35, 'Британская академия', 1994),
(7, 11, 'Британская академия', 1994),
(7, 22, 'Британская академия', 1994),
(7, 15, 'Британская академия', 1994),
(7, 20, 'Британская академия', 1994),
(7, 29, 'Британская академия', 1994),
(8, 9, 'Оскар', 1995),
(8, 36, 'Оскар', 1995),
(8, 10, 'Оскар', 1995),
(8, 11, 'Оскар', 1995),
(8, 15, 'Оскар', 1995),
(8, 16, 'Оскар', 1995),
(8, 9, 'Золотой глобус', 1995),
(8, 36, 'Золотой глобус', 1995),
(8, 10, 'Золотой глобус', 1995),
(8, 16, 'Британская академия', 1995),
(8, 30, 'Сатурн', 1995),
(8, 34, 'Сатурн', 1995),
(8, 36, 'Премия Гильдии актеров', 1995),
(9, 1, 'Оскар', 2003),
(9, 1, 'Сатурн', 2003),
(9, 2, 'Берлинский кинофестиваль', 2002),
(10, 37, 'Жорж', 2013),
(10, 38, 'Жорж', 2013),
(10, 39, 'Гойя', 2013), 
(10, 40, 'Сезар', 2012);


/* 4. скрипты характерных выборок (включающие группировки, JOIN'ы, вложенные таблицы). */

/* 4.1. Подсчитать средний бюджет фильмов.*/

SELECT AVG(budget) FROM meta_info

/* 4.2. Вывести название фильма и год выхода в порядке убывания.*/

SELECT CONCAT(title_orig, ' | ', title_rus) AS Title, year AS Year FROM (movies INNER JOIN meta_info ON movies.id = meta_info.movie_id)
GROUP BY movies.id ORDER BY meta_info.year DESC

/* 4.3. Вывести название фильма и бюджет в порядке убывания.*/

SELECT CONCAT(title_orig, ' | ', title_rus) AS Title, budget AS Budget FROM (movies INNER JOIN meta_info ON movies.id = meta_info.movie_id)
GROUP BY movies.id ORDER BY meta_info.budget DESC

/* 4.4. Вывести фильмы заданного жанра. */

SELECT CONCAT(title_orig, ' | ', title_rus) AS Title, genre AS Genre FROM (movies INNER JOIN meta_info ON movies.id = meta_info.movie_id)
WHERE genre LIKE '%драма%' ORDER BY Title 

/* 4.5. Вывести фильмы заданного режиссёра. */
SELECT title_rus AS Title, descr AS Description FROM (movies INNER JOIN meta_info ON movies.id = meta_info.movie_id) 
WHERE director = 'Стивен Спилберг'

/* 4.6. Средний бюджет фильмов заданного жанра. */

SELECT AVG(budget) AS Average_budget FROM (movies INNER JOIN meta_info ON movies.id = meta_info.movie_id)
WHERE genre LIKE '%фэнтези%'

/* 4.7. Общее количество наград для каждого фильма. */

SELECT (SELECT CONCAT(title_orig, ' | ', title_rus) FROM movies WHERE id = awards.movie_id) as Title, COUNT(*) AS Awards_amount FROM 
awards GROUP BY movie_id ORDER BY Awards_amount DESC;

/* 4.8. Количество отдельных наград для каждого фильма. */

SELECT CONCAT( (SELECT title_rus FROM movies WHERE id = awards.movie_id), ' (', title, ')') as Award,
COUNT(*) AS Amount FROM awards GROUP BY Award ORDER BY Award 


/* 5. Представления. */

/* 5.1. Фильм и соответствующая ему награда в номинации. */

CREATE OR REPLACE VIEW movie_award(Title, Nomination, Award) AS
SELECT (SELECT title_rus FROM movies WHERE id = awards.movie_id), 
(SELECT title FROM nominations WHERE id = awards.nomination_id), title FROM awards

/* 5.2. Фильм, год выхода, страна и студия производства. */

CREATE OR REPLACE VIEW movie_studio(Title, Year, Country, Studio) AS
SELECT title_rus, year, country, studio_name FROM (movies LEFT JOIN (meta_info LEFT JOIN (movie_studios LEFT JOIN studios ON movie_studios.studio_id = studios.id)
ON meta_info.movie_id = movie_studios.movie_id)
ON movies.id = meta_info.movie_id)
ORDER BY year DESC


/* 6. Хранимые процедуры / триггеры. */

/* 6.1. Если при создании записи в таблицах genres, countries и studios вводимое значение уже существует, операция отменяется. */

DROP TRIGGER IF EXISTS IfExistsGenre;
DELIMITER //
CREATE TRIGGER IfExistsGenre AFTER INSERT ON genres
FOR EACH ROW BEGIN
	IF NEW.genre_name IN (SELECT genre_name FROM genres) THEN
        SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'Genre already exists.'; 
	END IF;
END//
DELIMITER ;

DROP TRIGGER IF EXISTS IfExistsCountry;
DELIMITER //
CREATE TRIGGER IfExistsCountry AFTER INSERT ON countries
FOR EACH ROW BEGIN
	IF NEW.country_name IN (SELECT country_name FROM countries) THEN
        SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'Country already exists.'; 
	END IF;
END//
DELIMITER ;

DROP TRIGGER IF EXISTS IfExistsStudio;
DELIMITER //
CREATE TRIGGER IfExistsStudio AFTER INSERT ON studios
FOR EACH ROW BEGIN
	IF NEW.studio_name IN (SELECT studio_name FROM studios) THEN
        SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'Studio already exists.'; 
	END IF;
END//
DELIMITER ;


/* 6.2. Если текущий год чётный, вывести фильмы, вышедшие в чётном году. Если нечётный - фильмы, вышедшие в нечётном. */

DROP PROCEDURE IF EXISTS show_movie;
DELIMITER //
CREATE PROCEDURE show_movie()
BEGIN
	CASE 
		WHEN YEAR(CURDATE()) % 2 = 0 THEN
		SELECT title_rus, descr 
        FROM (movies INNER JOIN meta_info ON movies.id=meta_info.movie_id) 
        WHERE meta_info.year % 2 = 0;
		ELSE
		SELECT title_rus, descr 
        FROM (movies INNER JOIN meta_info ON movies.id=meta_info.movie_id) 
        WHERE meta_info.year % 2 != 0;
	END CASE;
END //
DELIMITER ;

/* 6.3. Вывести награды за режиссуру. */

DROP PROCEDURE IF EXISTS director_awards;
DELIMITER //
CREATE PROCEDURE director_awards()
BEGIN
	SELECT title_rus AS Title, director AS Director, date AS Date, nominations.title AS Nomination, awards.title AS Award 
	FROM (movies INNER JOIN (meta_info INNER JOIN (awards INNER JOIN nominations ON awards.nomination_id = nominations.id)
	ON meta_info.movie_id = awards.movie_id)
	ON movies.id = meta_info.movie_id) 
	WHERE nominations.title LIKE '%режисс%' ORDER BY date DESC, Award;
END //
DELIMITER ;








