import yt_dlp

def download_audio(url):
    # Definir las opciones para yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',  # Descargar el mejor audio disponible
        'outtmpl': '%(title)s.%(ext)s',  # Nombre del archivo de salida
        'postprocessors': [{
            'key': 'FFmpegAudioConvertor',  # Convertir el audio
            'preferredcodec': 'mp3',        # Convertir a mp3
            'preferredquality': '192',      # Calidad del mp3
        }],
    }

    # Intentar descargar el audio
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("¡Descarga completada!")
    except Exception as e:
        print(f"Se produjo un error: {e}")

if __name__ == "__main__":
    url = input("Introduce la URL del video de YouTube: ")
    download_audio(url)
