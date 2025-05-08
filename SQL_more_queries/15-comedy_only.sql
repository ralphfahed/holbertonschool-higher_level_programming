-- Script to list all Comedy shows in the hbtn_0d_tvshows database

-- Selecting the title of TV shows related to the Comedy genre
SELECT tv_shows.title
FROM tv_shows
-- Joining tv_shows table with tv_show_genres table to connect shows with genres
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Joining tv_show_genres table with tv_genres table to get the genre details
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
-- Filtering to only include shows related to the Comedy genre
WHERE tv_genres.name = 'Comedy'
-- Sorting the results in ascending order by the title of the shows
ORDER BY tv_shows.title ASC;

