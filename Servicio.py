from utils import descargar_audio, descargar_playlist, verificar_enlace


class Servicio:
    ruta_descarga = './canciones'
    songs = []
    def __init__(self):
        pass

    def add_song(self, url):
        tipo_enlace = verificar_enlace(url)
        if tipo_enlace == "cancion":
            self.songs.append(descargar_audio(url, self.ruta_descarga))
        elif tipo_enlace == "playlist":
            descargar_playlist(url, self.ruta_descarga)
        else:
            print("Enlace inválido")

    def get_song(self):
        if not self.songs:
            print("No hay canciones en la lista")
            return None
        return self.songs.pop(0)
