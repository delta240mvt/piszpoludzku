# Metodologia

**Ostatnia aktualizacja:** 2026-07-30

Skill opiera się na praktyce redakcyjnej: diagnozuje nadmierną regularność, pustosłowie, kalki, zbyt gładkie przejścia i rozjazd między formą a gatunkiem. To heurystyki, nie dowód pochodzenia tekstu.

Najwyższą rangę mają: polecenie użytkownika, fakty w źródle, ochrona znaczenia i integralność dokumentu. Niższą rangę mają listy „sygnałów AI”, porady o stylometrii oraz sugestie dotyczące rytmu. Nie stosujemy mechanicznie porad o dodawaniu błędów, slangu, metryk, historii, perplexity ani burstiness.

Rozwój odbywa się w cyklu RED–GREEN–REFACTOR. Publiczne fixtures są syntetyczne; nie zawierają e-booka, prywatnych danych ani cytatów z analiz źródłowych. `tests/example-coverage.md` pokazuje, że katalog obejmuje wszystkie klasy przykładów użyte przy projektowaniu, bez ich kopiowania.

Najważniejszy test brzmi: czy tekst po redakcji zachowuje to, co autor rzeczywiście powiedział, a jednocześnie czyta się łatwiej i bardziej naturalnie? Jeśli nie można odpowiedzieć twierdząco na oba pytania, zmiana nie powinna wejść do publikacji.
