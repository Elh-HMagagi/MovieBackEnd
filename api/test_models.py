#%%
from database import SessionLocal
from models import Movie, Rating, Tag, Link

db = SessionLocal()



#%%
### Test de la récupération des Films
# movies = db.query(Movie).limit(10).all()
# movies

movies = db.query(Movie).limit(10).all()
for movie in movies:
    print(f"ID :{movie.movieId}, Titre : {movie.title}, Genre :{movie.genres}")



# %%
# recuperation des  films du genre action 

action_movies =db.query(Movie).filter(Movie.genres.contains("Action")).limit(5).all()

for movie in action_movies:
    print(f"ID :{movie.movieId}, Titre : {movie.title}, Genre :{movie.genres}")

# %%
# Test de la recuperation des evaluations 

# movie_rating = db.query(Rating).limit(5).all()
# for m_rating in movie_rating:
#     print(f"ID:{m_rating.movieId},Rating:{m_rating.rating}")

#Recuperation des 5 premier films dont la note est > 5
movie_rating = db.query(Rating).filter(Rating.rating>=5).limit(5).all()
for m_rating in movie_rating:
    print(f"Movie_ID:{m_rating.movieId},Movie_Rating:{m_rating.rating}")

#Recuperation des 10 meilleurs films avec une note >= 4 au moyen des jointures
Top_10_Films = (
    db.query(Movie.title, Rating.rating)
    .join(Rating)
    .filter(Rating.rating >= 4,Movie.genres=="Action")
    .limit(10)
    .all()
)

for title, rating in Top_10_Films:
    print(f"title:{title},Rating:{rating}")


# %%
#Test de la recuperation de quelque Tags

movie_tags = db.query(Tag).limit(5).all()
for mv_tags in movie_tags:
    print(f"ID:{mv_tags.userId},Movie_ID:{mv_tags.movieId}, Movie_tag:{mv_tags.tag}")


# %%
#Test de la recuperation des liens 

movie_link = db.query(Link).limit(5).all()
for m_link in movie_link :
    print(f"Movi_ID:{m_link.movieId},Imdb_ID:{m_link.imdbId},Tmdb_ID:{m_link.tmdbId}")

# %%
#fermeture de la session
db.close()

# %%
