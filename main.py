import os
import openai
from dotenv import load_dotenv

# Załaduj zmienne środowiskowe z pliku .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Wczytaj treść artykułu z pliku
with open("Zadanie dla JJunior AI Developera - tresc artykulu.txt", "r", encoding="utf-8") as file:
    article_text = file.read()

# Przygotuj zaktualizowany prompt
prompt = f"""
Przekształć poniższy artykuł na kod HTML zgodny z następującymi wytycznymi:

- Użyj odpowiednich tagów HTML do strukturyzacji treści (np. <h1>, <h2>, <p>, <ul>, <li>).
- Określ **maksymalnie 3 miejsca** w całym artykule, gdzie warto wstawić grafiki, oznaczając je za pomocą tagu <img src="image_placeholder.jpg" alt="dokładny prompt do wygenerowania grafiki">.
- **Każda grafika powinna być ściśle związana z treścią** i ilustrować konkretne zagadnienia poruszane w artykule.
- **Opisy grafik (atrybut alt)** muszą być szczegółowe i precyzyjne, unikaj ogólnych sformułowań.
- Umieść podpisy pod grafikami, używając odpowiedniego tagu HTML (np. <figcaption> w ramach <figure>).
- Nie dodawaj żadnego kodu CSS ani JavaScript.
- Zwróć jedynie kod, który można wstawić pomiędzy <body> i </body>. Nie dołączaj znaczników <html>, <head> ani <body>.

Oto artykuł do przetworzenia:

{article_text}
"""

# Wysyłanie zapytania do OpenAI
try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
    )

    # Pobranie wygenerowanego kodu HTML
    generated_html = response.choices[0].message['content'].strip()

    # Zapisanie wygenerowanego kodu HTML do pliku
    with open("artykul.html", "w", encoding="utf-8") as file:
        file.write(generated_html)

    print("HTML został zapisany w pliku artykul.html.")

except openai.error.OpenAIError as e:
    print("Wystąpił błąd:", e)
