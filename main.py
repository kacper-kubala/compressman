import subprocess

# Definiujemy nazwy plików
input_file = "temp_input.mp4"
output_file = "temp_output.mp4"

# Budujemy komendę jako listę
command = [
    "ffmpeg", 
    "-i", input_file,       # Flaga wejścia i nazwa pliku
    "-vcodec", "libx264",       # Kodek wideo
    "-crf", "20",               # Poziom kompresji
    temp_output              # Plik wynikowy
]

print("Zaczynam kompresję... ⏳")

# Uruchamiamy proces
subprocess.run(command) 

print("Skończone! Sprawdź folder. 🎉")