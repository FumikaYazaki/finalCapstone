#import spacy and model
import spacy
nlp = spacy.load('en_core_web_md')

#read text file
file = open("movies.txt", "r")
movies = file.read()
movies = movies.split("\n")

#Make a function
def similar_movie(description):
    
    similarities_list = []

    #Meadure similarlity scores for each movie and store the score in the list
    for movie in movies:
        movie_description = nlp(movie)
        similarities = movie_description.similarity(description)
        similarities_list.append(similarities)
    #Finf out the movie has the highest similarity score
    max_similarity = max(similarities_list)
    max_similarity_index = similarities_list.index(max_similarity)
    most_similar_movie = movies[max_similarity_index]
    return print("We reccommend you this movie to watch next:\n",most_similar_movie)

#The movie the user watched and its description     
Planet_hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator"
description = nlp(Planet_hulk)

#Print the recommended movie based on the description of the movie user watched
similar_movie(description)