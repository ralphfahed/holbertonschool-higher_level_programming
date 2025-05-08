-- Script to list all shows and their linked genres, with NULL if no genre is linked

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
-- Left join with tv_show_genres to get the show-genre relationships
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Left join with tv_genres to get the genre names
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
-- Sorting the results by show title and genre name in ascending order
ORDER BY tv_shows.title ASC, tv_genres.name ASC;

