# func2
movies = [
    {"title": "Usual Suspects", "rating": 7.0, "genre": "Thriller"},
    {"title": "Hitman", "rating": 6.3, "genre": "Action"},
    {"title": "Dark Knight", "rating": 9.0, "genre": "Adventure"},
    {"title": "The Help", "rating": 8.0, "genre": "Drama"},
    {"title": "The Choice", "rating": 6.2, "genre": "Romance"},
    {"title": "Colonia", "rating": 7.4, "genre": "Romance"},
    {"title": "Love", "rating": 6.0, "genre": "Romance"},
    {"title": "Bride Wars", "rating": 5.4, "genre": "Romance"},
    {"title": "AlphaJet", "rating": 3.2, "genre": "War"},
    {"title": "Ringing Crime", "rating": 4.0, "genre": "Crime"},
    {"title": "Joking muck", "rating": 7.2, "genre": "Comedy"},
    {"title": "What is the name", "rating": 9.2, "genre": "Suspense"},
    {"title": "Detective", "rating": 7.0, "genre": "Suspense"},
    {"title": "Exam", "rating": 4.2, "genre": "Thriller"},
    {"title": "We Two", "rating": 7.2, "genre": "Romance"}
]

# >5.5
def is_high_rated(movie):
    return movie["rating"] > 5.5

# back if >5,5
def get_high_rated_movies(movie_list):
    return [movie["title"] for movie in movie_list if is_high_rated(movie)]

# genre
def get_movies_by_genre(movie_list, genre):
    return [movie["title"] for movie in movie_list if movie["genre"] == genre]

# avg
def calculate_average_rating(movie_list):
    return sum(movie["rating"] for movie in movie_list) / len(movie_list)

# avg genre
def calculate_genre_average(movie_list, genre):
    genre_movies = [movie["rating"] for movie in movie_list if movie["genre"] == genre]
    return sum(genre_movies) / len(genre_movies) if genre_movies else 0

if __name__ == "__main__":
    print("Фильмы с рейтингом выше 5.5:", get_high_rated_movies(movies))
    print("Фильмы жанра 'Romance':", get_movies_by_genre(movies, "Romance"))
    print("Средний рейтинг всех фильмов:", calculate_average_rating(movies))
    print("Средний рейтинг фильмов 'Romance':", calculate_genre_average(movies, "Romance"))
