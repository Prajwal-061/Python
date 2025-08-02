movie_ratings={}

with open("movie_ratings.csv","r") as f:
    for line in f:
        movie_name,_,rating=line.split(",")
        rating=int(rating.strip())
        if movie_name in movie_ratings:
            movie_ratings[movie_name].append(rating)
        else:
            movie_ratings[movie_name]=[rating]
print(movie_ratings)

for name,rating_list in movie_ratings.items():
    min_value=min(rating_list)
    max_value=max(rating_list)
    avg=sum(rating_list)/len(rating_list)
    print(f"{name}==> Min:{min_value},Max:{max_value},Average={avg}")