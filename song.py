class Song:
    def __init__(self, title, artist, duration, file_path):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.file_path = file_path

    def __str__(self):
        return f"Título: {self.title}\nArtista: {self.artist}\nDuración: {self.duration}\nRuta del archivo: {self.file_path}"
