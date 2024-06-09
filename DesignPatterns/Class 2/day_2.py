class Song:
    def __init__(self, title, artist, duration=None):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return f"{song.title} by {song.artist} ({self.duration} seconds)"

    # for more official purposes (technical people)
    def __repr__(self):
        return f"Song({self.title}, {self.artist}, {self.duration})"

# Song("My heart will go on", "Celine Dion")


class SongBuilder:

    def __init__(self):
        self.title = None
        self.artist = None
        self.duration = None

    def with_title(self, title):
        self.title = title
        return self  # reference to the builder

    def with_artist(self, artist):
        self.artist = artist
        return self

    def with_duration(self, duration):
        self.duration = duration
        return self

    def build(self):
        if not self.title or not self.artist:
            raise ValueError("Title and artist are required to build a song!")
        return Song(self.title, self.artist, self.duration)


builder = SongBuilder()
song = builder.with_title("Love me you like you do")\
    .with_artist("Ellie Glouding")\
    .with_duration(560)\
    .build()

print(song)
