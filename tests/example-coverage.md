# Pokrycie przykładów

**Ostatnia aktualizacja:** 2026-07-30
**Zasada:** wszystkie pozycje są syntetyczne; katalog opisuje klasy przykładów, nie udostępnia źródłowych treści.

| Kategoria źródłowa | Identyfikator syntetyczny | Miejsce użycia | Test ochronny |
|---|---|---|---|
| E-book: ogólnik bez sytuacji | `ebook-kontekst-zamiast-hasla` | katalog przykładów | brak konfabulacji |
| E-book: seryjna produkcja treści | `ebook-seria-przed-weryfikacja` | katalog przykładów | selektywna redakcja |
| E-book: jeden materiał jako aktywo | `ebook-material-jako-aktywum` | formaty | zachowanie tezy |
| E-book: biblioteka rozwiązań | `ebook-biblioteka-problemow` | katalog przykładów | struktura |
| E-book: problem techniczny | `ebook-problem-techniczny` | katalog przykładów | konkret bez danych |
| E-book: problem emocjonalny | `ebook-problem-emocjonalny` | katalog przykładów | brak fałszywej historii |
| E-book: platforma a odbiorca | `ebook-platforma-do-osoby` | formaty | brak stereotypizacji |
| E-book: doświadczenie jako zasób | `ebook-doswiadczenie-jako-zasob` | katalog przykładów | głos autora |
| E-book: forma surowa | `ebook-biegun-surowy` | formaty | gatunek |
| E-book: forma filmowa | `ebook-biegun-filmowy` | formaty | gatunek |
| E-book: przypadkowy środek | `ebook-przypadkowy-srodek` | problemy redakcyjne | brak nadinterpretacji |
| E-book: percepcja twórcy | `ebook-obraz-tworcy` | katalog przykładów | brak obietnic statusu |
| E-book: percepcja materiału | `ebook-obraz-materialu` | elementy dokumentu | kontrola CTA |
| E-book: dowód społeczny | `ebook-dowod-spoleczny` | katalog przykładów | brak zmyślonych wyników |
| E-book: blok głębokiej pracy | `ebook-ochrona-uwagi` | formaty | zachowanie warunku |
| E-book: przecięcie kompetencji | `ebook-nietypowe-polaczenie` | katalog przykładów | brak biografii |
| E-book: fraktal tematu | `ebook-fraktal-niszy` | katalog przykładów | zachowanie metafory, gdy działa |
| E-book: autor–przekaz–rynek | `ebook-trzy-czestotliwosci` | katalog przykładów | nie spłaszczać modelu |
| E-book: karta jednej osoby | `ebook-jeden-odbiorca` | formaty | celowe pytania |
| E-book: tutorial krok po kroku | `ebook-pokaz-potem-nazwij` | formaty | celowe imperatywy |
| E-book: dwa tytuły | `ebook-tytul-i-obnizenie-progu` | elementy dokumentu | mikrocopy |
| E-book: komunikacja bez oceny | `ebook-opcja-zamiast-wyroku` | katalog przykładów | modalność |
| E-book: granica komentarzy | `ebook-granica-relacji` | katalog przykładów | zachowanie stanowczości |
| E-book: dolina i mastery | `ebook-wzrost-nieliniowy` | katalog przykładów | brak coachingu |
| E-book: analiza sygnału | `ebook-akordeon-iteracji` | katalog przykładów | przyczynowość |
| E-book: AI przetwarza materiał | `ebook-ai-nie-zastepuje-doswiadczenia` | katalog przykładów | autorstwo |
| Raport GPT: seryjne końcówki | `gpt-koniec-rozdzialu-seria` | fixture + audytor | seria, nie pojedynczy przypadek |
| Raport GPT: kontrast binarny | `gpt-nie-x-lecz-y` | fixture + audytor | false positive dla pojedynczego |
| Raport GPT: abstrakt | `gpt-abstrakt-bez-stawki` | katalog przykładów | brak dopisanych danych |
| Raport GPT: imperatyw | `gpt-imperatyw-seryjny` | fixture | instrukcja celowa zostaje |
| Raport GPT: metakomentarz | `gpt-meta-zapowiedz` | fixture + audytor | lokalna poprawka |
| Raport GPT: anglicyzm | `gpt-framework-po-polsku` | naturalna polszczyzna | nazwa własna zostaje |
| Raport humanizacji: pustosłowie | `humanizacja-puste-wzmocnienie` | audytor | neutralna nazwa reguły |
| Raport humanizacji: kalka | `humanizacja-kalka-oferty` | naturalna polszczyzna | lokalizacja |
| Raport humanizacji: lokalny kontekst | `humanizacja-nielokalne-swieto` | katalog przykładów | brak fałszywego lokalizowania |
| Raport humanizacji: symetria | `humanizacja-trojka-rytmiczna` | fixture | celowa anafora zostaje |
| Raport humanizacji: emoji | `humanizacja-nadmiar-emoji` | formaty | gatunek social media |
| Raport humanizacji: repetycja | `humanizacja-fałszywy-cios` | problemy redakcyjne | funkcja powtórzenia |
| Raport humanizacji: halucynacja liczby | `humanizacja-niepotwierdzony-procent` | fixture | brak konfabulacji |
| Raport humanizacji: fałszywe źródło | `humanizacja-zrodlo-bez-pokrycia` | elementy dokumentu | cytowania |
| Raport humanizacji: rytm | `humanizacja-rowne-akapity` | przyklady przed/po | nie dodawać błędów |
| Signs: przesadne znaczenie | `signs-nadmuchana-waznosc` | audytor | nie stwierdzać AI |
| Signs: ton promocyjny | `signs-puffery` | audytor | gatunek reklamy |
| Signs: pseudoatrybucja | `signs-nieokreslone-zrodla` | elementy dokumentu | źródło chronione |
| Signs: szeroki trend | `signs-szeroki-trend-bez-danych` | katalog przykładów | brak dopisania związku |
| Signs: słownictwo nadęte | `signs-nadete-slownictwo` | audytor | pojedynczy wyraz nie alarmuje |
| Signs: komunikacja użytkowa | `signs-canned-odpowiedz` | formaty | zachowanie uprzejmości |
| Signs: markup | `signs-uszkodzony-markdown` | chroniony-markdown fixture | parser Markdown |
| Signs: cytowania | `signs-przypis-bez-zakresu` | chroniony-markdown fixture | zakres przypisu |
| Signs: komentarze | `signs-komentarz-szablonowy` | katalog przykładów | rejestr |
| Signs: podsumowanie edycji | `signs-edit-summary` | katalog przykładów | konkretny raport |
| Signs: medialna notability | `signs-notability-bez-dowodu` | katalog przykładów | źródło albo usunięcie |
| Signs: wyzwania i przyszłość | `signs-wyzwania-przyszlosc` | katalog przykładów | proporcja |
| Signs: przymiotnikowa mgła | `signs-przymiotnikowa-mgla` | katalog przykładów | seria, nie pojedynczy wyraz |
| Signs: nienaturalny synonim | `signs-sztywny-synonim` | naturalna polszczyzna | prosty czasownik |
| Signs: automatyczne przywitanie | `signs-automatyczne-przywitanie` | katalog przykładów | uprzejmość bez automatyzmu |
| Signs: deklaracja wiedzy | `signs-deklaracja-wiedzy` | katalog przykładów | nie udawaj pewności |
| Signs: źródło nieużyte | `signs-zrodlo-nieuzyte` | elementy dokumentu | integralność przypisów |
| Signs: niedziałający link | `signs-link-bez-pokrycia` | elementy dokumentu | nie twórz replacementu |
| Signs: historyczny disclaimer | `signs-historyczny-disclaimer` | katalog przykładów | heurystyka niskiej pewności |
| Signs: nieskuteczny wskaźnik | `signs-formalnosc-to-nie-dowod` | problemy redakcyjne | false positive |
| Kontrprzykład: formalność | `kontrformalny-raport` | naturalny-formalny fixture | brak nadredakcji |
| Kontrprzykład: instrukcja | `kontrinstrukcja-krokowa` | naturalny-formalny fixture | imperatywy zostają |
| Kontrprzykład: cytat | `kontrcytat-z-klisza` | chroniony-markdown fixture | cytat zostaje |
| Kontrprzykład: język mieszany | `kontr-pl-en` | tekst-mieszany fixture | bez tłumaczenia |
