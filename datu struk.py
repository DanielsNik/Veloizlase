import requests
from bs4 import BeautifulSoup
import pandas as pd


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}
url = "https://www.ss.com/lv/transport/bycycles/search-result/"

# Veic HTTP GET pieprasījumu uz doto URL
response = requests.get(url, headers=headers)

# Pārbauda, vai lapa veiksmīgi ielādēta
if response.status_code != 200:
    print("Kļūda pieprasot lapu:", response.status_code)
    exit()

# Nolasa lapas saturu ar BeautifulSoup HTML parseri
soup = BeautifulSoup(response.text, "html.parser")

# Atlasām tikai tās rindas tabulā, kurām ir ID
rows = soup.select("tr[id^='tr_']")
results = []
for row in rows:
    td_cells = row.find_all("td")  # Atrodam visas šūnas konkrētajā rindā
    if len(td_cells) >= 7:         # Pārliecināmies, ka rindā ir pietiekami daudz šūnu
        marka = td_cells[3].get_text(strip=True)
        stav = td_cells[5].get_text(strip=True)
        cena = td_cells[6].get_text(strip=True)
        apr = td_cells[2].get_text(strip=True)

        results.append({
            "Marka": marka,
            "Stāv.": stav,
            "Cena (€)": cena,
            "Apraksts": apr
        })

# Izveidojam pandas DataFrame
df = pd.DataFrame(results)
print(df)

df.to_excel("velosipedi.xlsx", index=False, engine='openpyxl')
print("Dati saglabāti Excel failā: velosipedi.xlsx")
