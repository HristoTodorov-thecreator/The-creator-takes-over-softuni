
def movie_organizer(*args):

    movies = {}
    for name,g in args:
        if g not in movies:
            movies[g] = []
        movies[g].append(name)

    sorted_genres = sorted(movies.items(), key=lambda x: (-len(x[1]), x[0]))

    result = []

    for g,s in sorted_genres:
        s.sort()
        result.append(f"{g} - {len(s)}")
        for movie in s:
            result.append(f"* {movie}")

    return "\n".join(result)





print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))