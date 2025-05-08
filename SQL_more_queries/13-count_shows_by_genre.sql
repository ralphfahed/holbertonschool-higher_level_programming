-- Select the genre name from the tv_genres table and rename it as 'genre'
-- Also count how many times each genre is linked to a show using COUNT()
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows

-- Perform a LEFT JOIN between tv_genres and tv_show_genres
-- This means we'll get all genres, even those that may have no linked shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id

-- Group the result by genre ID so that COUNT() is calculated per genre
GROUP BY tv_genres.id

-- Only keep the genres that have at least one linked show
HAVING number_of_shows > 0

-- Order the results by number of linked shows, from most to least
ORDER BY number_of_shows DESC;

