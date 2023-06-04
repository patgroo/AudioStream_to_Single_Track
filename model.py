class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def set_duration(self, duration):
        self.duration = duration

    def get_title(self):
        return self.title

    def get_artist(self):
        return self.artist

    def get_duration(self):
        return self.duration
