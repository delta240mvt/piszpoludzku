<p align="center">
  <img src="docs/assets/hero.svg" alt="Pisz po ludzku. Twój sens. Twój głos. Lepszy tekst." width="100%">
</p>

<h1 align="center">Pisz po ludzku</h1>

<p align="center">
  <strong>Zamień maszynowy tekst w naturalną polszczyznę.</strong><br>
  Skill dla Claude, Claude Code i Codexa. Zachowuje to, co chcesz powiedzieć.
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/licencja-MIT-232323?style=flat-square" alt="Licencja MIT"></a>
  <a href="#instalacja"><img src="https://img.shields.io/badge/Claude-gotowy-D97757?style=flat-square" alt="Dla Claude"></a>
  <a href="#instalacja"><img src="https://img.shields.io/badge/Codex-gotowy-337B65?style=flat-square" alt="Dla Codexa"></a>
  <a href="VERSION"><img src="https://img.shields.io/badge/wersja-1.0.0-232323?style=flat-square" alt="Wersja 1.0.0"></a>
</p>

<p align="center">
  <a href="#zobacz-różnicę">Przed i po</a> ·
  <a href="#instalacja">Instalacja</a> ·
  <a href="#pierwszy-tekst">Pierwszy tekst</a> ·
  <a href="#jak-to-działa">Zasady</a> ·
  <a href="#testy-i-rozwój">Testy</a>
</p>

---

Masz tekst, w którym wszystko jest „kluczowe”, każdy akapit zapowiada przełom, a po przeczytaniu trudno powiedzieć, o co chodziło? **Pisz po ludzku** pomaga go zredagować: usuwa pustosłowie, prostuje szyk i rozbija powtarzalne konstrukcje.

Pracuje według reguł zapisanych w tym repo. Pilnuje faktów, cytatów i głosu autora. Może poprawić post, e-mail, artykuł, stronę sprzedażową czy rozdział e-booka. Gdy tekst jest dobry, potrafi zostawić go bez zmian.

## Zobacz różnicę

Przykłady są syntetyczne i pokazują zamierzony sposób redakcji. Konkretna odpowiedź zależy od modelu i materiału.

<table>
  <thead><tr><th width="50%">Przed</th><th width="50%">Po</th></tr></thead>
  <tbody>
    <tr>
      <td>Warto podkreślić, że nasza aplikacja umożliwia użytkownikom dokonywanie zapisu notatek w jednym miejscu.</td>
      <td>W naszej aplikacji możesz zapisywać notatki w jednym miejscu.</td>
    </tr>
    <tr>
      <td>W celu dokonania zmiany hasła konieczne jest przejście do ustawień konta.</td>
      <td>Żeby zmienić hasło, przejdź do ustawień konta.</td>
    </tr>
    <tr>
      <td>Należy zaznaczyć, że ta zmiana może przyczynić się do poprawy czytelności tekstu, jednak nie gwarantuje poprawy wyników.</td>
      <td>Ta zmiana może poprawić czytelność tekstu, ale nie gwarantuje lepszych wyników.</td>
    </tr>
  </tbody>
</table>

W ostatnim przykładzie **„może” zostaje „może”**. Lepszy styl nie daje podstaw do mocniejszej obietnicy.

## Co dostajesz

| Możliwość | Co robi w praktyce |
| --- | --- |
| Naturalna polszczyzna | Upraszcza rozwlekłe zdania, kalki i zbędne nominalizacje. |
| Redakcja dopasowana do tekstu | Uwzględnia odbiorcę i gatunek. Formalny tekst może pozostać formalny. |
| Ochrona głosu autora | Korzysta z przekazanej próbki stylu bez dopisywania historii czy emocji. |
| Wierność znaczeniu | Zachowuje liczby, negacje, warunki i stopień pewności. |
| Praca z dokumentami | Chroni cytaty, linki, przypisy, kod i strukturę Markdown. |
| Cztery tryby | Od drobnych poprawek po przebudowę narracji lub samą diagnozę. |
| Audytor pomocniczy | Lokalny skrypt wskazuje wybrane powtarzalne wzorce i niezamknięte bloki kodu. |

## Instalacja

Wybierz miejsce, w którym używasz asystenta. Do samej redakcji nie musisz instalować Pythona ani dodawać klucza API. Potrzebujesz środowiska obsługującego skille.

### Claude w przeglądarce lub aplikacji

1. **[Pobierz gotową paczkę piszpoludzku.zip](https://github.com/delta240mvt/piszpoludzku/raw/refs/heads/main/dist/piszpoludzku.zip).**
2. W Claude otwórz **Customize → Skills**, kliknij **+ → Create skill → Upload a skill**.
3. Wgraj ZIP, włącz skill i rozpocznij nową rozmowę.

Paczka zawiera folder `piszpoludzku` z instrukcjami i materiałami. Wgrywasz ją w całości. Jeśli nie widzisz sekcji Skills, sprawdź dostępność wykonywania kodu oraz ustawienia organizacji. [Instrukcja Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

### Claude Code i Codex

Pobierz repozytorium:

```sh
git clone https://github.com/delta240mvt/piszpoludzku.git
cd piszpoludzku
```

**Windows / PowerShell**

```powershell
.\install.ps1 -Target Both
```

**macOS / Linux / Git Bash**

```sh
sh install.sh --target both
```

| Chcesz zainstalować tylko… | PowerShell | Shell |
| --- | --- | --- |
| Claude Code | `.\install.ps1 -Target Claude` | `sh install.sh --target claude` |
| Codexa | `.\install.ps1 -Target Codex` | `sh install.sh --target codex` |

Instalatory kopiują folder skilla do `~/.claude/skills/piszpoludzku` dla Claude Code i `~/.agents/skills/piszpoludzku` dla Codexa. Uruchom nową sesję i wybierz skill. [Miejsca instalacji w Codex](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills) · [Miejsca instalacji w Claude Code](https://code.claude.com/docs/en/skills#where-skills-live).

<details>
<summary><strong>Instalacja ręczna, aktualizacja i rozwiązywanie problemów</strong></summary>

Ręcznie skopiuj **cały** folder `skills/piszpoludzku` do jednej z powyższych lokalizacji. Sam `SKILL.md` nie zawiera wszystkich reguł.

Dla konkretnego projektu umieść folder w `.claude/skills/` lub `.agents/skills/` tego projektu. W sesji chmurowej folder musi być dostępny w środowisku zdalnym. Instalacja na komputerze nie jest automatycznie instalacją w chmurze.

Starsze instalacje Codexa mogą korzystać z `~/.codex/skills`. Instalator ich nie przenosi. Przy zmianie lokalizacji zachowaj własne poprawki i pozostaw jedną aktywną kopię skilla.

Aktualizacja z kopią poprzedniej wersji:

```powershell
git pull --ff-only
.\install.ps1 -Target Both -Force
```

```sh
git pull --ff-only
sh install.sh --target both --force
```

Bez `-Force` lub `--force` instalator odmawia nadpisania istniejącego folderu. Kopię znajdziesz obok niego jako `piszpoludzku.bak-*`. Przenieś ją poza katalog `skills`, jeśli asystent wyświetla ją jako dodatkowy skill.

Własny katalog bazowy wskaż przez `-DestinationRoot "ścieżka"` lub `--destination-root "ścieżka"`. Instalator utworzy w nim `.claude/skills` lub `.agents/skills`.

Jeśli PowerShell blokuje skrypt, skorzystaj z instalacji ręcznej. Aby odinstalować skill, usuń wyłącznie folder `piszpoludzku` z wybranego katalogu skilli. W Claude wyłącz go w ustawieniach Skills.

</details>

## Pierwszy tekst

**Codex**

```text
$piszpoludzku Zredaguj poniższy tekst w trybie standardowym.
Zachowaj sens, fakty i mój ton. Zwróć sam tekst.

[Wklej tekst]
```

**Claude Code**

```text
/piszpoludzku Popraw tekst poniżej w trybie minimalnym.
Zachowaj kolejność akapitów, cytaty i linki.

[Wklej tekst]
```

**Claude**

```text
Użyj skilla Pisz po ludzku. Przeredaguj ten tekst, żeby brzmiał
naturalnie po polsku. Nie dopisuj informacji. Zwróć sam tekst.

[Wklej tekst]
```

### Wybierz zakres zmian

| Tryb | Kiedy go wybrać | Zakres |
| --- | --- | --- |
| **Minimalny** · domyślny | Chcesz wygładzić gotowy tekst. | Słowa, szyk, interpunkcja, podział zdań; zachowana kolejność i układ akapitów. |
| **Standardowy** | Tekst potrzebuje lepszego rytmu. | Dodatkowo dzielenie i łączenie akapitów oraz poprawa nagłówków bez przenoszenia akapitów. |
| **Głęboki** | Wyraźnie chcesz przebudowy narracji. | Nowy układ argumentu, nadal bez nowych faktów i doświadczeń. |
| **Audyt** | Chcesz wiedzieć, co poprawić. | Diagnoza i propozycje bez zmiany tekstu. |

Możesz poprosić o `tekst`, `tekst+raport` lub `audyt`. Przy `tekst+raport` dostaniesz wersję po redakcji i od 3 do 7 najważniejszych typów zmian.

<details>
<summary><strong>Gotowe polecenia: post, e-book, głos autora</strong></summary>

**Post**

```text
Użyj piszpoludzku w trybie standardowym. To post dla osób prowadzących
małe firmy. Usuń pustosłowie i powtarzalne konstrukcje. Zachowaj
moje stanowisko i wezwanie do działania. Wynik: tekst.
```

**Rozdział e-booka**

```text
Użyj piszpoludzku w trybie minimalnym do redakcji rozdzial.md.
Zachowaj kolejność, definicje, cytaty i przypisy.
Zapisz wynik w nowym pliku rozdzial-po-redakcji.md.
```

**Twój głos**

```text
Użyj piszpoludzku. Przeczytaj moją próbkę stylu, a potem zredaguj tekst
w tym samym gatunku i tonie. Nie przenoś faktów ani historii z próbki
do redagowanego tekstu.

Próbka stylu: [wklej]
Tekst do redakcji: [wklej]
```

</details>

## Jak to działa

```text
Twój tekst → rozpoznanie problemów → redakcja → kontrola sensu → gotowy tekst
             gatunek i odbiorca     wybrany     fakty, cytaty,
             oraz głos autora       zakres     warunki i ton
```

Model czyta krótki plik `SKILL.md`, a potem sięga po reguły potrzebne do zadania. Pełna metodyka opisuje m.in. pustosłowie, kalki, rytm, powtarzalne kontrasty, źródła, Markdown i pracę z długimi dokumentami.

Najpierw liczy się polecenie użytkownika i znaczenie tekstu. Dopiero potem styl. Dlatego skill nie zamienia każdego formalnego zdania na potoczne, nie usuwa potrzebnych powtórzeń i nie dopisuje osobistych historii. W redagowanej prozie prowadzi myśl kropkami, przecinkami i dwukropkami; chroni myślniki w cytatach, nazwach, zakresach i zapisie technicznym.

**[Przeczytaj reguły skilla](skills/piszpoludzku/SKILL.md)** · [Pełna metodyka](skills/piszpoludzku/references/metodyka-pelna.md) · [Katalog przykładów](skills/piszpoludzku/references/katalog-przykladow.md)

## Audytor tekstu

Opcjonalny skrypt wymaga **Pythona 3.10+**. Korzysta wyłącznie z biblioteki standardowej, działa lokalnie i nie wysyła tekstu do sieci.

```sh
python skills/piszpoludzku/scripts/audyt_tekstu.py tekst.md
```

Raport JSON do osobnego pliku:

```sh
python skills/piszpoludzku/scripts/audyt_tekstu.py tekst.md --format json --output raport.json
```

Audytor wskazuje seryjne kontrasty, powtarzane zapowiedzi, nagromadzone wzmocnienia, powtarzające się nagłówki oraz niezamknięte bloki kodu. Trafienia są miejscami do przeczytania. Skrypt nie ocenia prawdziwości zdań, autorstwa ani pełnej poprawności Markdown. Nie przepisuje tekstu i odmawia zapisu raportu w pliku źródłowym.

<details>
<summary><strong>Kody zakończenia dla automatyzacji</strong></summary>

| Kod | Znaczenie |
| --- | --- |
| `0` | Audyt wykonany. Raport może zawierać uwagi. |
| `1` | Błąd odczytu lub zapisu, także próba nadpisania źródła raportem. |
| `2` | Niepoprawne argumenty. |
| `3` | Raport zawiera błąd i podano `--fail-on error`. |

</details>

## Co warto wiedzieć

Skill jest zestawem instrukcji dla modelu. Jakość wyniku zależy również od modelu, tekstu wejściowego i kontekstu. Przy publikacji sprawdź wersję po redakcji, zwłaszcza liczby, cytaty i warunki.

Nie służy do ustalania autorstwa ani nie obiecuje wyniku w detektorach AI. Nie zastępuje sprawdzania źródeł. Sam skill nie dodaje połączeń z zewnętrznymi usługami; tekst przekazany Claude lub Codexowi jest przetwarzany według zasad wybranego dostawcy i ustawień konta.

## Pliki w repo

```text
piszpoludzku/
├── skills/piszpoludzku/
│   ├── SKILL.md              Instrukcje i wybór trybu
│   ├── agents/openai.yaml   Nazwa i opis w Codexie
│   ├── references/          Metodyka, reguły i przykłady
│   └── scripts/             Opcjonalny audytor tekstu
├── dist/piszpoludzku.zip    Gotowa paczka do wgrania
├── scripts/package_skill.py
├── install.ps1             Instalacja w Windows
├── install.sh              Instalacja w macOS i Linux
├── docs/                   Metodologia i baner
├── tests/                  Testy i scenariusze redakcji
├── CONTRIBUTING.md
└── LICENSE
```

## Testy i rozwój

```sh
python -m unittest discover -s tests -v
python scripts/package_skill.py
```

Testy sprawdzają audytor, instalatory i zawartość paczki. Workflow GitHub Actions uruchamia je na Windows, Linux i macOS. Scenariusze oceny redakcji są opisane osobno, ponieważ test skryptu nie dowodzi jakości odpowiedzi modelu.

[Instrukcja testowania](tests/README.md) · [Zapis weryfikacji](tests/results/with-skill.md) · [Pochodzenie przykładów](tests/PROVENANCE.md) · [Jak rozwijać skill](CONTRIBUTING.md)

## Autor i licencja

**Przemysław Filipiak · [delta240mvt](https://github.com/delta240mvt)**

Kod i dokumentacja: [MIT](LICENSE). Syntetyczne materiały w `tests/fixtures/`: [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/), zgodnie z [opisem pochodzenia](tests/PROVENANCE.md).

Układ README inspirowany [InstaScaler](https://github.com/delta240mvt/InstaScaler): wyraźny tytuł, praktyczne porównania i szybkie przejście do użycia.

---

<p align="center"><strong>Twój sens. Twój głos. Lepszy tekst.</strong><br><sub>Pisz po ludzku · 2026</sub></p>
