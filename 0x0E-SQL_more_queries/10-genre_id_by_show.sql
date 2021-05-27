-- lists all shows contained in hbtn_0d_tvshows that have at least one genre
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_shows_genres
ON tv_shows_genres.show_id = tv_shows.
ORDER BY tv_shows.title, tv_show_genres.genre_id;