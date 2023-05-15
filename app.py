from flask import Flask, render_template, request
import random
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
import os

app = Flask(__name__)

# Przykładowa lista zawodników
zawodnicy = [
    {'imie': 'Jan', 'nazwisko': 'Kowalski', 'pozycja': 'Napastnik'},
    {'imie': 'Adam', 'nazwisko': 'Nowak', 'pozycja': 'Pomocnik'},
    {'imie': 'Piotr', 'nazwisko': 'Nowicki', 'pozycja': 'Bramkarz'},
    # Dodaj więcej zawodników według potrzeb
]

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        imie_zawodnika = request.form['tekst']
        zawodnik = znajdz_zawodnika(imie_zawodnika)
        wykres = generuj_wykres(imie_zawodnika)
         # Ustawienie nazwy obrazu w zależności od imienia zawodnika
        if imie_zawodnika == 'Adam':
            obraz = './static/assets/player2.png'
        elif imie_zawodnika == 'Jan':
            obraz = './static/assets/player1.png'
        elif imie_zawodnika == 'Piotr':
            obraz='./static/assets/player3.png'
        else:
            obraz = 'default.png'
        return render_template('wyniki.html', zawodnik=zawodnik, wykres=wykres, obraz=obraz)
    return render_template('index.html')

def znajdz_zawodnika(imie_zawodnika):
    for zawodnik in zawodnicy:
        if imie_zawodnika.lower() == f"{zawodnik['imie'].lower()}":
            return zawodnik
    return None

def generuj_wykres(imie_zawodnika):
    # Generowanie losowych danych na temat wydajności
    dni = range(1, 8)
    wydajnosc = [random.randint(50, 100) for _ in dni]

    # Tworzenie wykresu
    plt.plot(dni, wydajnosc)
    plt.xlabel('Dzień')
    plt.ylabel('Wydajność')
    plt.title(f'Wydajność zawodnika: {imie_zawodnika}')

    # Zapisywanie wykresu do bufora pamięci
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    # Konwertowanie wygenerowanego wykresu na dane w formacie base64
    wykres_data = base64.b64encode(buf.read()).decode('utf-8')

    plt.close()

    return wykres_data

if __name__ == '__main__':
    app.run(debug=True)
