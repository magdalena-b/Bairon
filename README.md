# Bairon



https://user-images.githubusercontent.com/20151778/152591669-8c237a27-7c8b-4ab8-8aa3-ee815a8eab21.mp4


https://user-images.githubusercontent.com/20151778/152591701-1ea7a63b-07c7-4bad-ab67-3ed8c3afc175.mp4


https://user-images.githubusercontent.com/20151778/152591718-a6e12c44-d74d-4030-ad04-d2d306f9b10f.mp4


https://user-images.githubusercontent.com/20151778/152591736-67b9532b-b484-4c6c-858c-e6e2ba22f31b.mp4


https://user-images.githubusercontent.com/20151778/152591745-f3878827-e615-4f71-be62-29cbc31477a1.mp4



Generator:

![Generator](img/generator.png)

Saved poems:

![Poems](img/poems.png)

Poetry Turing Test:

![Turing](img/turing.png)


## NLP

Dotrenowane modele:
- [x] William Shakespeare
- [x] Allen Ginsberg
- [x] e.e. cummings

Styl `Lorem Ipsum` dodałem tylko tymczasowo, do testowania, żeby nie trzeba było za każdym razem czekać na response po 20s.

## frontend

Frontend napisany w Vue.js

Style zrobione z pomocą Bulmy

Na razie działa to jako osobna aplikacja, docelowo zrobimy tak, że Django będzie serwowało spreparowaną aplikację

Podstrony:
- [x] Home - strona główna (`/`) 
- [x] Generate - strona do generowania i zapisywania wygenerowanych wierszy (`/generate`)
- [x] About - opis projektu, można zamiast prezentacji wykorzystać (`/about`)
- [x] Poems - lista wszystkich wygenerowanych wierszy, można filtrować(`/poems`)
- [x] Poem - wybrany wiersz, pokazuje statystyki i umożliwia głosowanie (`/poem/id`)
- [x] Turing Test - umożliwia głosowanie w TT (`/turing-test`)

## backend

### model bazy danych

![schemat](db_schema.png)

#### Input:
- style - styl tekstu w jaki ma być wygenerowany z dostępnej listy
- first_line - pierwsza linia tekstu na podstawie której ma być generowany tekst
- ```TODO``` nie wiem czy będą jeszcze inne dane wejściowe

#### Poem:
- author - autor tekstu - Różni się od style, bo tu może być prawdziwy autor albo maszyna, jeśli jest wygenerowany przez AI
- input - FK do `Input` (opcjonalne, np. kiedy tekst jest prawdziwy)
- text - wygenerowany tekst
- views - ilość wyświetleń  (opcjonalne, automatycznie 0)
- sentiment - zaklasyfikowany sentyment  (opcjonalne, np. jak nie uda się tego zaimplementować)

#### Rate:
- poem - FK do `Poem`
- rating - liczba naturalna

#### TuringTestVote:
- poem - FK do `Poem`
- fragment - fragment tekstu na podstawie którego została podjęta decyzja (opcjonalne, np. jak nie będzie to potrzebne nigdzie)
- vote - Human/Machine

## API

**Wszystkie endpointy wraz z poprawnymi parametrami powinny się znajdować pod adresem** `/swagger`

`/api/generate/`

po wysłaniu jsona z danymi potrzebnymi do stworzenia `Input` zwraca jsona z wygenerowanym `Poem`

`/api/save/`

po wysłaniu jsona z danymi potrzebnymi do stworzenia `Poem` zapisuje się w bazie

`/api/poem/id/`

zwraca jsona z danymi wiersza o konkretnym id

`/api/poems/`

zwraca podstawowe (pierwsza linia i tekst) dane o [10] najczęściej wyświetlanych wierszach

`/api/poems/[style=style][&][sentiment=sentiment]`

zwraca podstawowe (pierwsza linia i tekst) dane o [10] najczęściej wyświetlanych wierszach od konkretnego autore i/lub z konkretnym sentymentem

`/api/rating/id/`

zwraca jsona z ocenami (zarówno średnia i TT) o wierszu z konkretnym id

`/api/rating/`

zwraca jsona z ocenami (zarówno średnia i TT) o wszystkich wierszach

`/api/add/rate/id/`

endpoint do dodawania z oceny [1-10] dla wiersza z konkretnym id

`/api/add/turing-test-vote/id/` 

endpoint do dodawania opinii Human/Machine dla wiersza z konkretnym id

`/api/get/tt-fragment/` 

endpoint odpytywania serwera o dane potrzebne do TT

## Uruchomienie

### model

Jak na razie działa tylko z python3.7 i niższym, z powodu starej wersji tensorflow.

Do przełączenia się między wersjami polecam pyenv.

### frontend

##### wer. alfa

1. `cd frontend`
2. `sudo npm install vue`
3. `sudo npm install -g @vue/cli`
3. `npm install`
4. `npm run serve`
5. `npm install --save jspdf`

### Django

Aktywacja pyenv: `python3 -m venv .venv`

Pobieranie modułów do pythona: `pip install -r requirements.txt`

Migracje: `python manage.py makemigrations` i `python manage.py migrate`

Żeby dodać admina automatycznie `python manage.py create_admin`, nie trzeba wtedy wszystkiego wpisywać - tworzy się automatycznie - login: `admin`, password: `admin`

Żeby załadować wiersze prawdziwych poetów do bazy (potrzebne do TT) `python manage.py save_poems`

Uruchomienie `python manage.py runserver`

### Docker

Teraz nie trzeba uruchamiać wszystkigo osobno.

Wystarczy pobrać `docker` i `docker-compose` i wpisać w katalogu z projektem:
* `sudo docker-compose up` żeby uruchomić
* `sudo docker-compose down` żeby zatrzymać wszystko
* `sudo docker-compose build` żeby zbudować od nowa projekt (po każdej zmianie w django albo na froncie)

## Modele
Do głównego katalogu należy dodać folder checkpoint i w dodać foldery z plikami modelu (checkpoint, counter, encoder.json...):
- shakespeare2
- cummings2
- ginbsger2
- shakespeare_T5
