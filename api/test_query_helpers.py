from database import SessionLocal
from query_helpers import *

db = SessionLocal()

# movie = get_movie(db,movie_id=1)
# print(movie.title)

n_movie = get_movie_count(db)
print(f"Nombre de total de film :{n_movie}")


db.close()