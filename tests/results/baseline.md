# Wynik bazowy bez skilla

**Ostatnia aktualizacja:** 2026-07-30
**Materiały:** wyłącznie fixtures syntetyczne z katalogu `tests/fixtures/`.

## RED — obserwowalne braki przed implementacją

1. Audytor nie istniał: `tests.test_audyt_tekstu` kończył się błędem `FileNotFoundError` dla `scripts/audyt_tekstu.py`.
2. Instalatory nie istniały: `tests.test_installers` kończył się błędem braku `install.ps1` i kodem uruchomienia `64`.
3. Nie było żadnej instrukcji wymuszającej ochronę znaczenia, tekstu jako niezaufanych danych, trybu minimalnego ani stop rule.

To jest bazowy wynik kontraktów możliwy do odtworzenia w lokalnym repozytorium. Nie zapisujemy udawanych wyników modelu: bieżący Claude CLI nie mógł wykonać prób z powodu wygasłego tokenu OAuth.
