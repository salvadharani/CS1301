#We've given you a file called "top500.txt" which contains
#the name and lifetime gross revenue of the top 500
#films at the time this question was written.
#
#Each line of the given file is formatted like so:
# <name>\t<gross revenue in dollars>
#
#In other words, you should call .split("\t") to split
#the line into the movie name (the first item) and the
#gross (the second item).
#
#Unfortunately, these movies are not in order. Write a
#function called "sort_films" that accepts two parameters:
#a string of a source filename and a string of a
#destination filename. Your function should open the
#source file and sort the contents from greatest gross
#revenue to least gross revenue, and write the sorted
#contents to the destination filename. You may assume the
#source file is correctly formatted.


#Write your function here!
def sort_films(filename, destination):
    file = open(filename, "r")
    movies = []
    for line in file:
        movies.append(line.strip().split("\t")) # results into list of lists
    file.close()
    revenues = []
    for movie in movies:
        revenues.append(int(movie[1]))
    revenues.sort()
    revenues.reverse()
    sorted_movies = []
    for revenue in revenues:
        for movie in movies:
            if revenue == int(movie[1]):
                sorted_movies.append(movie)
    fileout = open(destination, "w")
    for movie in sorted_movies:
        print(movie[0], "\t", movie[1], file = fileout)
    fileout.close()



#The line of code below will test your function and put
#your results in top500result.txt. Then, it will print
#"Done!"
#print(sort_films("top500.txt"))

sort_films("top500.txt", "top500result.txt")
print("Done!")





