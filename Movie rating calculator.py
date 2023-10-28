import os
movie_ratings = {}
ratings = []
while True:
    try:
        title = input("Enter a movie title (or 'q' to quit): ")
        
        
        if title.lower() == 'q':
            break
        
        rating = float(input("Enter a rating (1-5): "))
        f = title.split()
        if title:
            movie_ratings[title] = rating
            ratings.append(rating)
            for i, f in enumerate(movie_ratings, start=0):
                i += 1
                print(f"{i}. {f}: {rating}")
        
        elif rating > 5:
            print("Please enter: 1-5")
        

        
    except ValueError:
        print("Value error: Try again")
        

# Calculate average ratings for each movie

    if rating == 5:
        pass

# Find the highest-rated and lowest-rated movies

# Create a menu for users to choose various operations, such as searching, listing, etc.

# Implement the selected operation and display the results
