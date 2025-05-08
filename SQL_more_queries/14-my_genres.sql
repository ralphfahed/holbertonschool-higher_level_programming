-- Script to list all genres of the show 'Dexter'
-- The results will display genre names sorted in ascending order

-- Selecting the genre name from tv_genres table
SELECT tv_genres.name
FROM tv_genres
-- Joining tv_genres table with tv_show_genres table on genre_id
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
-- Joining tv_show_genres table with tv_shows table on show_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
-- Filtering for the show titled 'Dexter'
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
