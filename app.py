from flask import Flask, render_template, request

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
        szukany_tekst = request.form['tekst']
        zawodnik = znajdz_zawodnika(szukany_tekst)
        return render_template('wyniki.html', zawodnik=zawodnik)
    return render_template('index.html')

def znajdz_zawodnika(szukany_tekst):
    for zawodnik in zawodnicy:
        if szukany_tekst.lower() == f"{zawodnik['imie'].lower()} {zawodnik['nazwisko'].lower()}":
            return zawodnik
    return None

if __name__ == '__main__':
    app.run(debug=True)
