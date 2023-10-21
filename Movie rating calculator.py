
movie_ratings = {}

while True:
    title = input("Enter a movie title (or 'q' to quit): ")
    
    if title.lower() == 'q':
        break
    
    rating = float(input("Enter a rating (1-5): "))
    
    if title in movie_ratings:
        movie_ratings[title] = (rating)
        print(movie_ratings)
    else:
        movie_ratings[title] = rating
