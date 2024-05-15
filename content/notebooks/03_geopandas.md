---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
    split_at_heading: true
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Geopandas: en introduksjon

I denne seksjonen vil vi dekke det grunnleggende med *geopandas*, et Python-bibliotek for
å samhandle med geospatial vektordata.

[Geopandas](https://geopandas.org/) gir et brukervennlig grensesnitt til vektordatasett. Det kombinerer mulighetene til *pandas*, datapakkene
vi ble kjent med i [Geo-Python
kurset](https://geo-python-site.readthedocs.io/en/latest/lessons/L5/pandas-overview.html),
med geometrikapabilitetene til
[shapely](../lesson-1/geometry-objects), [geospatial-filformateringstøtte
fra fiona](vector-data-io) og [kartprojeksjonsbibliotekene til
pyproj](map-projections).

Hoveddatastrukturene i geopandas er `GeoDataFrame`s og `GeoSeries`. De
utvider funksjonaliteten til `pandas.DataFrame`s og `pandas.Series`. Dette betyr
at **vi kan bruke alle våre *pandas* ferdigheter også når vi jobber med
*geopandas*!**. 

:::{tip}

Hvis du føler at du trenger å oppfriske hukommelsen om pandas, gå tilbake til
[leksjon
5](https://geo-python-site.readthedocs.io/en/latest/lessons/L5/pandas-overview.html)
og [leksjon
6](https://geo-python-site.readthedocs.io/en/latest/notebooks/L6/advanced-data-processing-with-pandas.html)
av Geo-Python.
:::

Det er en nøkkelforskjell mellom pandas data rammer og geopandas
[`GeoDataFrame`s](https://geopandas.org/en/stable/docs/user_guide/data_structures.html#geodataframe):
en `GeoDataFrame` inneholder en ekstra kolonne for geometrier. Som standard er
navnet på denne kolonnen `geometry`, og det er en
[`GeoSeries`](https://geopandas.org/en/stable/docs/user_guide/data_structures.html#geoseries)
som inneholder geometrier (punkter, linjer, polygoner, ...) som
`shapely.geometry` objekter.

```{code-cell} python python
:tags: [remove-input]

import pathlib
import geopandas
import numpy
import pandas

DATA_DIRECTORY = pathlib.Path().resolve() / "data"

HIGHLIGHT_STYLE = "background: #f66161;"

# så følgende blokk er litt dårlig magi for å få tabellutdataen til å se
# fin ut (denne cellen er skjult, vi er bare interessert i en kort tabellisting
# der geometrikolonnen er fremhevet).
#
# For dette, vi
#    1. konverterer geopandas tilbake til en ‘normal’ pandas.DataFrame med en forkortet
#       WKT-streng i geometrikolonnen
#    1b. samtidig som vi gjør det, blir vi kvitt de fleste av kolonnene (gir de gjenværende kolonner nye navn)
#    2. bruker stilen på alle celler i kolonnen "geometry", og til aksen-1-indeksen "geometry"

# Hvorfor gikk jeg via en ‘plain’ `pandas.DataFrame`?
# `pandas.set_option("display.max_colwidth", 40)` ble ignorert, så dette så ut som den reneste måten

df = geopandas.read_file(DATA_DIRECTORY / "finland_topographic_database" / "m_L4132R_p.shp")

df["geom"] = df.geometry.to_wkt().apply(lambda wkt: wkt[:40] + " ...")

df = df[["RYHMA", "LUOKKA", "geom"]]
df = df.rename(columns={"RYHMA": "GRUPPE", "LUOKKA": "KLASSE", "geom": "geometry"})

(
    df.head().style
        .applymap(lambda x: HIGHLIGHT_STYLE, subset=["geometry"])
        .apply_index(lambda x: numpy.where(x.isin(["geometry"]), HIGHLIGHT_STYLE, ""), axis=1)
)
```

---

## Inngangsdata: Finsk topografisk database

I denne leksjonen vil vi jobbe med [National Land Survey of Finland (NLS)/Maanmittauslaitos (MML) topografiske database](https://www.maanmittauslaitos.fi/en/maps-and-spatial-data/expert-users/product-descriptions/topographic-database). 
- Datasettet er lisensiert under NLS’ [åpen data lisens](https://www.maanmittauslaitos.fi/en/opendata-licence-cc40) (CC BY 4.0).
- Strukturen til dataene er beskrevet i en [separat Excel-fil](http://www.nic.funet.fi/index/geodata/mml/maastotietokanta/2022/maastotietokanta_kohdemalli_eng_2019.xlsx).
- Ytterligere informasjon om filnavngivning er tilgjengelig på [fairdata.fi](https://etsin.fairdata.fi/dataset/5023ecc7-914a-4494-9e32-d0a39d3b56ae) (denne lenken er relatert til 2018-utgaven av den topografiske databasen, men er fremdeles gyldig).

For denne leksjonen har vi skaffet oss et utvalg av den topografiske databasen som
shapefiler fra Helsinki-regionen i Finland via [CSC’s Paituli nedlastingsportal](https://paituli.csc.fi). Du kan finne filene i `data/finland_topographic_database/`.

:::{figure} ../../static/images/lesson-2/paituli-download_700x650px.png
:alt: Skjermbilde av Paituli-nedlastingssiden

Paituli *spatial download service* tilbyr data fra en lang liste av nasjonale institutter og etater.
:::


---

## Les og utforsk geospatial datasett

Før vi prøver å laste opp noen filer, la oss ikke glemme å definere en konstant
som peker til vår datamappe:

```{code-cell} python python
import pathlib 
NOTEBOOK_PATH = pathlib.Path().resolve()
DATA_DIRECTORY = NOTEBOOK_PATH / "data"
```

I denne leksjonen vil vi fokusere på **terrengobjekter** (Feature-gruppe:
"Terrain/1" i den topografiske databasen). Terrain/1-funksjonsgruppen inneholder
flere funksjonsklasser. 

**Målet vårt i denne leksjonen er å lagre alle Terrain/1
funksjonsklassene i separate filer**.

*Terrain/1-funksjoner i den topografiske databasen:*

|  funksjonsklasse | Navn på funksjon                                           | Funksjonsgruppe |
|----------------|------------------------------------------------------------|---------------|
| 32421          | Motor trafikk område                                       | Terrain/1     |
| 32200          | Kirkegård                                                   | Terrain/1     |
| 34300          | Sand                                                       | Terrain/1     |
| 34100          | Stein - område                                             | Terrain/1     |
| 34700          | Steinete område                                            | Terrain/1     |
| 32500          | Steinbrudd                                                  | Terrain/1     |
| 32112          | Område for utvinning av mineralressurser, finkornet materiale | Terrain/1     |
| 32111          | Område for utvinning av mineralressurser, grovkornet materiale | Terrain/1     |
| 32611          | Felt                                                       | Terrain/1     |
| 32612          | Hage                                                       | Terrain/1     |
| 32800          | Eng                                                        | Terrain/1     |
| 32900          | Park                                                       | Terrain/1     |
| 35300          | Myrland                                                    | Terrain/1     |
| 35412          | Myr, enkel å krysse skogkledd                              | Terrain/1     |
| 35411          | Åpen myr, enkel å krysse tre


:::{admonition} Søk etter filer ved hjelp av et mønster
:class: hint

(#search-for-files-using-a-pattern)=
En `pathlib.Path` (som `DATA_DIRECTORY`) har en hendig metode for å liste opp alle
filer i en katalog (eller underkataloger) som samsvarer med et mønster:
[`glob()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob).
For å liste opp alle shapefilene i vår topografiske databasekatalog, kan vi bruke følgende uttrykk:

```{code}
(DATA_DIRECTORY / "finland_topographic_database").glob("*.shp")
```

I søkemønsteret representerer `?` ett enkelt tegn, `*` flere
(eller ingen, eller ett) tegn, og `**` flere tegn som kan inkludere
underkataloger.

La du merke til parentesene i kodeeksemplet ovenfor? De fungerer akkurat som
de ville i et matematisk uttrykk: først blir uttrykket inne i
parentesene evaluert, bare da koden utenfor.
:::

Hvis du tar en rask titt på datamappen ved hjelp av en filutforsker, vil
du legge merke til at den topografiske databasen består av *mange* mindre filer. Deres
navn følger en strengt definert 
[navngivningskonvensjon](https://etsin.fairdata.fi/dataset/5023ecc7-914a-4494-9e32-d0a39d3b56ae),
i henhold til denne filnavngivningskonvensjonen, starter alle filer vi er interessert i
(*Terrain/1* og *polygoner*) med en bokstav `m` og slutter med en `p`.

Vi kan bruke `glob()` mønstersøksfunksjonaliteten til å finne disse filene:

```{code-cell} python python
TOPOGRAPHIC_DATABASE_DIRECTORY = DATA_DIRECTORY / "finland_topographic_database"

TOPOGRAPHIC_DATABASE_DIRECTORY
```

```{code-cell} python python
list(TOPOGRAPHIC_DATABASE_DIRECTORY.glob("m*p.shp"))
```

(Merk at `glob()` returnerer en iterator, men for nå konverterer vi
den raskt til en liste)

Det ser ut til at vårt inngangsdatasett bare har én fil som samsvarer med vårt søkemønster.
Vi kan lagre filnavnet i en ny variabel, ved å velge det første elementet i listen (indeks 0):

```{code-cell} python python
input_filename = list(TOPOGRAPHIC_DATABASE_DIRECTORY.glob("m*p.shp"))[0] 
```

Nå er det endelig på tide å åpne filen og se på innholdet:

```{code-cell} python python
import geopandas
data = geopandas.read_file(input_filename)
```

Først, sjekk datatype av det leste datasettet:

```{code-cell} python python
type(data)
```

Alt gikk bra, og vi har en `geopandas.GeoDataFrame`. 
La oss også utforske dataene: (1) skriv ut de første få radene, og 
(2) list opp kolonnene.

```{code-cell} python python
data.head()
```

```{code-cell} python python
data.columns
```

Å herregud! Dette datasettet har mange kolonner, og alle kolonnenavnene er på
finsk.

La oss velge noen nyttige og oversette navnene deres til
engelsk. Vi beholder ’RYHMA’ og ’LUOKKA’ (‘gruppe’ og ‘klasse’, henholdsvis),
og selvfølgelig kolonnen `geometry`.

```{code-cell} python python
data = data[["RYHMA", "LUOKKA", "geometry"]]
```

Å endre navn på en kolonne i (geo)pandas fungerer ved å sende en ordbok til
`DataFrame.rename()`. I denne ordboken er nøklene de gamle navnene, verdiene
de nye:

```{code-cell} python python
data = data.rename(
    columns={
        "RYHMA": "GROUP",
        "LUOKKA": "CLASS"
    }
)
```

Hvordan ser datasettet ut nå?

```{code-cell} python python
data.head()
```

:::{admonition} Sjekk din forståelse:
:class: hint

Bruk dine pandas ferdigheter på dette geopandas datasettet for å finne ut følgende
informasjon:

- Hvor mange rader har datasettet?
- Hvor mange unike klasser?
- ... og hvor mange unike grupper?
:::


---

### Utforsk datasettet på et kart:

Som geografer, elsker vi kart. Men utover det, er det alltid en god idé å
utforske et nytt datasett også på et kart. For å lage et enkelt kart av en
`geopandas.GeoDataFrame`, bruk ganske enkelt dens `plot()` metode. Den fungerer likt som
pandas (se [Leksjon 7 av Geo-Python 
kurset](https://geo-python.github.io/site/notebooks/L7/matplotlib.html), men
**tegner et kart basert på geometriene i datasettet** i stedet for et diagram.

```{code-cell} python python
data.plot()
```

Voilá! Det er faktisk så enkelt å lage et kart ut av et geografisk datasett.
Geopandas posisjonerer automatisk kartet ditt på en måte som dekker hele
utstrekningen av dataene dine.

:::{note}
Hvis du bor i Helsinki-regionen, kan du kjenne igjen noen av formene på
kartet ;)
:::

### Geometrier i geopandas

Geopandas drar nytte av shapelys geometriobjekter. Geometrier lagres
i en kolonne kalt *geometry*.

La oss skrive ut de første 5 radene av kolonnen `geometry`:

```{code-cell} python python
data.geometry.head()
```

Se og behold, kolonnen `geometry` inneholder kjente verdier:
*Well-Known Text* (WKT) strenger. La deg ikke lure, de er faktisk,
`shapely.geometry` objekter (du husker kanskje fra [forrige ukes
leksjon](../lesson-1/geometry-objects)) som når `print()`ed eller typekonvertert til
en `str`, blir representert som en WKT-streng).

Siden geometriene i en `GeoDataFrame` er lagret som shapely-objekter, kan vi
bruke **shapely metoder** for å håndtere geometrier i geopandas.

La oss ta en nærmere titt på (en av) polygon-geometriene i terrengdatasettet,
og prøve å bruke noe av shapely-funksjonaliteten vi allerede er kjent med. For klarhets skyld, vil vi først jobbe med geometrien til den aller første posten:

```{code-cell} python python
# Verdien av kolonnen `geometry` i rad 0:
data.at[0, "geometry"]
```

```{code-cell} python python
# Skriv ut informasjon om arealet 
print(f"Område: {round(data.at[0, 'geometry'].area)} m².")
```

:::{admonition} Områdemålenhet
:class: note

Her kjenner vi koordinatreferansesystemet (CRS) til inngangsdatasettet. CRS definerer også måleenheten (i vårt tilfelle, meter). Derfor kan vi skrive ut det beregnede området, inkludert en områdemåleenhet (kvadratmeter).
:::


La oss gjøre det samme for flere rader, og utforske ulike måter å gjøre det på.
Først bruker vi det pålitelige og prøvde `iterrows()`-mønsteret vi lærte i [leksjon 6
av Geo-Python kurset](https://geo-python.github.io/site/notebooks/L6/pandas/advanced-data-processing-with-pandas.html#Iterating-rows-and-using-self-made-functions-in-Pandas).

```{code-cell} python ipython3
# Iterer over de første 5 radene i datasettet
for index, row in data[:5].iterrows():
    polygon_area = row["geometry"].area
    print(f"Polygonet i rad {index} har et overflateareal på {polygon_area:0.1f} m².")
```

Som du ser er alle **pandas** funksjoner, som `iterrows()`-metoden, tilgjengelige i geopandas uten behov for å kalle pandas separat. Geopandas bygger på toppen av pandas, og arver mesteparten av funksjonaliteten.

Selvfølgelig er ikke `iterrows()`-mønsteret den mest praktiske og effektive måten
å beregne arealet til mange rader. Både `GeoSeries` (geometri-kolonner) og
`GeoDataFrame`s har en `area`-egenskap:

```{code-cell} python ipython3
# `area`-egenskapen til en `GeoDataFrame`
data.area
```

```{code-cell} python ipython3
# `area`-egenskapen til en `GeoSeries`
data["geometry"].area
```

Det er enkelt å lage en ny kolonne som holder arealet:

```{code-cell} python ipython3
data["area"] = data.area
data
```

:::{admonition} Beskrivende statistikk
:class: hint

Husker du hvordan du beregner *minimum*, *maksimum*, *sum*, *gjennomsnitt*, og
*standardavvik* av en pandas-kolonne? ([Leksjon 5 av
Geo-Python](https://geo-python-site.readthedocs.io/en/latest/notebooks/L5/exploring-data-using-pandas.html#descriptive-statistics))
Hva er disse verdiene for arealkolonnen i datasettet?
:::



## Lagre en delmengde av data til en fil

[I forrige avsnitt](./vector-data-io.md#writing-geospatial-data-to-a-file), lærte vi
hvordan vi skriver en hel `GeoDataFrame` til en fil. Vi kan også skrive en
filtrert delmengde av et datasett til en ny fil, f.eks. for å hjelpe med behandling
komplekse datasett.

Først, isoler innsjøene i inngangsdatasettet (klassenummer `36200`, se tabell
over):

```{code-cell} python ipython3
lakes = data[data.CLASS == 36200]
```

Deretter, tegn datadelmengden for å visuelt sjekke om den ser riktig ut:

```{code-cell} python ipython3
lakes.plot()
```

Og til slutt, skriv de filtrerte dataene til en Shapefile:

```{code-cell} python ipython3
lakes.to_file(DATA_DIRECTORY / "finland_topographic_database" / "lakes.shp")
```

Sjekk [Vector Data I/O](vector-data-io) avsnittet for å se hvilke dataformater
geopandas kan skrive til.



## Gruppering av data

En spesielt nyttig metode i (geo)pandas' datarammer er deres grupperingsfunksjon: [`groupby()`](https://pandas.pydata.org/docs/user_guide/groupby.html)
kan **dele data inn i grupper** basert på noen kriterier, **bruke** en funksjon
individuelt til hver av gruppene, og **kombinere** resultater av en slik
operasjon i en felles datastruktur.

Vi har brukt denne funksjonen tidligere: i [Geo-Python, 
leksjon 6](https://geo-python-site.readthedocs.io/en/latest/notebooks/L6/advanced-data-processing-with-pandas.html#aggregating-data-in-pandas-by-grouping).

Vi kan bruke *gruppering* her for å dele inngangsdatasettet vårt i delmengder som relatere
til hver av `CLASS`ene i terrengdekning, deretter lagre en separat fil for hver
klasse.

La oss starte dette ved igjen å ta en titt på hvordan datasettet faktisk ser ut:

```{code-cell} python ipython3
data.head()
```

Husk: kolonnen `CLASS` inneholder informasjon om en polygons arealbrukstype. Bruk metoden [`pandas.Series.unique()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.unique.html) for å liste alle verdier som forekommer:

```{code-cell} python ipython3
data["CLASS"].unique()
```

For å gruppere data, bruk data-rammens `groupby()` metode, oppgi et kolonnenavn som parameter:

```{code-cell} python ipython3
grouped_data = data.groupby("CLASS")
grouped_data
```

Så, `grouped_data` er et `DataFrameGroupBy` objekt. Inne i et `GroupBy` objekt,
er egenskapen `groups` en ordbok som fungerer som en oppslagstabell: den registrerer
hvilke rader som hører til hvilken gruppe. Nøklene i ordboken er de unike
verdiene av gruppekolonnen:

```{code-cell} python
grouped_data.groups
```

Imidlertid kan man også ganske enkelt iterere over hele `GroupBy` objektet. La oss
telle hvor mange rader med data hver gruppe har:

```{code-cell} python
for key, group in grouped_data:
    print(f"Terrengklasse {key} har {len(group)} rader.")
```

Det er for eksempel 56 innsjøpolygoner (klasse `36200`) i inngangsdatasettet.

For å få alle rader som tilhører en bestemt gruppe, bruk `get_group()`
metoden, som returnerer en helt ny `GeoDataFrame`:

```{code-cell} python
lakes = grouped_data.get_group(36200)
type(lakes)
```

:::{caution}
Indekset i den nye data-rammen forblir den samme som i det ugrupperte inngangsdatasettet.
Dette kan være nyttig, for eksempel når du vil slå sammen de grupperte dataene
tilbake til de originale inngangsdataene.
:::


## Skriv grupperte data til separate filer

Nå har vi alle nødvendige verktøy for hånden for å dele inngangsdataene i
separate datasett for hver terrengklasse, og skrive de individuelle delmengdene til
nye, separate, filer. Faktisk ser koden nesten for enkel ut, gjør den ikke?

```{code-cell} python
# Iterer over inngangsdataene, gruppert etter CLASS
for key, group in data.groupby("CLASS"):
    # lagre gruppen til en ny shapefile
    group.to_file(TOPOGRAPHIC_DATABASE_DIRECTORY / f"terrain_{key}.shp")
```

:::{admonition} Filnavn
:class: attention

Vi brukte en `pathlib.Path` kombinert med en f-streng for å generere den nye utdatafilens
sti og navn. Sjekk denne ukens avsnitt [Managing file
paths](managing-file-paths), og [Geo-Python leksjon
2](https://geo-python-site.readthedocs.io/en/latest/notebooks/L2/Python-basic-elements.html#f-string-formatting)
for å gå gjennom hvordan de fungerer.
:::


## Ekstra: lagre sammendragsstatistikk til CSV regneark

Når resultatene av en operasjon på en `GeoDataFrame` ikke inkluderer en
geometri, vil data-rammen som kommer ut automatisk bli en 'vanlig'
`pandas.DataFrame`, og kan lagres til standard tabellformater.

En interessant anvendelse av dette er å lagre grunnleggende beskrivende statistikk av
et geografisk datasett til en CSV-tabell. For eksempel ønsker vi kanskje å vite
arealet hver terrengklasse dekker.

Igjen starter vi med å gruppere inngangsdataene etter terrengklasser, og deretter beregne
summen av hvert klasses areal. Dette kan kondenseres til en linje med kode:

```{code-cell} python
area_information = data.groupby("CLASS").area.sum()
area_information
```

Vi kan deretter lagre den resulterende tabellen til en CSV-fil ved å bruke den standard pandas
tilnærmingen vi lærte om i [Geo-Python
leksjon 5](https://geo-python-site.readthedocs.io/en/latest/notebooks/L5/processing-data-with-pandas.html#writing-data-to-a-file).

```{code-cell} python
area_information.to_csv(TOPOGRAPHIC_DATABASE_DIRECTORY / "area_by_terrain_class.csv")
```