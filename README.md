# Przetwarzanie artykułu na kod HTML z użyciem OpenAI API

## Opis projektu

Aplikacja w Pythonie, która:

1. **Łączy się z API OpenAI** w celu przetworzenia tekstu.
2. **Odczytuje plik tekstowy z artykułem** i przygotowuje go do obróbki.
3. **Przekazuje treść artykułu wraz z promptem** do OpenAI, aby wygenerować kod HTML zgodny z określonymi wytycznymi.
4. **Zapisuje otrzymany od OpenAI kod HTML** w pliku `artykul.html`.

**Dodatkowo**, w ramach zadania dla chętnych:

- Stworzono szablon HTML `szablon.html` z estetycznymi stylami CSS do podglądu artykułu.
- Wygenerowano pełny podgląd artykułu w pliku `podglad.html`.

## Spis treści

- [Wymagania](#wymagania)
- [Instalacja](#instalacja)
- [Konfiguracja](#konfiguracja)
- [Użycie](#użycie)
- [Dodatkowe zadanie](#dodatkowe-zadanie)
  - [Szablon HTML](#szablon-html)
  - [Podgląd artykułu](#podgląd-artykułu)
- [Struktura projektu](#struktura-projektu)
- [Działanie API OpenAI i wyjaśnienie parametrów](#Działanie-API-OpenAI-i-wyjaśnienie-parametrów)

## Wymagania

- **Python 3.x**
- **Pakiety Python**:
  - `openai`
  - `python-dotenv`

## Instalacja

1. **Sklonuj repozytorium:**

   ```bash
   git clone https://github.com/JoanKr/Task-OpenAI.git
   ```

      ```bash
   cd Task-OpenAI
   ```

2. **Zainstaluj wymagane pakiety:**
```bash
pip3 install -r requirements.txt
```
## Konfiguracja

1. **Utwórz plik .env w głównym folderze projektu.**
2. **Dodaj do pliku .env swój klucz API OpenAI:**
```bash
 OPENAI_API_KEY=twój_klucz_api
```

## Użycie
1. **Umieść plik tekstowy z artykułem w folderze projektu.**
Plik powinien nazywać się `artykul.txt` lub dostosuj nazwę w skrypcie `main.py`.

2. **Uruchom skrypt:**
```bash
   python3 main.py
```
3. **Po uruchomieniu skryptu:**

Wygenerowany plik `artykul.html` pojawi się w folderze projektu.
Sprawdź wygenerowany plik:

Otwórz `artykul.html` w edytorze tekstu lub przeglądarce, aby zweryfikować zawartość.

## Dodatkowe zadanie
### Szablon HTML
Plik `szablon.html` zawiera szablon strony HTML z estetycznymi stylami CSS, gotowy do wklejenia wygenerowanego artykułu.

### Instrukcje:

1. Otwórz `szablon.html` w edytorze tekstu.
2. Wklej wygenerowany kod artykułu z artykul.html pomiędzy znacznikami `<div class="container"> a </div>`.
3. Zapisz plik jako `podglad.html`.

### Podgląd artykułu
Plik `podglad.html` to pełny podgląd artykułu z wklejonym kodem HTML, umożliwiający wizualizację treści z zastosowaniem estetycznych stylów CSS.

Instrukcje:

1. Otwórz `podglad.html` w przeglądarce internetowej.
2. Artykuł powinien być poprawnie sformatowany i gotowy do przeglądania.


## Struktura projektu
```
├── main.py
├── artykul.txt
├── artykul.html
├── szablon.html
├── podglad.html
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

- main.py - główny skrypt aplikacji.
- artykul.txt - plik z treścią artykułu do przetworzenia.
- artykul.html - wygenerowany kod HTML artykułu.
- szablon.html - szablon HTML z estetycznymi stylami CSS.
- podglad.html - pełny podgląd artykułu.
- requirements.txt - lista wymaganych pakietów Python.
- .env - plik z kluczem API OpenAI (nie dodawaj do repozytorium).
- .gitignore - plik określający, które pliki mają być ignorowane przez Git.
- README.md - ten plik z opisem projektu.

## Działanie API OpenAI i wyjaśnienie parametrów

W projekcie wykorzystywana jest metoda openai.ChatCompletion.create, która jest częścią API OpenAI. Jej zadaniem jest generowanie odpowiedzi na zadany prompt (czyli tekst wprowadzony przez użytkownika) na podstawie wytrenowanego modelu językowego, takiego jak gpt-3.5-turbo.

Oto krótkie wyjaśnienie najważniejszych parametrów, które zostały ustawione w projekcie:

- model: Określa wersję modelu, której chcemy użyć. W tym projekcie korzystamy z gpt-3.5-turbo, który oferuje odpowiedni balans pomiędzy jakością odpowiedzi a efektywnością kosztową.

- messages: Ten parametr przyjmuje listę wiadomości, które symulują dialog. Każda wiadomość jest obiektem zawierającym role (np. „system”, „user”, „assistant”) oraz content (tekst wiadomości). Dialog z ustawieniem roli systemu pomaga zdefiniować zachowanie modelu w kontekście projektu.

- temperature: Parametr kontrolujący stopień kreatywności odpowiedzi:

  - Niższe wartości (bliskie 0) sprawiają, że odpowiedzi są bardziej precyzyjne i deterministyczne, co jest zalecane, gdy ważna jest spójność i przewidywalność.
  - Wyższe wartości (bliższe 1) zwiększają kreatywność i różnorodność generowanych odpowiedzi. W projekcie ustawiliśmy wartość temperature na 0.5, aby uzyskać równowagę pomiędzy precyzją a naturalnością odpowiedzi.

- max_tokens: Określa maksymalną liczbę tokenów w wygenerowanej odpowiedzi. Tokeny to podstawowe jednostki tekstu, które składają się na słowa i inne znaki. Limity tokenów pomagają kontrolować długość odpowiedzi oraz koszty. W projekcie max_tokens ustawiono na wartość 750, co pozwala na tworzenie odpowiednio długich sekcji HTML, bez ryzyka przekroczenia limitu API.

### Dodatkowe materiały:

- [OpenAI API Documentation](https://beta.openai.com/docs/)
- [Python-dotenv Documentation](https://pypi.org/project/python-dotenv/)
