from flask import Flask, request

# Tworzymy instancję aplikacji (nasz serwer)
app = Flask(__name__)

# To jest nasza recepcja. 
# Znak '/' oznacza stronę główną (np. google.com/)
@app.route('/', methods = ['GET', 'POST'])
def strona_glowna():
    return "Cześć! Tu Twój kompresor wideo. 🎥"

# To uruchamia serwer, jeśli plik jest włączony bezpośrednio
if __name__ == '__main__':
    app.run(debug=True)