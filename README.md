# SS.com velosipēdu sludinājumu pārraudzības rīks


## Projekta uzdevums

Šī projekta mērķis ir izstrādāt programmu, kas automatizē velosipēdu sludinājumu pārbaudi portālā "ss.com".
Novēršot vajadzību lietotājam manuāli apmeklēt saitu un meklēt interesējošos piedāvājumus.

Programma automātiski iegūst sludinājumus no sadaļas “Velosipēdi”, strukturē iegūto informāciju, saglabā to Excel failā un.
Ja nepieciešams, var izfiltrēt sludinājumus pēc lietotāja kritērijiem (piemēram, marka, cena vai atslēgvārdi).

Šī programmatūra ir noderīga cilvēkiem, kuri regulāri meklē lietotus velosipēdus par izdevīgām cenām un vēlas automatizēt savu uzdevumu.


## Tehnoloģijas un izmantotās bibliotēkas

Projekts ir izstrādāts ar **Python**, izmantojot šādas bibliotēkas:

| Bibliotēka        | Funkcija/problēma, ko tā risina 
|-------------------|------------------------------------------------------
| `requests`        | HTTP pieprasījumu veikšanai un lapas satura iegūšanai 
| `beautifulsoup4`  | HTML koda parsēšanai un datu izvilkšanai 
| `pandas`          | Datu struktūras izveidei un eksportam uz Excel 
| `openpyxl`        | Excel failu (`.xlsx`) saglabāšanai ar `pandas` 
