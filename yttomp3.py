#pip3 install youtube_dl
import youtube_dl

#Pedimos la URL de input al usuario
input_url = input("Ingrese URL del video: ")

#Obtenemos el titulo del video
video_info = youtube_dl.YoutubeDL().extract_info(url=input_url, download=False)
video_title = video_info['title']

#Setear las opciones para la descarga del video
opciones = {
    'format': 'bestaudio/best',
    'outtmpl': f"D:\\Descargas 2.0\\{video_title}.mp3", #Seteamos la ubicacion deseada
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

#Descargamos el video
with youtube_dl.YoutubeDL(opciones) as ydl:
    ydl.download([input_url])

"""
pasos adicionales antes de iniciar programa
1) Ir a direccion: https://ffmpeg.org/download.html
2) Ir a sección "Windows builds from gyan.dev"
3) En la nueva ventana, ir a git y seleccionar primer link, se descarga archivo
4) Extraer y copiar archivos del rar en la dirección C: o D: en una nueva carpeta de nombre "FFMPEG"
5) Entrar a bin y copiar direccion (ejemplo C:\FFMPEG\bin)
6) En inicio, buscar variables de entorno
7) Abrir path y crear un nuevo path, copiar la direccion, y guardamos
"""
