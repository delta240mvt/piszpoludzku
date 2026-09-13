# Wynik po implementacji

**Ostatnia aktualizacja:** 2026-09-13

## Zweryfikowane lokalnie

- `python -m unittest discover -s tests -v`: 13 testów PASS, bez pominięć; Windows, Python 3.10, PowerShell i Git Bash.
- Walidator formatu skilla: PASS.
- Audytor tworzy raport JSON, zachowuje plik wejściowy, obsługuje UTF-8/BOM/CRLF i zgłasza błąd niezamkniętego fenced code.
- Instalator PowerShell działa dla Claude Code i Codexa, obsługuje ścieżki ze spacją i polskimi znakami, odmawia nadpisania oraz tworzy backup po `-Force`.
- Instalator shell poprawnie kończy instalację wyłącznie dla Claude. Instalatory używają `.agents/skills` dla Codexa.
- Audytor odmawia nadpisania źródła raportem, również gdy wskazano dowiązanie twarde do źródła.
- Paczka ZIP zawiera wszystkie pliki skilla, licencję i wersję. Pomija cache Pythona.

## Ręczne próby w Codex

Osobny agent Codex zastosował reguły w czterech próbach. Były to pojedyncze odpowiedzi z oceną opisową, bez porównania statystycznego i bez prób w Claude.

| Przypadek | Zaobserwowany wynik |
| --- | --- |
| `minimalne-pary.md` | Bez zmian; zachowane modalność, negacje, warunki i rozróżnienie korelacji od przyczynowości. |
| `chroniony-markdown.md` | Bez zmian; zachowane cytat, URL, kod, tabela i przypis. W przeglądzie poprawiono położenie komentarza fixture, aby frontmatter rozpoczynał plik. |
| `naturalny-formalny.md` | Bez zmian; zachowane lista kroków, triada i zastrzeżenie. |
| `ai-szablonowy.md` | Usunięte puste zapowiedzi i wzmocnienia; trzy rozróżnienia zachowane w pierwotnej kolejności. |

Fragment rzeczywistego wyniku ostatniej próby:

> W pisaniu liczy się jakość, nie częstotliwość. W materiałach liczy się ich wartość, nie liczba. Chodzi o trwały wpływ, nie widoczność.

Powtórzone nagłówki „Zrób teraz” i polecenia „Wybierz temat” pozostały w wyniku. Agent uznał, że ich usunięcie przekroczyłoby zakres trybu minimalnego. To ilustracja decyzji redakcyjnej, nie dowód ogólnej skuteczności.

Przegląd wykrył też przykłady dopisujące skutki nieobecne w wejściu oraz odwróconą logikę pytania o funkcję wzorca. Poprawiono je przed spakowaniem wydania.

## Zakres weryfikacji

Nie wykonano prób w Claude ani importu do konta Claude. Historyczna próba z 2026-07-30 została zablokowana przez wygasły token OAuth lokalnego CLI. Obecne sprawdzenie potwierdza format paczki i działanie instalatorów, nie zachowanie każdego obsługiwanego modelu. Scenariusze kolejnych prób opisuje `tests/evaluations.json`.

Nie deklarujemy wyniku „przejdzie detektor” ani autorstwa tekstu. Testowana jest wierność, integralność i zachowanie ochronne.
