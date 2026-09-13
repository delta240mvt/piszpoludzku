# Rozwijanie Pisz po ludzku

Najbardziej pomaga konkret: tekst przed redakcją, oczekiwany wynik i wyjaśnienie, co obecna reguła zepsuła. Do zgłoszeń dodawaj własne lub syntetyczne przykłady bez danych prywatnych.

## Zmiana reguł

1. Znajdź właściwy plik w `skills/piszpoludzku/references/`. `SKILL.md` powinien pozostać krótkim punktem wejścia.
2. Pokaż przypadek, w którym obecna instrukcja zawodzi, oraz kontrprzykład, którego nie należy zmieniać.
3. Zapisz regułę i parę przed/po. Porównaj fakty, negacje, warunki i stopień pewności. Nie dopisuj konkretów nieobecnych w wejściu.
4. Sprawdź wynik w modelu i opisz środowisko oraz ograniczenia. Oddziel rzeczywistą odpowiedź od oczekiwanego wyniku.

Nie dodawaj list zakazanych słów ani obietnic dotyczących detektorów AI. Reguła powinna pomagać podjąć decyzję redakcyjną w kontekście.

## Zmiana kodu lub instalatora

Dla poprawki błędu dodaj test pokazujący problem. Testuj instalację w katalogu tymczasowym, żeby nie nadpisywać własnych skilli.

```sh
python -m unittest discover -s tests -v
python scripts/package_skill.py
git diff --check
```

Po zmianie zawartości skilla dołącz aktualny `dist/piszpoludzku.zip`. Skrypt pakujący pomija cache Pythona, dodaje licencję i numer wersji oraz ustala jednakowy zapis końców linii. Baner i dokumentacja repo nie trafiają do paczki.

Jeśli zmieniasz wydanie, zaktualizuj `VERSION` i oznaczenie wersji w README. Zmiany kodu i dokumentacji podlegają MIT; przykłady w `tests/fixtures/` są udostępniane jako CC0 1.0.
