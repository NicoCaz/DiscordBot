import os
from pytube import YouTube, Playlist
from song import Song
# URL de la playlist de YouTube

def verificar_enlace(url):
    cad='playlist'
    try:
        if cad in url:
            return "playlist"
        else:
            return "cancion"
    except Exception as e:
        print(f"Error al verificar el enlace: {e}")
        return None

# Función para descargar una playlist
def descargar_playlist(url, ruta_descarga):
    songs = []
    try:
        playlist = Playlist(url)
        print(f"Descargando playlist: {playlist.title}")

        # Crear un directorio para la playlist
        ruta_playlist = os.path.join(ruta_descarga, playlist.title)
        os.makedirs(ruta_playlist, exist_ok=True)

        # Descargar cada video de la playlist
        for video in playlist.videos:
            song = descargar_audio(video.watch_url, ruta_playlist)
            if song:
                songs.append(song)

        print(f"Descarga de la playlist '{playlist.title}' completada.")
        return songs
    except Exception as e:
        print(f"Error al descargar la playlist: {e}")


# Función para descargar el audio de un video
def descargar_audio(url, ruta_descarga):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()

        print(f"Descargando: {yt.title}")
        print(f"Tamaño: {video.filesize / (1024 * 1024):.2f} MB")

        audio = video.download(output_path=ruta_descarga)
        base, ext = os.path.splitext(audio)
        nuevo_archivo = base + '.mp3'
        os.rename(audio, nuevo_archivo)

        song_info = Song(yt.title, yt.author, yt.length, nuevo_archivo)
        print(song_info)

        return song_info
    except Exception as e:
        print(f"Error al descargar el video: {e}")
        return None


