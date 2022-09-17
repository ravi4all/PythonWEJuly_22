movie_db = {
    "action" : ["hulk","thor","ironman","kgf","robot","pushpa","avengers","batman","superman","captain america"],
    "comedy" : ["dhamaal", "hera pheri", "golmaal", "golmaal 2", "golmaal 3"],
    "horror" : ["nun","ring","oculus","conjuring","golmaal"],
    "sci-fi" : ["interstellar","robot","ironman","avengers","time machine"]
}

user_1 = {"hulk","thor","batman","robot","golmaal","pushpa"}
user_2 = {"hulk","thor","kgf","avengers","golmaal","interstellar"}

commonMovies = user_1.intersection(user_2)
print(commonMovies)

# Jaccard Distance
scores = {}
for key in movie_db:
    movies = movie_db[key]
    movies = set(movies)
    numer = len(movies.intersection(commonMovies))
    denom = len(movies.union(commonMovies))
    scores[key] = numer/denom

print(scores)
category = max(scores, key=scores.get)

user_2_rec = set(user_1 - user_2).intersection(set(movie_db[category]))
user_1_rec = set(user_2 - user_1).intersection(set(movie_db[category]))

print(user_1_rec)
print(user_2_rec)