---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.1
    split_at_heading: true
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Romlig join

*Romlige joiner* er operasjoner som kombinerer data fra to eller flere romlige datasett
basert på deres geometriske forhold. I de forrige delene fikk vi
kjennskap til to spesifikke tilfeller av romlige joiner: [Punkt-i-polygon
spørringer](point-in-polygon-queries) og [kryssforespørsler](intersect). Men,
det er mer å bruke det geometriske forholdet mellom trekk og mellom
hele lag.

Romlige joinoperasjoner krever to inngangsparametere: *predikatet*, dvs. den
geometriske betingelsen som må oppfylles mellom to geometrier, og
*join-typen*: om bare rader med matchende geometrier beholdes, eller alle av en
inputtabellens rader, eller alle poster.

*Geopandas* (ved hjelp av `shapely` for å implementere geometriske forhold) [støtter en
standard sett med geometriske
predikater](https://geopandas.org/en/stable/docs/user_guide/mergingdata.html#binary-predicate-joins),
som ligner de fleste GIS analyseverktøy og applikasjoner:

- intersects
- contains
- within
- touches
- crosses
- overlaps

Geometriske predikater uttrykkes som verb, så de har en intuitiv
betydning. Se [shapely bruker
manual](https://shapely.readthedocs.io/en/stable/manual.html#binary-predicates)
for en detaljert beskrivelse av hvert geometrisk predikat.


:::{admonition} Binære geometriske predikater
:class: hint

Shapely støtter flere *binære geometriske predikater* enn geopandas implementerer
for romlige joiner. Hva er de? Kan de uttrykkes ved å kombinere de
implementerte?
:::

Når det gjelder *join-typen*, implementerer geopandas tre forskjellige alternativer:

- *left*: behold alle poster av *left* data-rammen, fyll med tomme verdier hvis
  ingen match, behold *left* geometrikolonne
- *right*: behold alle poster av *left* data-rammen, fyll med tomme verdier hvis
  ingen match, behold *right* geometrikolonne
- *inner*: behold bare poster av matchende poster, behold *left* geometrikolonne


:::{tip}
[PyGIS
bok](https://pygis.io/docs/e_spatial_joins.html) har en flott oversikt over
romlige predikater og join-typer med forklarende tegninger.
:::


---


## Last inn inngangsdata

Som et praktisk eksempel, la oss finne befolkningstettheten på hver av
adressene fra [tidligere i denne leksjonen](geocoding-in-geopandas), ved å kombinere
datasettet med data fra et befolkningsnett.

Befolkningsnettdata er tilgjengelig fra [HSY, Helsingforsregionens
Miljøtjenester](https://www.hsy.fi/en/environmental-information/open-data/), for
eksempel via deres WFS-endepunkt.

```{code-cell} python
import pathlib 
NOTEBOOK_PATH = pathlib.Path().resolve()
DATA_DIRECTORY = NOTEBOOK_PATH / "data"
```


```{code}
import geopandas

adresser = geopandas.read_file(DATA_DIRECTORY / "adresser.gpkg")

befolkningsnett = geopandas.read_file(
    (
        "https://kartta.hsy.fi/geoserver/wfs"
        "?service=wfs"
        "&version=2.0.0"
        "&request=GetFeature"
        "&typeName=asuminen_ja_maankaytto:Vaestotietoruudukko_2020"
        "&srsName=EPSG:3879"
    ),
)
befolkningsnett.crs = "EPSG:3879"  # for WFS data, må CRS spesifiseres manuelt
```

```{code-cell} python
:tags: ["remove-input", "remove-output"]

import geopandas

adresser = geopandas.read_file(DATA_DIRECTORY / "adresser.gpkg")

befolkningsnett = geopandas.read_file(
    "https://avoidatastr.blob.core.windows.net/avoindata/AvoinData/"
    "6_Asuminen/Vaestotietoruudukko/Shp/Vaestotietoruudukko_2021_shp.zip"
)
befolkningsnett = (
    befolkningsnett[["ASUKKAITA", "geometri"]]
    .rename(columns={"ASUKKAITA": "asukkaita"})
)
```

:::{admonition} Sammenkjede lange strenger
:class: note

I WFS-adressen ovenfor delte vi en lang streng over flere linjer. Strenger
mellom parenteser blir automatisk sammenkjedet (satt sammen), selv
uten noen operator (f.eks., `+`).

For klarhetens skyld har eksempelet en ekstra sett med parenteser, men
allerede parentesene til metodekallet ville være tilstrekkelig.
:::


---


```{code-cell} python
befolkningsnett.head()
```

Befolkningsnettet har mange kolonner, og alle kolonnenavnene er på
finsk. La oss fjerne (slette) alle kolonnene bortsett fra befolkningstotalen,
og gi de gjenværende engelske navn:

```{code-cell} python
befolkningsnett = befolkningsnett[["asukkaita", "geometri"]]
befolkningsnett = befolkningsnett.rename(columns={"asukkaita": "population"})
```

Til slutt, beregn befolkningstettheten ved å dele antall innbyggere
av hver rutenettcelle med arealet i km²:

```{code-cell} python
befolkningsnett["population_density"] = (
    befolkningsnett["population"]
    / (befolkningsnett.area / 1_000_000)
)
befolkningsnett.head()
```

:::{admonition} Koding stil: store tall, operatorer i flerlinjeuttrykk
:class: tip

Hvis du trenger å bruke veldig store tall, for eksempel, i eksempelet ovenfor, *1
million* for å konvertere m² til km², kan du bruke understrekingskarakterer (`_`) som
tusenvis separatorer. Python-tolkeren vil behandle en sekvens av tall
sammenvevd med understrekinger som en vanlig numerisk verdi.
[Du kan bruke samme syntaks for å gruppere
tall](https://peps.python.org/pep-0515/) etter en annen logikk, for eksempel,
for å gruppere heksadesimale eller binære verdier i grupper av fire.

I tilfelle et uttrykk, for eksempel, en matematisk formel, sprer seg over
flere linjer, anses det for å være god koding stil å plassere en operator i
begynnelsen av en ny linje, i stedet for å la den hale i den forrige linjen. Dette er
anses som mer lesbart, som forklart i [PEP-8 styling
retningslinjer](https://peps.python.org/pep-0008/#should-a-line-break-before-or-after-a-binary-operator)
:::


---

## Join inngangslagene


Nå er vi klare til å utføre den romlige joinen mellom de to lagene.
Husk: målet er å finne befolkningstettheten rundt hver av adressene
punktene. Vi ønsker å knytte befolkningstetthetsinformasjon fra
`befolkningsnett` polygonlag til `adresser` punktlag, avhengig av
om **punktet er innenfor polygonen**. Under denne operasjonen ønsker vi å
**beholde geometriene til punktlaget**.

Før vi kan fortsette med join-operasjonen, må vi sørge for at de to
lagene er i det samme kartografiske referansesystemet:

```{code-cell} python
:tags: ["raises-exception"]

assert adresser.crs == befolkningsnett.crs, "CRS er ikke identiske"
```

De deler ikke samme CRS, la oss reprojisere en av dem:

```{code-cell} python
befolkningsnett = befolkningsnett.to_crs(adresser.crs)
```

Nå er vi klare til å utføre den faktiske romlige joinen ved hjelp av
[`geopandas.GeoDataFrame.sjoin()`](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.sjoin.html)
metoden. Husk, vi ønsker å bruke et *within* geometrisk predikat og beholde
punktlagets geometrier (i eksempelet nedenfor er *left* data-rammen).

```{code-cell} python
adresser_med_befolkningsdata = adresser.sjoin(
    befolkningsnett,
    how="left",
    predicate="within"
)
adresser_med_befolkningsdata.head()
```


Det ser flott ut! Vi har nå et adresse datasett med befolkningstetthets
informasjon knyttet til det. 


---


Som en endelig oppgave, la oss se på hvordan du kan plotte data ved hjelp av en *gradert*
kartografisk visualiseringsskjema. 

`geopandas.GeoDataFrame.plot()` metoden kan variere kartfargene avhengig av en kolonnes verdier ved å sende inn navnet som et navngitt argument `column`. I tillegg til det, aksepterer metoden mange argumenter for å påvirke stilen på kartet. Blant dem er `scheme` og `cmap` som definerer [kategoriseringsskjemaet](https://geopandas.org/en/stable/gallery/choropleths.html), og [fargekartet](https://matplotlib.org/stable/tutorials/colors/colormaps.html) som brukes. Mange flere argumenter sendes gjennom til `matplotlib`, som `markersize` for å sette størrelsen på punktsymboler, og `facecolor` for å sette fargen på polygonområder. For å tegne en legend, sett `legend` til `True`, for å sette størrelsen på figuren, send inn en tuple (med verdier i tommer) som `figsize`.

```{code-cell} python
ax = adresser_med_befolkningsdata.plot(
    figsize=(10, 10),
    column="population_density",
    cmap="Reds",
    scheme="quantiles",
    markersize=15,
    legend=True
)
ax.set_title("Befolkningstetthet rundt adressepunktene")
```


---

Vi kan bruke de samme argumentene for å plotte et befolkningstetthetskart ved hjelp av
hele `befolkningsnett` datasettet:

```{code-cell} python
ax = befolkningsnett.plot(
    figsize=(10, 10),
    column="population_density",
    cmap="Reds",
    scheme="quantiles",
    legend=True
)
ax.set_title("Befolkningstetthet i Helsingfors storbyområde")

```


---


Til slutt, husk å lagre output data-rammen til en fil. Vi kan legge den til
den eksisterende *GeoPackage* ved å spesifisere et nytt lag navn:

```{code-cell} python
adresser_med_befolkningsdata.to_file(
    DATA_DIRECTORY / "adresser.gpkg",
    layer="adresser_med_befolkningsdata"
)
