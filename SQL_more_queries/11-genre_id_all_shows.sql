-- Script that lists all shows and their linked genre_id
-- Results are sorted by tv_shows.title and tv_show_genres.genre_id

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres
WHERE tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
