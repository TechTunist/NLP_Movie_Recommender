# create function to return recommended movies based on the description below
import spacy

# target description
description = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the illuminati trick Julk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planey Sakaar where he is sold into slavery and trained as a gladiator."""

# function that takes in a target description and recommends a movie to watch next based on its description
def recommender(description):

    # load the language model
    nlp = spacy.load('en_core_web_md')

    # read in text file 'movies.txt' and create a list of descriptions
    with open('movies.txt', 'r') as f:
        lines = f.readlines()

    # create a dictionary and add the movie name as a key with the description as a value
    sentences_dict = {}
    for i in range(len(lines)):
        sentences_dict[lines[i].split(':')[0]] = lines[i].split(':')[1]

    # create a target sentence to compare
    model_sentence = nlp(description)

    # create a dictionary of movies with their respective scores as values
    score_dict = {}
    for key, val in sentences_dict.items():
        similarity = nlp(val).similarity(model_sentence)
        score_dict[key] = round(similarity, 3)

    return max(score_dict, key=score_dict.get)

print(f"\nThe movie I recommend you watch next is : {recommender(description)}")




