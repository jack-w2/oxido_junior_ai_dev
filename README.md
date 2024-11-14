# oxido_junior_ai_dev
Zadanie rekrutacyjne w ramach rekrutacji na stanowisko Junior AI Developer w Oxido

Aplikacja generuje kod artykułu w HTML na podstawie tekstu dostępnego w pliku `artykul.txt`. Wykorzystuje do tego celu API OpenAI. Jako wynik działania otrzymujemy plik `artykul.html` zawierający kod, który należy umieścić w tagu `<body>` na przygotowanej stronie internetowej.

Wynikowy artykuł jest wstępnie sformatowany (ustrukturyzowany) oraz zawiera sugestie miejsc, w których warto osadzić grafiki.

## Użycie

Aby uruchomić aplikację należy uruchomić plik `ai_article_body_formatter.py`.

Wymagane zależności są opisane w pliku `requirements.txt`.

Oprócz tego wymagane są następujące zmienne środowiskowe `API_KEY`, `ORGANIZATION`, `PROJECT` zawierające odpowiednio klucz API oraz identyfiaktory organizacji i projektu.