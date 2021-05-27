--  lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genres.name AS genre, COUNT(*) AS number_shows
INNER JOIN tv_genres ON tv_genre.id=tv_show_genres.genre.id
GROUP BY tv_genres.name ORDER BY number_shows DESC;