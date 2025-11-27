import subprocess, send_file
from flask import Flask, request

# Tworzymy instancję aplikacji (nasz serwer)
app = Flask(__name__)

# To jest nasza recepcja. 
# Znak '/' oznacza stronę główną (np. google.com/)
@app.route('/', methods = ['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        file = request.files['video_file']
        file.save('temp_input.mp4')
        compress('temp_input.mp4', 'temp_output.mp4')
        return "Hey! It's your video compressor. 🎥"
    
    else:
        return 'Showing form'

def compress(input_path, output_path):
    command = [
        "ffmpeg", 
        "-i", input_path,       # Flaga wejścia i nazwa pliku
        "-vcodec", "libx264",       # Kodek wideo
        "-crf", "20",               # Poziom kompresji
        output_path              # Plik wynikowy
        ]
    subprocess.run(command) 

# To uruchamia serwer, jeśli plik jest włączony bezpośrednio
if __name__ == '__main__':
    app.run(debug=True)