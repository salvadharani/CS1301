# We've given you a class called "Song" that represents
# some basic information about a song. We also wrote a
# class called "Artist" which contains some basic
# information about an artist. Your job is to do the
# following:
#
# 1. Create a song object with the following attributes:
#       name = "You Belong With Me"
#       album = "Fearless"
#       year = 2008
#       artist.name = "Taylor Swift"
#       artist.label = "Big Machine Records, LLC"
# Store this song object in a variable named "song_1"
# Hint: You'll first need to make an Artist object
#
# 2. Create another song object with the following
#    attributes:
#       name = "All Too Well"
#       album = "Red"
#       year = 2012
#       artist = the same artist instance as song_1
# Store this song object in a variable named "song_2"
#
# 3. Finally, create another song object with the following
#    attributes:
#       name = "Up We Go"
#       album = "Midnight Machines"
#       year = 2016
#       artist.name = "LIGHTS"
#       artist.label = "Warner Bros. Records Inc."
# Store this song object in a variable named "song_3"
#
# When your code is done running, there should exist three
# variables: song_1, song_2, and song_3, according to the
# requirements above.

class Artist:
    def __init__(self, name, label):
        self.name = name
        self.label = label


class Song:
    def __init__(self, name, album, year, artist):
        self.name = name
        self.album = album
        self.year = year
        self.artist = artist

# Write your code here!

swift = Artist("Taylor Swift", "Big Machine Records, LLC")
song_1 = Song("You Belong With Me", "Fearless", 2008, swift)
song_2 = Song("All Too Well", "Red", 2012, swift)
song_3 = Song("Up We Go", "Midnight Machines", 2016, Artist("LIGHTS", "Warner Bros. Records Inc."))

# Feel free to add code to test your code below.

for song in [song_1, song_2, song_3]:
    print(song.name, song.album, song.year, song.artist.name, song.artist.label)
