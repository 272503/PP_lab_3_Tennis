# PP_lab_3_Tennis

# Tennis Scoring System – Refaktoryzacja i Testowanie

## Opis projektu

Projekt przedstawia **trzy różne implementacje klasy punktacji meczu tenisa**:

- `TennisGame1`
- `TennisGame2`
- `TennisGame3`

Każda wersja została **zrefaktoryzowana** w celu poprawy czytelności, eliminacji powtórzeń i zwiększenia elastyczności. Projekt zawiera również zestaw testów sprawdzających poprawność każdej wersji.

---

## Struktura projektu

| Plik                  | Opis                                             |
|-----------------------|--------------------------------------------------|
| `tennis1.py`          | Refaktoryzowana wersja TennisGame1              |
| `tennis2.py`          | Refaktoryzowana wersja TennisGame2              |
| `tennis3.py`          | Refaktoryzowana wersja TennisGame3              |
| `tennis_unittest.py`  | Testy jednostkowe z użyciem `unittest`          |
| `test_tennis.py`      | Testy parametryzowane z użyciem `pytest`        |
| `README.md`           | Dokumentacja projektu                           |



---

## Założenia logiki punktacji

System punktacji opiera się na klasycznych zasadach tenisa:

- Punkty: `Love`, `Fifteen`, `Thirty`, `Forty`
- Remis (np. `Fifteen-All`, `Thirty-All`)
- `Deuce` przy remisie 3:3 lub większym
- `Advantage` dla gracza, który zdobył punkt przy wyniku `Deuce`
- `Win for player` przy przewadze dwóch punktów powyżej 3

---

## Refaktoryzacja – co zostało poprawione?

- Zmniejszono liczbę powtórzeń kodu
- Zastosowano słowniki do tłumaczenia punktów (`0`, `1`, `2`, `3`) na nazwy
- Wydzielono metody pomocnicze (`_equal_score`, `_advantage_or_win`, `_get_regular_score`)
- Zmieniono nazwy zmiennych dla większej przejrzystości
- Umożliwiono użycie **dowolnych nazw graczy** (nie tylko "player1" i "player2")

---

## Jak uruchomić testy?

### Wymagania

- Python `3.8+`
- `pytest` (dla testów parametryzowanych)

### Instalacja zależności

```bash
pip install pytest
```

### Uruchomienie testów

**1. Testy** `unittest`
```bash
python tennis_unittest.py
```
**2. Testy** `pytest`
```bash
pytest test_tennis.py
```





