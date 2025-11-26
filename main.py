import subprocess

# Definiujemy nazwy plików
plik_wejsciowy = "input.mp4"
plik_wyjsciowy = "skompresowany.mp4"

# Budujemy komendę jako listę
komenda = [
    "ffmpeg", 
    "-i", plik_wejsciowy,       # Flaga wejścia i nazwa pliku
    "-vcodec", "libx264",       # Kodek wideo
    "-crf", "20",               # Poziom kompresji
    plik_wyjsciowy              # Plik wynikowy
]

print("Zaczynam kompresję... ⏳")

# Uruchamiamy proces
subprocess.run(komenda) 

print("Skończone! Sprawdź folder. 🎉")