# create function to return recommended movies based on the description below
description = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the illuminati trick Julk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planey Sakaar where he is sold into slavery and trained as a gladiator."""


# read in text file 'movies.txt'
with open('movies.txt', 'r') as f:
    lines = f.readlines()


for i in lines:
    print(i)

