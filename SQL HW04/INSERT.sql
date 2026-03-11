-- Исполнители --
INSERT INTO public.artist(
	name)
	VALUES ('АЛЕКСАНДР ПАНАЙОТОВ');
INSERT INTO public.artist(
	name)
	VALUES ('АНДРЕЙ ПЕТРОВ');
INSERT INTO public.artist(
	name)
	VALUES ('ВИА_АРИЭЛЬ');
INSERT INTO public.artist(
	name)
	VALUES ('АЛЕКСАНДР ГРАДСКИЙ');
INSERT INTO public.artist(
	name)
	VALUES ('АЛЕКСЕЙ ЧУМАКОВ');

-- альбомы --
INSERT INTO public.album(
	name, yearof)
	VALUES ('АЛЕКСАНДР ПАНАЙОТОВ. ЛЕДИ ДОЖДЯ', 2006);

INSERT INTO public.album(
	name, yearof)
	VALUES ('АЛЕКСАНДР ПАНАЙОТОВ. ФОРМУЛА ЛЮБВИ', 2010);

INSERT INTO public.album(
	name, yearof)
	VALUES ('АЛЕКСАНДР ПАНАЙОТОВ. ХИТЫ', 2020);

INSERT INTO public.album(
	name, yearof)
	VALUES ('АНДРЕЙ ПЕТРОВ. ПЕСНИ',1966);

INSERT INTO public.album(
	name, yearof)
	VALUES ('АНДРЕЙ ПЕТРОВ. ПОЕТ ЭДУАРД ХИЛЬ',1968);

INSERT INTO public.album(
	name, yearof)
	VALUES ('АНДРЕЙ ПЕТРОВ. ПРОИЗВЕДЕНИЯ ДЛЯ СИМФОНИЧЕСКОГО ОРКЕСТРА',1971);


INSERT INTO public.album(
	name, yearof)
	VALUES ('ВИА АРИЭЛЬ. РУССКИЕ КАРТИНКИ',1977);

INSERT INTO public.album(
	name, yearof)
	VALUES ('ВИА АРИЭЛЬ. КАЖДЫЙ ДЕНЬ ТВОЙ',1982);

INSERT INTO public.album(
	name, yearof)
	VALUES ('ВИА АРИЭЛЬ. УТРО ПЛАНЕТЫ',1983);


INSERT INTO public.album(
	name, yearof)
	VALUES ('АЛЕКСАНДР ГРАДСКИЙ. МОЯ ЛЮБОВЬ НА ТРЕТЬЕМ КУРСЕ',1976);

INSERT INTO public.album(
	name, yearof)
	VALUES ('АЛЕКСАНДР ГРАДСКИЙ. ЭЛТОН ДЖОН',1979);

INSERT INTO public.album(
	name, yearof)
	VALUES ('АЛЕКСАНДР ГРАДСКИЙ. НАМ НЕ ЖИТЬ ДРУГ БЕЗ ДРУГА',1983);


INSERT INTO public.album(
	name, yearof)
	VALUES ('АЛЕКСЕЙ ЧУМАКОВ. СНЫ О ЧЕМ-ТО БОЛЬШЕМ',2006);
INSERT INTO public.album(
	name, yearof)
	VALUES ('АЛЕКСЕЙ ЧУМАКОВ. ТУТ И ТАМ',2013);
INSERT INTO public.album(
	name, yearof)
	VALUES ('АЛЕКСЕЙ ЧУМАКОВ. ЛУЧШИЕ ПЕСНИ',2019);

-- Жанры --
INSERT INTO public.genre(
	name)
	VALUES ('POP');

INSERT INTO public.genre(
	name)
	VALUES ('CLASSIC');
INSERT INTO public.genre(
	name)
	VALUES ('FILM SOUND');
INSERT INTO public.genre(
	name)
	VALUES ('SOUL');
INSERT INTO public.genre(
	name)
	VALUES ('JAZZ');
INSERT INTO public.genre(
	name)
	VALUES ('FUNK');
INSERT INTO public.genre(
	name)
	VALUES ('RnB');
INSERT INTO public.genre(
	name)
	VALUES ('LOUNGE');

-- Сборники --
INSERT INTO public.collection(
	name, yearof)
	VALUES ('НОВЫЙ ГОД 2023',2024);
INSERT INTO public.collection(
	name, yearof)
	VALUES ('НАРОДНЫЙ АРТИСТ.ЛУЧШЕЕ',2001);
INSERT INTO public.collection(
	name, yearof)
	VALUES ('ЛУЧШИЕ ПЕСНИ ИЗ КИНОФИЛЬМОВ',2019);
INSERT INTO public.collection(
	name, yearof)
	VALUES ('ЛУЧШИЕ ХИТЫ 70-Х',2000);

-- Треки --
INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Леди дождя', 180, 1);

INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Лунная мелодия', 185, 1);

INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Балалайка', 179, 1);

INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Она', 180, 2 );
INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Формула любви', 190, 2 );
INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Снег', 180, 2 );


INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Голос', 220, 3 );
INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Радио', 182, 3 );
INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Супергерой', 185, 3 );

INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Осень', 180, 4 );
INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Голубые города', 180, 4 );
INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Русский сувенир', 180, 4 );

INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Песня о моем отце', 180, 5 );
INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Песня о любви', 180, 5 );
INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Земля людей', 180, 5 );

INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Vivace', 180, 6 );
INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Moderato', 180, 6 );
INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Allegro', 180, 6 );

INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Аленушка', 180, 7 );
INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Скоморошина', 180, 7 );
INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Частушки', 180, 7 );

INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Ты-музыка', 180, 8 );
INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Шире круг', 180, 8 );
INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Каждый день твой', 180, 8 );

INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Вступление', 180, 9 );
INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Утро планеты', 180, 9 );
INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Гроза', 180, 9 );

INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('мой трек №1', 180, 10 );
INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Track 2', 180, 10 );
INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Track 3', 180, 10 );

INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Elton John 1', 180, 11 );
INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Elton John 2', 180, 11 );
INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Elton John 3', 180, 11 );

INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Колыбельная', 180, 12 );
INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Самба', 180, 12 );
INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Бардовская', 180, 12 );

INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Черные глаза', 180, 13 );
INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Сны о чем-то большем', 180, 13 );
INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Балалайка', 180, 13 );

INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Моя весна', 180, 14 );
INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Загадай', 180, 14 );
INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Тут и там', 180, 14 );

INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Эти глаза напротив', 180, 15 );
INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Скажи зачем', 180, 15 );
INSERT INTO public.track(
	name, timeof, album_id)
	VALUES('Одиночество', 180, 15 );

-- Исполнитель-альбом
INSERT INTO public.artist_album(
	artist_id, album_id)
	VALUES (1,1);
INSERT INTO public.artist_album(
	artist_id, album_id)
	VALUES (1,2);
INSERT INTO public.artist_album(
	artist_id, album_id)
	VALUES (1,3);

INSERT INTO public.artist_album(
	artist_id, album_id)
	VALUES (2,4);
INSERT INTO public.artist_album(
	artist_id, album_id)
	VALUES (2,5);
INSERT INTO public.artist_album(
	artist_id, album_id)
	VALUES (2,6);

INSERT INTO public.artist_album(
	artist_id, album_id)
	VALUES (3,7);
INSERT INTO public.artist_album(
	artist_id, album_id)
	VALUES (3,8);
INSERT INTO public.artist_album(
	artist_id, album_id)
	VALUES (3,9);

INSERT INTO public.artist_album(
	artist_id, album_id)
	VALUES (4,10);
INSERT INTO public.artist_album(
	artist_id, album_id)
	VALUES (4,11);
INSERT INTO public.artist_album(
	artist_id, album_id)
	VALUES (4,12);

INSERT INTO public.artist_album(
	artist_id, album_id)
	VALUES (5,13);
INSERT INTO public.artist_album(
	artist_id, album_id)
	VALUES (5,14);
INSERT INTO public.artist_album(
	artist_id, album_id)
	VALUES (5,15);

-- Исполнитель-жанр --
INSERT INTO public.genre_artist(
	genre_id, artist_id)
	VALUES (1,1);
INSERT INTO public.genre_artist(
	genre_id, artist_id)
	VALUES (4,1);
INSERT INTO public.genre_artist(
	genre_id, artist_id)
	VALUES (5,1);

INSERT INTO public.genre_artist(
	genre_id, artist_id)
	VALUES (3,2);

INSERT INTO public.genre_artist(
	genre_id, artist_id)
	VALUES (1,3);
INSERT INTO public.genre_artist(
	genre_id, artist_id)
	VALUES (8,3);

INSERT INTO public.genre_artist(
	genre_id, artist_id)
	VALUES (1,4);
INSERT INTO public.genre_artist(
	genre_id, artist_id)
	VALUES (2,4);
INSERT INTO public.genre_artist(
	genre_id, artist_id)
	VALUES (3,4);

INSERT INTO public.genre_artist(
	genre_id, artist_id)
	VALUES (1,5);
INSERT INTO public.genre_artist(
	genre_id, artist_id)
	VALUES (2,5);
INSERT INTO public.genre_artist(
	genre_id, artist_id)
	VALUES (4,5);
INSERT INTO public.genre_artist(
	genre_id, artist_id)
	VALUES (5,5);
INSERT INTO public.genre_artist(
	genre_id, artist_id)
	VALUES (6,5);
INSERT INTO public.genre_artist(
	genre_id, artist_id)
	VALUES (8,5);

-- cборнит-трек --
INSERT INTO public.collection_track(
	collection_id, track_id)
	VALUES (1,1);
INSERT INTO public.collection_track(
	collection_id, track_id)
	VALUES (1,7);
INSERT INTO public.collection_track(
	collection_id, track_id)
	VALUES (1,10);

INSERT INTO public.collection_track(
	collection_id, track_id)
	VALUES (2,2);
INSERT INTO public.collection_track(
	collection_id, track_id)
	VALUES (2,14);
INSERT INTO public.collection_track(
	collection_id, track_id)
	VALUES (2,15);

INSERT INTO public.collection_track(
	collection_id, track_id)
	VALUES (3,4);
INSERT INTO public.collection_track(
	collection_id, track_id)
	VALUES (3,5);
INSERT INTO public.collection_track(
	collection_id, track_id)
	VALUES (3,6);

INSERT INTO public.collection_track(
	collection_id, track_id)
	VALUES (4,7);
INSERT INTO public.collection_track(
	collection_id, track_id)
	VALUES (4,8);
INSERT INTO public.collection_track(
	collection_id, track_id)
	VALUES (4,12);
