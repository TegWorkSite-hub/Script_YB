from pytube import YouTube

def descargar_audio(url):
    try:
        # Crear un objeto YouTube
        yt = YouTube(url)
        
        # Seleccionar el stream de audio de más alta calidad
        stream = yt.streams.filter(only_audio=True).first()
        
        # Descargar el archivo de audio
        print(f"Descargando {yt.title}...")
        stream.download(filename=f"{yt.title}.mp4")  # Puedes cambiar el nombre del archivo si lo deseas
        print("¡Descarga completa!")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = input("Introduce la URL del video de YouTube: ")
    descargar_audio(url)
