SELECT name, timeof/60*1.00 as timeof_in_min 
	FROM public.track
	ORDER BY timeof desc
	LIMIT 1;

SELECT name, timeof/60*1.00 as timeof_in
	FROM public.track
	WHERE timeof >=3.5*60;

SELECT name 
	FROM public.collection
	WHERE yearof>=2018 AND yearof<=2020;

SELECT name 
	FROM public.artist
	WHERE NOT (name like '% %');

SELECT name 
	FROM public.track
	WHERE (name ilike 'my %' or name ilike 'мой %' or name ilike '% my' or name ilike '% мой' or name ilike '% my %' or name ilike '% мой %' or name ilike 'my' or name ilike 'мой'); 

-- ----------

SELECT genre.name, COUNT(genre_artist.artist_id) as artist_count
FROM public.genre_artist AS genre_artist
LEFT JOIN public.genre AS genre ON genre.id = genre_artist.genre_id
GROUP BY genre.name;

SELECT COUNT(track.id)
FROM public.track as track
LEFT JOIN public.album as album ON album.id = track.album_id
WHERE album.yearof between 2019 and 2020;


SELECT album.name, round(AVG(track.timeof)/60,2) as timeof_in
FROM public.track as track
LEFT JOIN public.album as album ON album.id = track.album_id
GROUP BY album.name;

SELECT artists.artistList, artists.cntAlbum
FROM
	(
	SELECT artist.name as artistList,
	COUNT(album.name) as cntAlbum
	FROM public.artist_album as artist_album
	LEFT JOIN public.artist as artist ON artist.id = artist_album.artist_id
	LEFT JOIN public.album as album ON album.id = artist_album.album_id AND album.yearof = 2020
	GROUP BY artist.name
	) as artists
WHERE artists.cntAlbum=0;

SELECT collection.name, track.name, album.name, artist.name 
FROM collection_track as collection_track
LEFT JOIN public.collection as collection ON collection.id = collection_track.collection_id
LEFT JOIN public.track as track on track.id = collection_track.track_id
left join public.album as album ON album.id = track.album_id
left join public.artist_album as artist_album ON artist_album.album_id = album.id
left join public.artist as artist ON artist.id = artist_album.artist_id

WHERE artist.name = 'АНДРЕЙ ПЕТРОВ';

-- ---------------

SELECT * FROM
	(
	SELECT album.name as albumName, Count(genre_artist.genre_id) as genreCnt
	FROM public.genre_artist as genre_artist
	LEFT JOIN public.artist as artist ON artist.id = genre_artist.artist_id
	LEFT JOIN public.artist_album as artist_album ON artist_album.artist_id = artist.id
	LEFT JOIN public.album as album ON album.id = artist_album.album_id
	GROUp BY album.name, genre_artist.artist_id
	) as genreList
WHERE (genreList.genreCnt) > 1;

SELECT track.name, collection_track.collection_id FROM public.track
LEFT JOIN public.collection_track as collection_track ON track.id = collection_track.track_id
WHERE collection_track.collection_id IS NULL;

SELECT artist.name, track.timeof FROM public.track
LEFT JOIN public.album as album on track.album_id = album.id
LEFT JOIN public.artist_album as artist_album on artist_album.album_id = album.id
LEFT JOIN public.artist as artist on artist_album.artist_id = artist.id 
WHERE track.timeof = 
	(
	SELECT min(timeof) FROM public.track
	);

SELECT album.name 
FROM public.album
LEFT JOIN public.track on track.album_id = album.id	
GROUP BY album.id 
HAVING COUNT(album_id) = 
	(
    SELECT COUNT(id) as count FROM public.track 
    GROUP BY album_id
    ORDER BY count 
    LIMIT 1
	);


