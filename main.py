import os
from pytube import YouTube, Playlist

# URL de la playlist de YouTube
playlist_url = 'https://music.youtube.com/playlist?list=PLvozzQtjAFILHv_oG0gzYVZ6r7NTlK-tQ'


# Función para descargar una playlist
def descargar_playlist(url, ruta_descarga):
    try:
        playlist = Playlist(url)
        print(f"Descargando playlist: {playlist.title}")

        # Crear un directorio para la playlist
        ruta_playlist = os.path.join(ruta_descarga, playlist.title)
        os.makedirs(ruta_playlist, exist_ok=True)

        # Descargar cada video de la playlist
        for video in playlist.videos:
            descargar_audio(video.watch_url, ruta_playlist)

        print(f"Descarga de la playlist '{playlist.title}' completada.")
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

        print(f"Descarga completada: {nuevo_archivo}")
    except Exception as e:
        print(f"Error al descargar el video: {e}")


ruta_descarga = './canciones'

# Llamar a la función para descargar la playlist
descargar_playlist(playlist_url, ruta_descarga)
# Ruta de descarga (puedes cambiarla según tus necesidades)


