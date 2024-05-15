---
jupytext:
  text_representation:
    extension: .ipynb
    format_name: jupytext
    format_version: '1.6'
    jupytext_version: 1.14.0
    split_at_heading: true
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Håndtering av filstier

Når man jobber med data, er det viktig å holde oversikt over hvor hvilke inndatafiler er lagret, og hvor hvilke utdatafiler skal skrives. Dette er spesielt viktig når man flytter mellom datamaskiner eller mellom virtuelle maskiner, som for eksempel CSC Notebooks-plattformen. Bruk av et distribuert kodeoppbevaring eller versjoneringssystem, som GitHub, legger til et ekstra lag med kompleksitet: filstier bør ofte være *relative* til git-repoet, eller til den gjeldende filen, siden repositoriet kan klones til hvilken som helst plassering på en annen datamaskin (og allerede et annet brukernavn på skole- og personlige datamaskiner kan ødelegge ting).

Tidligere har filstier ofte vært hardkodede strenger, tekstverdier. Hvis for eksempel et utdatafilnavn måtte avledes fra et inndatafilnavn, ble alle slag av slicing og andre strengmanipulasjonsmetoder brukt. Mer nylig ble `os.path`-modulen i Python populær, som tillot å splitte en sti i kataloger, og filnavn i grunnnavn og filetternavn. Imidlertid krevde manipulering av filstier fortsatt kunnskap om datamaskinen et skript til slutt ville kjøre på. For eksempel, på alle Unix-baserte operativsystemer, som Linux eller MacOS, er kataloger adskilt med skråstreker (`/`), mens Microsoft Windows bruker bakstreker (`\`) (dette spesielle problemet kan omgås med `os.sep` og `os.path.join`, men ikke på en veldig praktisk måte).

Siden Python 3.4 (så, ganske nylig), eksisterer det en innebygd modul som letter mye av problemene med å håndtere filstier: [`pathlib`](https://docs.python.org/3/library/pathlib.html). Den gir et abstrakt lag på toppen av de faktiske operativsystemets filstier som er konsistent mellom datamaskiner. Et `pathlib.Path()`-objekt kan initieres med en filsti (som en `str`), når den opprettes uten et argument, refererer den til katalogen til skriptet eller notatblokkfilen.

```{code-cell} python
import pathlib
pathlib.Path()
```

Så langt er denne stien ikke sjekket mot den faktiske katalogstrukturen, men vi kan `resolve()` den for å konvertere den til en absolutt sti:

```{code-cell} python
path = pathlib.Path()
path = path.resolve()
path
```

:::{note}

Denne stien er nå utvidet for å gjenspeile katalogstrukturen til datamaskinen den ble kjørt på. Mest sannsynlig har kopien du leser akkurat nå blitt generert på [readthedocs.io](https://readthedocs.io/) servere, og *‘nåværende arbeidskatalog’* er på et sted du ikke forventet.
:::

Dette stiobjektet har nå en rekke egenskaper og metoder. For eksempel kan vi teste om stien eksisterer i filsystemet, eller om den er en katalog:

```{code-cell} python
path.exists()
```

```{code-cell} python
path.is_dir()
```

Vi kunne også omdøpe eller slette stien (men la oss ikke gjøre dette med kursinnholdet!):

```{code-cell} python
# path.rename("new name")

# path.unlink()  # delete if path is a file
# path.rmdir()  # delete if path is a directory
```

Endelig, for å traversere innenfor denne stien, trenger du ikke å tenke på om du kjører skriptet på Windows eller Linux, og du trenger definitivt ikke å bruke strengmanipulasjon. For å henvise til en mappe `data` i samme katalog som denne notatboken, bruk `/` (divisjonsoperatøren) for å legge til en annen stikomponent (kan være en streng). For eksempel, for å henvise til en mappe `data` innenfor samme katalog som denne notatboken, skriv følgende:

```{code-cell} python
data_directory = path / "data"
data_directory
```

For å henvise til ‘en katalog opp’ fra en sti, bruk dens `.parent`-egenskap:

```{code-cell} python
path.parent
```

`Path()`-objekter kan brukes (nesten) hvor som helst en filsti forventes som en variabel av typen `str`, da den automatisk *typekaster* (konverterer) seg selv til en passende type.

I data science-prosjekter er det en god vane å definere en konstant i begynnelsen av hver notatbok som peker på datamappen, eller flere konstanter for å peke på, for eksempel, inngangs- og utgangsmapper. I dagens øvelser bruker vi forskjellige prøvedatasett fra filer lagret i samme *datamappe*. Øverst i notatbøkene definerer vi derfor en konstant `DATA_DIRECTORY` som vi senere kan bruke til å finne prøvedatasettfilene:

```{code-cell} python
# location (directory) of the notebook
import pathlib
NOTEBOOK_PATH = pathlib.Path().resolve()
DATA_DIRECTORY = NOTEBOOK_PATH / "data"
```

```{code-cell} python
# this can then be used, for instance, in `geopandas.read_file()` (see next section):
import geopandas
data_set = geopandas.read_file(DATA_DIRECTORY / "finland_municipalities" / "finland_municipalities_2021.gpkg")
data_set.plot()
```

:::{admonition} Konstanter?
:class: note

*Konstanter* er verdier som ikke kan endres når de er definert. Dette hjelper med å optimere programmets hastighet og minneavtrykk, og lar også programmereren stole på at en konstant har en gyldig verdi.

Python kjenner ikke konseptet med en konstant, per se. Imidlertid er det en konvensjon å behandle variabler med et all-uppercase navn som konstanter (f.eks. de skal ikke endres).
:::

:::{caution}

I eksemplene ovenfor brukte vi en sti som vi `resolve()` tidligere. Dette forbedrer ytterligere kompatibilitet og konsistens mellom operativsystemer og lokale installasjoner.

Spesielt når du bruker stien til den gjeldende filen (som i `pathlib.Path()` uten parametere), anbefaler vi å løse stien før du går inn i noen annen katalog.
:::