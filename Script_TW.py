import yt_dlp

def download_audio(url, download_path='./'):
    # Definir las opciones para yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',  # Descargar solo el mejor audio disponible
        'outtmpl': f'{download_path}%(title)s.%(ext)s',  # Nombre del archivo de salida
        'postprocessors': [{
            'key': 'FFmpegAudioConvertor',  # Usamos FFmpeg para convertir el audio
            'preferredcodec': 'mp3',        # Convertimos a MP3
            'preferredquality': '192',      # Calidad del MP3
        }],
        'postprocessor_args': [
            '-strict', '-2'  # Esto ayuda en algunos casos para evitar problemas con ffmpeg
        ],
    }

    try:
        # Intentamos descargar el audio
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("¡Descarga completada con éxito!")
    except Exception as e:
        print(f"Se produjo un error: {e}")

if __name__ == "__main__":
    url = input("Introduce la URL del video de YouTube: ")
    if url:  # Verifica si la URL no está vacía
        download_audio(url)
    else:
        print("Por favor, ingresa una URL válida.")
