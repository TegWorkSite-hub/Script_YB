import yt_dlp

def descargar_audio(url):
    try:
        # Configuración para solo audio
        ydl_opts = {
            'format': 'bestaudio/best',  # Selecciona el mejor audio disponible
            'postprocessors': [{
                'key': 'FFmpegAudioConvertor',  # Usar FFmpeg para convertir el audio
                'preferredcodec': 'mp3',  # Formato de salida: mp3
                'preferredquality': '192',  # Calidad del audio
            }],
            'outtmpl': '%(title)s.%(ext)s',  # Nombre del archivo: título del video
        }

        # Descargar el audio
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print("¡Descarga completa!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = input("Introduce la URL del video de YouTube: ")
    descargar_audio(url)
