-- Script that lists all shows and their linked genre_id
-- Results are sorted by tv_shows.title and tv_show_genres.genre_id
-- Shows with no linked genre will have NULL for genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
