import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = []

for quote in soup.find_all("div", class_="quote"):
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text

    quotes.append({
        "Frase": text,
        "Autor": author
    })

df = pd.DataFrame(quotes)

df.to_csv("citacoes.csv", index=False, encoding="utf-8-sig")

print("Arquivo criado com sucesso!")
