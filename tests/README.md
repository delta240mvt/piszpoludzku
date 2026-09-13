# Testy

Uruchom pełny zestaw:

```text
python -m unittest discover -s tests -v
```

`evaluations.json` opisuje scenariusze zachowania skilla. `example-coverage.md` mapuje syntetyczne przykłady na klasy przypadków zaczerpnięte z prac redakcyjnych. Nie jest to korpus do wykrywania autorstwa AI.

Testy uruchamiają instalatory w katalogach tymczasowych. PowerShell i Bash są sprawdzane, jeśli są dostępne; brak interpretera oznacza pominięcie odpowiednich testów. Na Windows obsługiwany jest również Git Bash.

Test paczki porównuje zawartość ZIP-a z plikami skilla i sprawdza obecność licencji oraz brak cache. Po zmianach zbuduj paczkę ponownie:

```sh
python scripts/package_skill.py
```

## Próby z modelem

W nowej sesji wczytaj skill i użyj tekstu wskazanego przez `fixture` w `evaluations.json`. Zachowaj żądany `mode`. Porównaj wynik z `hard_invariants`, a następnie oceń czytelność według `quality`.

Zapisz model lub środowisko, datę, wejście, rzeczywistą odpowiedź i ocenę. Nie zastępuj wyniku modelu oczekiwanym tekstem. Dla porównania przeprowadź ten sam scenariusz w osobnej sesji bez skilla. Jedna dobra odpowiedź nie jest pomiarem skuteczności.

Aktualne sprawdzenia i ich ograniczenia opisuje [zapis weryfikacji](results/with-skill.md).
