"""SQLAlchemy Query Functions for MovieLens API"""
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

import models

# --- Films ---
def get_movie(db: Session, movie_id: int):
    """Récupère un film par son ID."""
    return db.query(models.Movie).filter(models.Movie.movieId == movie_id).first()

def get_movies(db: Session, skip: int = 0, limit: int = 100, title: str = None, genre: str = None):
    """Récupère une liste de films avec filtres optionnels."""
    query = db.query(models.Movie)
    
    if title:
        query = query.filter(models.Movie.title.ilike(f"%{title}%"))
    if genre:
        query = query.filter(models.Movie.genres.ilike(f"%{genre}%"))
    
    return query.offset(skip).limit(limit).all()

# --- Évaluations ---
def get_rating(db: Session, rating_id: int):
    """Récupère une évaluation par son ID."""
    return db.query(models.Rating).filter(models.Rating.id == rating_id).first()

def get_ratings(db: Session, skip: int = 0, limit: int = 100, movie_id: int = None, user_id: int = None, min_rating: float = None):
    """Récupère une liste d'évaluations avec filtres optionnels."""
    query = db.query(models.Rating)
    
    if movie_id:
        query = query.filter(models.Rating.movieId == movie_id)
    if user_id:
        query = query.filter(models.Rating.userId == user_id)
    if min_rating:
        query = query.filter(models.Rating.rating >= min_rating)
    
    return query.offset(skip).limit(limit).all()

# --- Tags ---
def get_tag(db: Session, tag_id: int):
    """Récupère un tag par son ID."""
    return db.query(models.Tag).filter(models.Tag.id == tag_id).first()

def get_tags(db: Session, skip: int = 0, limit: int = 100, movie_id: int = None, user_id: int = None):
    """Récupère une liste de tags avec filtres optionnels."""
    query = db.query(models.Tag)
    
    if movie_id:
        query = query.filter(models.Tag.movieId == movie_id)
    if user_id:
        query = query.filter(models.Tag.userId == user_id)
    
    return query.offset(skip).limit(limit).all()

# --- Liens ---
def get_link(db: Session, movie_id: int):
    """Récupère les liens IMDB et TMDB pour un film donné."""
    return db.query(models.Link).filter(models.Link.movieId == movie_id).first()

def get_links(db: Session, skip: int = 0, limit: int = 100):
    """Récupère une liste de liens IMDB et TMDB."""
    return db.query(models.Link).offset(skip).limit(limit).all()

# --- Requêtes analytiques ---
def get_movie_count(db: Session):
    """Retourne le nombre total de films."""
    return db.query(models.Movie).count()

def get_rating_count(db: Session):
    """Retourne le nombre total d'évaluations."""
    return db.query(models.Rating).count()

def get_tag_count(db: Session):
    """Retourne le nombre total de tags."""
    return db.query(models.Tag).count()

def get_link_count(db: Session):
    """Retourne le nombre total de liens."""
    return db.query(models.Link).count()


