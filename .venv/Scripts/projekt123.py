# Podział danych na podstawie wartości podziału
def podziel_dane(index, value, dane):
    lewa = [r for r in dane if r[index] < value]
    prawa = [r for r in dane if r[index] >= value]
    return lewa, prawa

# Obliczanie indeksu Gini
def gini(grupy, klasy):
    n = sum(len(grupa) for grupa in grupy)
    wynik = 0.0
    for grupa in grupy:
        if len(grupa) == 0:
            continue
        score = 0.0
        for klasa in klasy:
            proporcja = [r[-1] for r in grupa].count(klasa) / len(grupa)
            score += proporcja ** 2
        wynik += (1 - score) * (len(grupa) / n)
    return wynik

# Znalezienie najlepszego podziału
def znajdz_podzial(dane):
    if not dane:
        return {'index': None, 'value': None, 'gini': float('inf'), 'grupy': ([], [])}
    klasy = list(set(row[-1] for row in dane))
    najlepszy_podzial = {'index': None, 'value': None, 'gini': float('inf'), 'grupy': None}
    for index in range(len(dane[0]) - 1):  # iterowanie po cechach
        for row in dane:
            grupy = podziel_dane(index, row[index], dane)
            g = gini(grupy, klasy)
            if g < najlepszy_podzial['gini']:
                najlepszy_podzial = {'index': index, 'value': row[index], 'gini': g, 'grupy': grupy}
    return najlepszy_podzial


# Funkcja tworząca liść
def to_terminal(grupa):
    klasy = [row[-1] for row in grupa]
    return max(set(klasy), key=klasy.count)

# Budowanie drzewa
def buduj_drzewo(dane, max_glebokosc, min_wielkosc, glebokosc=1):
    if not dane:
        return None
    podzial = znajdz_podzial(dane)
    lewa, prawa = podzial['grupy']
    if not lewa or not prawa or glebokosc >= max_glebokosc:
        return to_terminal(lewa + prawa)
    if len(lewa) <= min_wielkosc:
        lewa = to_terminal(lewa)
    else:
        lewa = buduj_drzewo(lewa, max_glebokosc, min_wielkosc, glebokosc + 1)
    if len(prawa) <= min_wielkosc:
        prawa = to_terminal(prawa)
    else:
        prawa = buduj_drzewo(prawa, max_glebokosc, min_wielkosc, glebokosc + 1)
    return {'index': podzial['index'], 'value': podzial['value'], 'lewa': lewa, 'prawa': prawa}


# Przewidywanie wyniku
def przewiduj(drzewo, dane):
    if isinstance(drzewo, dict):
        if dane[drzewo['index']] < drzewo['value']:
            return przewiduj(drzewo['lewa'], dane)
        else:
            return przewiduj(drzewo['prawa'], dane)
    return drzewo

# Dane treningowe
dataset = [
    [200, 1, 14, 1, 0],
    [1500, 2, 19, 1, 1],
    [50, 1, 10, 1, 0],
    [10, 3, 3, 0, 0],
    [1400, 1, 23, 1, 0],
    [1000, 2, 20, 0, 1],
    [500, 1, 15, 1, 0],
    [2500, 3, 22, 1, 1]
]

# Budowanie drzewa
drzewo = buduj_drzewo(dataset, max_glebokosc=4, min_wielkosc=1)

# Przykład użycia
def ocena_transakcji():
    kwota = float(input("Kwota transakcji: "))
    lokalizacja = int(input("Lokalizacja (1-3): "))         # 1 - transakcja lokalna, 2 - inny region, 3 - zagraniczna
    godzina = int(input("Godzina transakcji (0-24): "))
    metoda = int(input("Metoda płatności (0-1): "))         #0 - platnosc karta kredytowa, 1 - przelew
    wynik = przewiduj(drzewo, [kwota, lokalizacja, godzina, metoda])
    print("Podejrzana transakcja." if wynik == 1 else "Autoryzowana transakcja.")

ocena_transakcji()

