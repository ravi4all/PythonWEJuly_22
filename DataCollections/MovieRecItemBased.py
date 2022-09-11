movie_db = {
    "action" : ["hulk","thor","ironman","kgf","robot","pushpa","avengers","batman","superman","captain america"],
    "comedy" : ["dhamaal", "hera pheri", "thor", "golmaal"],
    "horror" : ["nun","ring","oculus","conjuring","golmaal"],
    "sci-fi" : ["interstellar","robot","ironman","avengers","time machine"]
}

user = {"hulk","thor","batman","robot","golmaal","pushpa"}

# Jaccard Distance
scores = {}
for key in movie_db:
    movies = movie_db[key]
    movies = set(movies)
    numer = len(movies.intersection(user))
    denom = len(movies.union(user))
    d = numer / denom
    scores[key] = d

print(scores)

max_value = max(scores.values())
for key in scores:
    if scores[key] == max_value:
        category = key
        break

recommended_movies = set(movie_db[category]) - user
print("Recommended Movies :",recommended_movies)
